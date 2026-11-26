# syntax=docker/dockerfile:1
# ucs-detect terminal testing image
# Arch Linux rolling release for latest terminal packages (libvte, foot, ghostty, etc.)
FROM archlinux:latest

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1

# bootstrap: update mirrors, install base deps, generate locale
RUN --mount=type=cache,target=/var/cache/pacman/pkg \
    pacman -Syu --noconfirm --needed \
    base-devel git sudo curl wget ccache \
    python python-pip dbus \
    && pacman -Scc --noconfirm \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# install X11, openbox, window manager, and terminal emulator packages

# X11 virtual framebuffer and automation tools
RUN --mount=type=cache,target=/var/cache/pacman/pkg \
    pacman -S --noconfirm --needed \
    xorg-server-xvfb \
    xdotool \
    xorg-xwd \
    xorg-xprop \
    xorg-xwininfo \
    openbox \
    imagemagick \
    gifsicle \
    weston \
    fontconfig \
    noto-fonts-emoji \
    xorg-fonts-misc \
    && pacman -Scc --noconfirm

# create non-root user for AUR builds and running tests
RUN useradd -m -s /bin/bash -u 1000 ucs && \
    echo "ucs ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    mkdir -p /home/ucs/.ccache && chown -R ucs:ucs /home/ucs/.ccache

# install yay (AUR helper) as ucs user, then install AUR-only terminals
RUN --mount=type=cache,target=/home/ucs/.ccache,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/ucs/.cache/yay,uid=1000,gid=1000 \
    --mount=type=cache,target=/var/cache/pacman/pkg \
    cd /tmp && \
    sudo -u ucs git clone https://aur.archlinux.org/yay-bin.git && \
    cd yay-bin && \
    sudo -u ucs makepkg -si --noconfirm && \
    cd / && rm -rf /tmp/yay-bin

# configure makepkg to use all CPUs minus 2, enable ccache, and tolerate old K&R-style code
RUN sed -i 's/^#\?MAKEFLAGS=.*/MAKEFLAGS="-j$(( $(nproc) > 2 ? $(nproc) - 2 : 1 ))"/' /etc/makepkg.conf && \
    sed -i 's/^CFLAGS="\(.*\)"/CFLAGS="\1 -Wno-error=incompatible-pointer-types"/' /etc/makepkg.conf && \
    sed -i 's/^BUILDENV=(\(.*\)!ccache\(.*\))/BUILDENV=(\1ccache\2)/' /etc/makepkg.conf && \
    sed -i 's|-fLC - --retry 3|-fL --retry 3|' /etc/makepkg.conf && \
    echo 'export CCACHE_DIR=/home/ucs/.ccache' >> /home/ucs/.bashrc && \
    echo 'export PATH=/usr/lib/ccache/bin:$PATH' >> /home/ucs/.bashrc

ENV CCACHE_DIR=/home/ucs/.ccache
ENV PATH=/usr/lib/ccache/bin:$PATH

# mlterm and domterm require compiling dependencies like gtk2 from scratch, consuming
# many several hours. We do not build for them, it is too much. They ask too much.
#
#RUN --mount=type=cache,target=/home/ucs/.ccache,uid=1000,gid=1000 \
#    --mount=type=cache,target=/home/ucs/.cache/yay,uid=1000,gid=1000 \
#    --mount=type=cache,target=/var/cache/pacman/pkg \
#    sudo -u ucs yay -S --noconfirm --needed --answerclean All --answerdiff None --removemake \
#    mlterm-git \
#    domterm-git \
#    && pacman -Scc --noconfirm

RUN --mount=type=cache,target=/home/ucs/.ccache,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/ucs/.cache/yay,uid=1000,gid=1000 \
    --mount=type=cache,target=/var/cache/pacman/pkg \
    sudo -u ucs yay -S --noconfirm --needed --answerclean All --answerdiff None --removemake \
    warp-terminal-bin \
    && pacman -Scc --noconfirm

RUN --mount=type=cache,target=/home/ucs/.ccache,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/ucs/.cache/yay,uid=1000,gid=1000 \
    --mount=type=cache,target=/var/cache/pacman/pkg \
    sudo -u ucs yay -S --noconfirm --needed --answerclean All --answerdiff None --removemake \
    extraterm-bin \
    bobcat-terminal-git \
    terminator-git \
    hyper-bin \
    && pacman -Scc --noconfirm

