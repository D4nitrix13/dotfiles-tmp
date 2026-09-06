sudo pacman -Rns pulseaudio pulseaudio-alsa pulseaudio-jack

sudo pacman -S pipewire pipewire-alsa pipewire-pulse pipewire-jack wireplumber qpwgraph

systemctl --user enable --now pipewire pipewire-pulse wireplumber
