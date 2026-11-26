#!/bin/bash
# Start the Guacamole stack in this container and open the client in Chromium.
set -uo pipefail

export GUACAMOLE_HOME=/etc/guacamole
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export CATALINA_HOME=/opt/tomcat
export CATALINA_BASE=/opt/tomcat
export LANG=C.UTF-8
export LC_ALL=C.UTF-8

sudo mkdir -p /run/sshd
if ! sudo pgrep -F /tmp/sshd-guac.pid >/dev/null 2>&1; then
    sudo /usr/sbin/sshd -f /etc/ssh/sshd_config.d/guac.conf -E /tmp/sshd-guac.log
fi

if ! pgrep -x guacd >/dev/null; then
    /usr/bin/guacd -b 127.0.0.1 -L info > /tmp/guacd.log 2>&1 &
fi

if ! curl -sf -o /dev/null http://127.0.0.1:8080/guacamole/; then
    "$CATALINA_HOME/bin/catalina.sh" run > /tmp/tomcat.log 2>&1 &
fi

for _ in $(seq 1 120); do
    if curl -sf -o /dev/null http://127.0.0.1:8080/guacamole/; then
        break
    fi
    sleep 0.5
done

STAGE=$(ls -t /tmp/ucs-stages-*/*-Guacamole.sh \
            /tmp/ucs-run-series-*/run-Guacamole.sh 2>/dev/null | head -1)
if [ -n "$STAGE" ]; then
    ln -sf "$STAGE" /tmp/ucs-stage.sh
fi

KEY=$(sed -n 's/^json-secret-key:[[:space:]]*//p' /etc/guacamole/guacamole.properties)
JSON='{"username":"ucs","connections":{"ucs":{"protocol":"ssh","parameters":{"hostname":"127.0.0.1","port":"2222","username":"ucs","password":"ucs","terminal-type":"xterm-256color","font-name":"Unifont","font-size":"16","locale":"C.UTF-8","disable-copy":"true","disable-paste":"true"}}}}'

printf '%s' "$JSON" | openssl dgst -sha256 -mac HMAC -macopt hexkey:"$KEY" -binary > /tmp/sig.bin
cat /tmp/sig.bin > /tmp/plain.bin
printf '%s' "$JSON" >> /tmp/plain.bin
ENC=$(openssl enc -aes-128-cbc -K "$KEY" -iv 00000000000000000000000000000000 -nosalt -a -A -in /tmp/plain.bin)
DATA=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1],safe=""))' "$ENC")
ID=$(python3 -c 'import base64;print(base64.urlsafe_b64encode(b"ucs\0c\0json").decode().rstrip("="))')
URL="http://127.0.0.1:8080/guacamole/?data=$DATA#/client/$ID"

rm -rf /tmp/chromium-guac
exec chromium \
    --no-sandbox --test-type --deny-permission-prompts --disable-gpu --disable-dev-shm-usage --ozone-platform=x11 \
    --user-data-dir=/tmp/chromium-guac --no-first-run --no-default-browser-check \
    --disable-features=Translate,ClipboardUnsanitizedContent --disable-sync --disable-extensions \
    --disable-background-networking --disable-component-update --hide-crash-restore-bubble \
    --force-device-scale-factor=1 --window-size=1280,800 --window-position=0,0 \
    --app="$URL"