# install st (suckless terminal) from AUR
RUN --mount=type=cache,target=/home/ucs/.ccache,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/ucs/.cache/yay,uid=1000,gid=1000 \
    --mount=type=cache,target=/var/cache/pacman/pkg \
    sudo -u ucs yay -S --noconfirm --needed --answerclean All --answerdiff None --removemake st

# all terminal emulators available in Arch official repos
RUN --mount=type=cache,target=/var/cache/pacman/pkg \
    pacman -S --noconfirm --needed \
    foot \
    ghostty \
    kitty \
    alacritty \
    konsole \
    xfce4-terminal \
    gnome-terminal \
    lxterminal \
    qterminal \
    rxvt-unicode \
    xterm \
    cool-retro-term \
    terminology \
    zutty \
    wezterm \
    contour \
    rio \
    tmux \
    screen \
    zellij \
    vim \
    putty \
    vulkan-swrast \
    xfconf \
    && pacman -Scc --noconfirm

# remove nvidia EGL vendor config -- nvidia-utils was pulled in by rio,
# but without a real GPU its libEGL_nvidia.so crashes Xvfb at startup
RUN rm -f /usr/share/glvnd/egl_vendor.d/10_nvidia.json

# Apache Guacamole... version, install all configured manually
ARG GUACAMOLE_VERSION=1.6.0
ARG TOMCAT_VERSION=9.0.124

RUN --mount=type=cache,target=/var/cache/pacman/pkg \
    pacman -S --noconfirm --needed \
    chromium \
    openssh \
    jre17-openjdk \
    libssh \
    libwebp \
    libjpeg-turbo \
    libpng \
    cairo \
    pango \
    openssl \
    libtool \
    && pacman -Scc --noconfirm

RUN curl -fsSL -o /tmp/guacamole-server.tar.gz \
        "https://archive.apache.org/dist/guacamole/${GUACAMOLE_VERSION}/source/guacamole-server-${GUACAMOLE_VERSION}.tar.gz" \
    && tar xzf /tmp/guacamole-server.tar.gz -C /tmp \
    && cd "/tmp/guacamole-server-${GUACAMOLE_VERSION}" \
    && ./configure --prefix=/usr --sbindir=/usr/bin \
        --with-ssh --with-terminal --with-webp \
        --without-vnc --without-telnet --without-rdp \
        --without-pulse --without-websockets --disable-kubernetes \
        CFLAGS="-Wno-error" CPPFLAGS="-Wno-error" \
    && make -j"$(nproc)" \
    && make install \
    && rm -rf "/tmp/guacamole-server-${GUACAMOLE_VERSION}" /tmp/guacamole-server.tar.gz

