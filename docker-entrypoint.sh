#!/bin/bash
# Docker entrypoint: start Xvfb, dbus, xfconfd, then exec the provided command.
# Only starts services when DISPLAY is set and we're inside Docker.

set -e

if [ -f /.dockerenv ] && [ -n "${DISPLAY:-}" ]; then
    DISPLAY_NUM="${DISPLAY#:}"
    # kill any leftover Xvfb on this display
    pgrep -f "Xvfb :${DISPLAY_NUM}" >/dev/null && kill "$(pgrep -f "Xvfb :${DISPLAY_NUM}")" 2>/dev/null || true
    rm -f "/tmp/.X${DISPLAY_NUM}-lock" "/tmp/.X11-unix/X${DISPLAY_NUM}" 2>/dev/null || true

    Xvfb "${DISPLAY}" -screen 0 1920x1080x24 -ac +extension RANDR 2>/dev/null &
    XVFB_PID=$!

    # generate machine-id for D-Bus (many terminals need this)
    if [ ! -s /etc/machine-id ]; then
        dbus-uuidgen --ensure=/etc/machine-id
    fi

    # wait for Xvfb to be ready
    for _ in $(seq 1 30); do
        if [ -e "/tmp/.X${DISPLAY_NUM}-lock" ]; then
            break
        fi
        sleep 0.1
    done

    # XDG_RUNTIME_DIR owned by ucs
    export XDG_RUNTIME_DIR=/tmp/runtime-ucs
    mkdir -p "$XDG_RUNTIME_DIR"
    chown ucs:ucs "$XDG_RUNTIME_DIR"
    chmod 700 "$XDG_RUNTIME_DIR"

    # start a minimal window manager (needed by Electron apps for WM properties)
    openbox --replace &
    OPENBOX_PID=$!
    sleep 0.5

    # start Weston Wayland compositor as ucs (needed by foot)
    rm -f "${XDG_RUNTIME_DIR}/wayland-0" "${XDG_RUNTIME_DIR}/wayland-0.lock" 2>/dev/null
    sudo -u ucs XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR}" \
        weston --backend=x11-backend.so --socket=wayland-0 2>/dev/null &
    WESTON_PID=$!
    # wait for weston socket
    for _ in $(seq 1 30); do
        if [ -S "${XDG_RUNTIME_DIR}/wayland-0" ]; then
            break
        fi
        sleep 0.1
    done
    export WAYLAND_DISPLAY=wayland-0

    # launch a host xterm for key-inject terminals (screen, tmux, zellij, etc.)
    # that need a visible X11 window to type commands into
    sudo -u ucs DISPLAY="${DISPLAY}" XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR}" \
        xterm -geometry 80x24+0+0 -e sleep 999999 &
    HOST_XTERM_PID=$!
    sleep 0.5

    # start session D-Bus via dbus-launch (properly initializes the session)
    eval "$(sudo -u ucs XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR}" dbus-launch --sh-syntax)"
    DBUS_PID=$DBUS_SESSION_BUS_PID
    sleep 0.3

    # start xfconfd for xfce4-terminal (binary not in PATH)
    sudo -u ucs XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR}" \
        DBUS_SESSION_BUS_ADDRESS="${DBUS_SESSION_BUS_ADDRESS}" \
        /usr/lib/xfce4/xfconf/xfconfd &
    XFCONFD_PID=$!
    sleep 0.3

    # force software Vulkan (lavapipe) for Rio and other GPU terminals
    export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/lvp_icd.json

    # run the command as ucs, then clean up
    sudo -u ucs \
        DISPLAY="${DISPLAY}" \
        XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR}" \
        DBUS_SESSION_BUS_ADDRESS="${DBUS_SESSION_BUS_ADDRESS}" \
        VK_ICD_FILENAMES="${VK_ICD_FILENAMES}" \
        WAYLAND_DISPLAY="${WAYLAND_DISPLAY}" \
        NO_AT_BRIDGE=1 \
        GTK_MODULES= \
        GSETTINGS_BACKEND=memory \
        SESSION_MANAGER= \
        -- "$@"
    EXIT_CODE=$?

    kill "$XFCONFD_PID" 2>/dev/null || true
    kill "$HOST_XTERM_PID" 2>/dev/null || true
    kill "$DBUS_PID" 2>/dev/null || true
    kill "$WESTON_PID" 2>/dev/null || true
    kill "$OPENBOX_PID" 2>/dev/null || true
    kill "$XVFB_PID" 2>/dev/null || true
    wait "$XVFB_PID" 2>/dev/null || true
    exit $EXIT_CODE
fi

exec "$@"
