# Window capture helper for ucs-detect running under WSL.
#
# ucs_detect/windows.py starts one copy of this script with powershell.exe and keeps it running.
# Each request is one line on stdin: a command and its arguments, every argument hex-encoded
# UTF-8 so titles and paths need no quoting.  Each reply is one line on stdout: "OK <value>" or
# "ERR <message>".  "READY" is printed once the native helpers are compiled.

$ErrorActionPreference = 'Stop'

Add-Type -ReferencedAssemblies System.Drawing -TypeDefinition @'
using System;
using System.Text;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

public static class UcsCapture
{
    delegate bool EnumProc(IntPtr hwnd, IntPtr lparam);

    [StructLayout(LayoutKind.Sequential)] struct RECT { public int Left, Top, Right, Bottom; }
    [StructLayout(LayoutKind.Sequential)] struct POINT { public int X, Y; }

    [DllImport("user32.dll")] static extern bool EnumWindows(EnumProc callback, IntPtr lparam);
    [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern int GetWindowTextW(IntPtr hwnd, StringBuilder text, int count);
    [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern int GetClassNameW(IntPtr hwnd, StringBuilder text, int count);
    [DllImport("user32.dll")] static extern bool IsWindow(IntPtr hwnd);
    [DllImport("user32.dll")] static extern bool IsWindowVisible(IntPtr hwnd);
    [DllImport("user32.dll")] static extern bool IsIconic(IntPtr hwnd);
    [DllImport("user32.dll")] static extern bool GetClientRect(IntPtr hwnd, out RECT rect);
    [DllImport("user32.dll")] static extern bool ClientToScreen(IntPtr hwnd, ref POINT point);
    [DllImport("user32.dll")] static extern bool PrintWindow(IntPtr hwnd, IntPtr hdc, uint flags);
    [DllImport("user32.dll")] static extern bool SetForegroundWindow(IntPtr hwnd);
    [DllImport("user32.dll")] static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")] static extern int GetSystemMetrics(int index);
    [DllImport("user32.dll")] static extern IntPtr SetThreadDpiAwarenessContext(IntPtr context);

    const uint PW_CLIENTONLY = 1;
    const uint PW_RENDERFULLCONTENT = 2;
    static readonly IntPtr PER_MONITOR_AWARE_V2 = new IntPtr(-4);

    // Physical pixels, not the scaled size an unaware process is told.  Set on every call
    // because the setting belongs to the calling thread.
    static void Aware() { SetThreadDpiAwarenessContext(PER_MONITOR_AWARE_V2); }

    static IntPtr Handle(string id) { return new IntPtr(long.Parse(id)); }

    static string Text(IntPtr hwnd)
    {
        var text = new StringBuilder(1024);
        GetWindowTextW(hwnd, text, text.Capacity);
        return text.ToString();
    }

    // The largest visible, not minimized, top level window whose title contains the text.
    public static string Find(string title)
    {
        Aware();
        IntPtr best = IntPtr.Zero;
        long bestArea = -1;
        EnumWindows(delegate (IntPtr hwnd, IntPtr unused)
        {
            if (!IsWindowVisible(hwnd) || IsIconic(hwnd)) return true;
            if (Text(hwnd).IndexOf(title, StringComparison.Ordinal) < 0) return true;
            RECT rect;
            GetClientRect(hwnd, out rect);
            long area = (long)(rect.Right - rect.Left) * (rect.Bottom - rect.Top);
            if (area > bestArea) { bestArea = area; best = hwnd; }
            return true;
        }, IntPtr.Zero);
        return best == IntPtr.Zero ? "" : best.ToInt64().ToString();
    }

    public static string Geometry(string id)
    {
        Aware();
        RECT rect;
        if (!GetClientRect(Handle(id), out rect)) throw new Exception("no such window " + id);
        return (rect.Right - rect.Left) + " " + (rect.Bottom - rect.Top);
    }

    public static string Display()
    {
        Aware();
        return GetSystemMetrics(78) + " " + GetSystemMetrics(79);   // SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN
    }

    public static string Title(string id) { return IsWindow(Handle(id)) ? Text(Handle(id)) : ""; }

    public static string Class(string id)
    {
        var text = new StringBuilder(256);
        GetClassNameW(Handle(id), text, text.Capacity);
        return text.ToString();
    }

    public static string Active() { return GetForegroundWindow().ToInt64().ToString(); }

    public static string Focus(string id) { return SetForegroundWindow(Handle(id)) ? "1" : "0"; }

    static bool AllOneColor(Bitmap bitmap)
    {
        Color first = bitmap.GetPixel(0, 0);
        for (int y = 0; y < bitmap.Height; y += 7)
            for (int x = 0; x < bitmap.Width; x += 7)
                if (bitmap.GetPixel(x, y) != first) return false;
        return true;
    }

    // The client area as the compositor shows it; PW_RENDERFULLCONTENT reads the window's own
    // surface, so a covered window still captures.  A capture that comes back one flat color
    // (a window that paints nothing for PrintWindow) is retaken from the screen.
    public static string Capture(string id, string path)
    {
        Aware();
        IntPtr hwnd = Handle(id);
        RECT rect;
        if (!GetClientRect(hwnd, out rect)) throw new Exception("no such window " + id);
        int width = rect.Right - rect.Left, height = rect.Bottom - rect.Top;
        if (width <= 0 || height <= 0) throw new Exception("window " + id + " has no client area");
        using (var bitmap = new Bitmap(width, height, PixelFormat.Format24bppRgb))
        {
            string how = "printwindow";
            using (var graphics = Graphics.FromImage(bitmap))
            {
                IntPtr hdc = graphics.GetHdc();
                bool printed = PrintWindow(hwnd, hdc, PW_CLIENTONLY | PW_RENDERFULLCONTENT);
                graphics.ReleaseHdc(hdc);
                if (!printed || AllOneColor(bitmap))
                {
                    POINT origin = new POINT();
                    ClientToScreen(hwnd, ref origin);
                    graphics.CopyFromScreen(origin.X, origin.Y, 0, 0, new Size(width, height));
                    how = "screen";
                }
            }
            bitmap.Save(path, ImageFormat.Png);
            return how + " " + width + " " + height;
        }
    }

    public static string FromHex(string hex)
    {
        var bytes = new byte[hex.Length / 2];
        for (int i = 0; i < bytes.Length; i++) bytes[i] = Convert.ToByte(hex.Substring(i * 2, 2), 16);
        return Encoding.UTF8.GetString(bytes);
    }
}
'@

[Console]::Out.WriteLine('READY')
[Console]::Out.Flush()
while ($null -ne ($line = [Console]::In.ReadLine())) {
    $parts = @($line.Trim().Split(' ') | Where-Object { $_ -ne '' })
    if ($parts.Count -eq 0) { continue }
    $arguments = @($parts | Select-Object -Skip 1 | ForEach-Object { [UcsCapture]::FromHex($_) })
    try {
        switch ($parts[0]) {
            'find'     { $reply = [UcsCapture]::Find($arguments[0]) }
            'geometry' { $reply = [UcsCapture]::Geometry($arguments[0]) }
            'display'  { $reply = [UcsCapture]::Display() }
            'title'    { $reply = [UcsCapture]::Title($arguments[0]) }
            'class'    { $reply = [UcsCapture]::Class($arguments[0]) }
            'active'   { $reply = [UcsCapture]::Active() }
            'focus'    { $reply = [UcsCapture]::Focus($arguments[0]) }
            'capture'  { $reply = [UcsCapture]::Capture($arguments[0], $arguments[1]) }
            default    { throw "unknown command $($parts[0])" }
        }
        [Console]::Out.WriteLine("OK $reply")
    } catch {
        [Console]::Out.WriteLine('ERR ' + ($_.Exception.Message -replace '\s+', ' '))
    }
    [Console]::Out.Flush()
}
