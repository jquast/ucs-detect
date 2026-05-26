#!/bin/bash
# Docker entrypoint: start Xvfb, then exec the provided command.
# Only starts Xvfb when DISPLAY is set and we're inside Docker.

set -e

if [ -f /.dockerenv ] && [ -n "${DISPLAY:-}" ]; then
    DISPLAY_NUM="${DISPLAY#:}"
    # kill any leftover Xvfb on this display
    pgrep -f "Xvfb :${DISPLAY_NUM}" >/dev/null && kill "$(pgrep -f "Xvfb :${DISPLAY_NUM}")" 2>/dev/null || true
    rm -f "/tmp/.X${DISPLAY_NUM}-lock" "/tmp/.X11-unix/X${DISPLAY_NUM}" 2>/dev/null || true

    Xvfb "${DISPLAY}" -screen 0 1920x1080x24 -ac +extension RANDR &
    XVFB_PID=$!

    # wait for Xvfb to be ready
    for _ in $(seq 1 30); do
        if [ -e "/tmp/.X${DISPLAY_NUM}-lock" ]; then
            break
        fi
        sleep 0.1
    done

    # run the command, then clean up
    "$@"
    EXIT_CODE=$?

    kill "$XVFB_PID" 2>/dev/null || true
    wait "$XVFB_PID" 2>/dev/null || true
    exit $EXIT_CODE
fi

exec "$@"
