"""Finding powershell.exe for the Windows capture helper under WSL."""
# std imports
import os
import stat

# local
from ucs_detect import windows

RELATIVE = os.path.join('Windows', 'System32', 'WindowsPowerShell', 'v1.0', 'powershell.exe')


def _fake_windows_drive(root):
    path = root / RELATIVE
    path.parent.mkdir(parents=True)
    path.write_text('')
    path.chmod(path.stat().st_mode | stat.S_IXUSR)
    return str(path)


def _mounts(tmp_path, *lines):
    path = tmp_path / 'mounts'
    path.write_text(''.join(line + '\n' for line in lines))
    return str(path)


def test_powershell_on_path_wins(tmp_path, monkeypatch):
    """A powershell.exe on PATH is used as it is (a WSL login shell appends the Windows PATH)."""
    monkeypatch.setattr(windows.shutil, 'which', lambda name: '/on/path/powershell.exe')
    assert windows.find_powershell(_mounts(tmp_path)) == '/on/path/powershell.exe'


def test_powershell_found_through_the_drive_mount(tmp_path, monkeypatch):
    """An ssh login into WSL has no Windows PATH: powershell.exe is found on the C: mount."""
    monkeypatch.setattr(windows.shutil, 'which', lambda name: None)
    expected = _fake_windows_drive(tmp_path / 'c')
    mounts = _mounts(tmp_path,
                     r'drivers /usr/lib/wsl/drivers 9p ro,dirsync 0 0',
                     rf'C:\134 {tmp_path / "c"} 9p rw,noatime 0 0')
    assert windows.find_powershell(mounts) == expected


def test_powershell_mount_point_with_a_space(tmp_path, monkeypatch):
    """/proc/mounts writes a space in a mount point as \\040."""
    monkeypatch.setattr(windows.shutil, 'which', lambda name: None)
    expected = _fake_windows_drive(tmp_path / 'win c')
    escaped = str(tmp_path / 'win c').replace(' ', '\\040')
    mounts = _mounts(tmp_path, rf'C:\134 {escaped} drvfs rw 0 0')
    assert windows.find_powershell(mounts) == expected


def test_powershell_absent(tmp_path, monkeypatch):
    """No PATH entry and no Windows drive with it: None, so the X11 tools are used."""
    monkeypatch.setattr(windows.shutil, 'which', lambda name: None)
    mounts = _mounts(tmp_path,
                     r'drivers /usr/lib/wsl/drivers 9p ro 0 0',
                     rf'C:\134 {tmp_path / "empty"} 9p rw 0 0')
    assert windows.find_powershell(mounts) is None
    assert windows.find_powershell(str(tmp_path / 'no-such-file')) is None