RUN curl -fsSL -o /tmp/tomcat.tar.gz \
        "https://archive.apache.org/dist/tomcat/tomcat-9/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz" \
    && mkdir -p /opt/tomcat \
    && tar xzf /tmp/tomcat.tar.gz -C /opt/tomcat --strip-components=1 \
    && rm -f /tmp/tomcat.tar.gz \
    && rm -rf /opt/tomcat/webapps/*

RUN curl -fsSL -o /opt/tomcat/webapps/guacamole.war \
        "https://archive.apache.org/dist/guacamole/${GUACAMOLE_VERSION}/binary/guacamole-${GUACAMOLE_VERSION}.war" \
    && mkdir -p /etc/guacamole/extensions \
    && curl -fsSL -o /tmp/auth-json.tar.gz \
        "https://archive.apache.org/dist/guacamole/${GUACAMOLE_VERSION}/binary/guacamole-auth-json-${GUACAMOLE_VERSION}.tar.gz" \
    && tar xzf /tmp/auth-json.tar.gz -C /tmp \
    && cp "/tmp/guacamole-auth-json-${GUACAMOLE_VERSION}/guacamole-auth-json-${GUACAMOLE_VERSION}.jar" /etc/guacamole/extensions/ \
    && rm -rf /tmp/auth-json.tar.gz "/tmp/guacamole-auth-json-${GUACAMOLE_VERSION}"

COPY scripts/guacamole.properties /etc/guacamole/guacamole.properties
COPY scripts/guacamole-sshd.conf /etc/ssh/sshd_config.d/guac.conf
COPY scripts/guacamole-launch.sh /usr/local/bin/guacamole-launch
RUN chmod +x /usr/local/bin/guacamole-launch \
    && mkdir -p /run/sshd \
    && ssh-keygen -A \
    && usermod --password "$(openssl passwd -6 ucs)" ucs \
    && chown -R ucs:ucs /opt/tomcat /etc/guacamole

ENV GUACAMOLE_HOME=/etc/guacamole
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk
ENV CATALINA_HOME=/opt/tomcat

# .NET SDK builds the XTerm.NET Avalonia host below
RUN --mount=type=cache,target=/var/cache/pacman/pkg \
    pacman -S --noconfirm --needed \
    dotnet-sdk \
    && pacman -Scc --noconfirm

# XTerm.NET is a headless emulator library; the terminal window ucs-detect drives
# is the Example desktop app from its Avalonia host, Iciclecreek.Avalonia.Terminal.
# Its window opens maximized; 680x520 keeps it near 80x24 like the other terminals.
RUN --mount=type=cache,target=/home/ucs/.nuget/packages,uid=1000,gid=1000 \
    mkdir -p /opt/xtermnet /home/ucs/.nuget && \
    chown ucs:ucs /opt/xtermnet /home/ucs/.nuget && \
    sudo -u ucs env HOME=/home/ucs git clone \
        https://github.com/tomlm/Iciclecreek.Avalonia.Terminal.git /home/ucs/iciclecreek && \
    sudo -u ucs env HOME=/home/ucs git -C /home/ucs/iciclecreek checkout \
        bbee5ed1f80cf00388749523d3389e5f30c41a1b && \
    sudo -u ucs sed -i 's/WindowState="Maximized"/Width="680" Height="520"/' \
        /home/ucs/iciclecreek/src/Example/MainWindow.axaml && \
    sudo -u ucs sed -i 's|FontSize="14" BufferSize="1000"|FontFamily="Unifont,Unifont Upper" FontSize="16" BufferSize="1000"|' \
        /home/ucs/iciclecreek/src/Example/MainWindow.axaml && \
    sudo -u ucs env HOME=/home/ucs DOTNET_CLI_HOME=/home/ucs \
        NUGET_PACKAGES=/home/ucs/.nuget/packages \
        dotnet publish /home/ucs/iciclecreek/src/Example/Example.csproj \
        -c Release -o /opt/xtermnet && \
    rm -rf /home/ucs/iciclecreek

# GNU Unifont 18.0.01 (Unicode 18.0) for consistent terminal font rendering.
# Both files are needed: unifont is the BMP, unifont_upper carries planes 1-3 and emoji.
# Noto Color Emoji, installed above, is what kitty, Ghostty, foot, WezTerm, Konsole, Contour and
# the VTE terminals select for emoji presentation cells; install-fonts.py aliases the "emoji"
# family to it in the fontconfig file the tests use.
COPY ucs_detect/fonts.py /tmp/install-fonts.py
RUN python /tmp/install-fonts.py --install --dest /usr/share/fonts/unifont \
    --fontconfig /etc/fonts/conf.d/99-ucs-unifont.conf

# python dependencies for ucs-detect
RUN --mount=type=cache,target=/var/cache/pacman/pkg \
    pacman -S --noconfirm --needed \
    python-yaml \
    python-blessed \
    python-pillow \
    python-prettytable \
    python-requests \
    python-psutil \
    python-matplotlib \
    && pacman -Scc --noconfirm

# create working directory mounted from host
WORKDIR /app

# install ucs-detect in editable mode
COPY README.rst pyproject.toml setup.cfg ./
COPY ucs_detect/ ./ucs_detect/
RUN pip install -e .  --break-system-package

# entrypoint: start Xvfb if DISPLAY is set, then exec command
ENV LIBGL_ALWAYS_SOFTWARE=1

# Weston fades its output to black after five minutes without input.  A terminal staged under it
# receives no pointer or keyboard events, so its later pages would be captured black.
RUN mkdir -p /etc/xdg/weston && printf '[core]\nidle-time=0\n' > /etc/xdg/weston/weston.ini

COPY docker-entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/bin/bash"]
