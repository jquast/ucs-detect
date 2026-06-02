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
    weston \
    fontconfig \
    xorg-fonts-misc \
    && pacman -Scc --noconfirm

# unifont for consistent terminal font rendering
# (not in Arch official repos, only AUR; download OTF directly from GNU)
RUN mkdir -p /usr/share/fonts/OTF && \
    curl -L -o /usr/share/fonts/OTF/unifont.otf \
    "https://unifoundry.com/pub/unifont/unifont-16.0.02/font-builds/unifont-16.0.02.otf" && \
    fc-cache -fv

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
    bobcat-terminal \
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

# python dependencies for ucs-detect
RUN --mount=type=cache,target=/var/cache/pacman/pkg \
    pacman -S --noconfirm --needed \
    python-yaml \
    python-blessed \
    python-pillow \
    python-prettytable \
    python-requests \
    python-wcwidth \
    python-psutil \
    python-matplotlib \
    && pacman -Scc --noconfirm

# create working directory mounted from host
WORKDIR /app

# install ucs-detect in editable mode
COPY README.rst pyproject.toml setup.cfg ./
COPY ucs_detect/ ./ucs_detect/
RUN pip install -e . --break-system-packages

# entrypoint: start Xvfb if DISPLAY is set, then exec command
ENV LIBGL_ALWAYS_SOFTWARE=1
COPY docker-entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/bin/bash"]
