mkdir -p $HOME/Notes/templates

echo "Instalando Oh my bash";

git clone https://github.com/ohmybash/oh-my-bash.git $HOME/.oh-my-bash --depth=1 --verbose
# upgrade_oh_my_bash

echo "Instalando Oh my zsh";

git clone https://github.com/ohmyzsh/ohmyzsh.git $HOME/.oh-my-zsh --depth=1 --verbose

# echo "Instalando plugins oh my zsh";
# * Se instalan con brew
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions --depth=1 --verbose
git clone https://github.com/marlonrichert/zsh-autocomplete.git ~/.oh-my-zsh/custom/plugins/zsh-autocomplete --depth=1 --verbose
git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions --depth=1 --verbose
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/fast-syntax-highlighting --depth=1 --verbose

echo "Powerlevel10k";

git clone --depth=1 --verbose https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k

echo "Instalando scrub";

yay -Syu --noconfirm scrub;

echo "Instalando Net Tools";

sudo pacman -Syu --noconfirm net-tools


echo "Instalando kitty";

# Ubuntu: Link https://linux.how2shout.com/how-to-install-kitty-terminal-on-ubuntu-22-04-or-20-04/
# Arch: https://wiki.archlinux.org/title/Kitty
sudo pacman -Syu --noconfirm kitty


echo "Instalando openssh";
sudo pacman -Syu --noconfirm openssh
sudo systemctl start sshd
sudo systemctl enable sshd


echo "Instalando homebrew";

sudo curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
# . $HOME/.cargo/env
rustup default stable

echo "Instalando homebrew";

NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)";

mkdir -p $HOME/.cache/starship
mkdir -p $HOME/.cache/carapace
mkdir -p $HOME/.local/share/atuin
mkdir -p $HOME/Notes/templates

echo "install wezterm"
sudo pacman -Syu --noconfirm wezterm

echo "install mesa-utils iw para tmux"
pacman -Syu mesa-utils iw

brew install nushell carapace zoxide atuin jq starship fish zsh-autosuggestions zsh-syntax-highlighting zsh-autocomplete powerlevel10k tmux zsh

echo "instalando ineutils: hostanme"
sudo pacman -Syu --noconfirm inetutils


# https://github.com/x-motemen/ghq
# brew install fastfetch
brew install ghq onefetch neofetch eza

sudo pacman -Syu --noconfirm gnupg

sudo pacman -Syu --noconfirm cmake base-devel pciutils vulkan-headers vulkan-tools wayland wayland-protocols libxrandr xcb-util dconf

echo "instalando zellij"
cargo install zellij

yay -Syu --noconfirm git-delta cpufetch

sudo pacman -Syu --noconfirm wmctrl bash xorg-xprop xorg-xwininfo xclip xorg-xrandr

echo "instalando ramfetch"
cd $HOME/utils/
sudo install -Dm755 ramfetch /usr/local/bin/ramfetch


echo "instalando homebrew"

curl -L -O https://github.com/phpbrew/phpbrew/releases/latest/download/phpbrew.phar
chmod +x phpbrew.phar
sudo mv phpbrew.phar /usr/local/bin/phpbrew

sudo mkdir -p /opt/phpbrew
sudo chown -R $USER:$USER /opt/phpbrew
echo "Y" | sudo env "PATH=$PATH" phpbrew lookup-prefix homebrew

phpbrew init --root=/opt/phpbrew

echo "instaling package brew"

brew install fzf fd ripgrep lazygit fnm pipx lazydocker luarocks lua

echo "instaling package bpytop"

sudo pacman -Syu --noconfirm bpytop

echo "install sdkman tool de java jdk (Java Development Kit), "
curl -s "https://get.sdkman.io" | bash

echo "instalando docker"

sudo pacman -Syu --noconfirm docker docker-compose

# sudo groupadd docker # ! Dara error groupadd: el grupo «docker» ya existe

sudo usermod -aG docker $USER
newgrp docker

sudo systemctl start docker.service
sudo systemctl enable docker.service
docker run hello-world

echo "instal luaenv"
git clone https://github.com/cehoffman/luaenv.git $HOME/.luaenv --depth=1 --verbose

echo "install zoxide obsidian"

yay -Syu --noconfirm zoxide obsidian


echo "install python dependencnies"
pipx install mypy ptpython pipenv

echo "install server"
sudo npm i -g serve

echo "install configurate ptpython"

mkdir -p ~/.config/ptpython/

echo "install tokei"

cargo install tokei
cargo install mdcat

echo "create directory starship"

mkdir -pv ~/.cache/starship ~/.cache/carapace ~/.local/share/atuin


starship init nu > ~/.cache/starship/init.nu
zoxide init nushell > ~/.zoxide.nu
atuin init nu > ~/.local/share/atuin/init.nu
carapace _carapace nushell > ~/.cache/carapace/init.nu

sudo pacman -Syu --noconfirm libffi openssl zlib pyenv

# https://stackoverflow.com/questions/40175669/when-typing-ls-command-i-get-zsh-command-not-found-gls


yay -Syu ttf-jetbrains-mono-nerd --noconfirm
yay -Syu ttf-hack-nerd --noconfirm

# copiar el tema personalizado
cp -r ~/utils/powerbash13k/ ~/.oh-my-bash/themes


sudo ln -sf ~/.config/nvim/ /root/.config/nvim
sudo ln -sf ~/.local/share/nvim/ /root/.local/share/
sudo ln -sf ~/.local/state/nvim/ /root/.local/state/
sudo ln -sf ~/.cache/nvim/ /root/.cache/

sudo ln -sf ~/.config/alacritty /root/.config/
sudo ln -sf ~/.config/atuin /root/.config/
sudo ln -sf ~/.config/dconf /root/.config/
sudo ln -sf ~/.config/gtk-3.0 /root/.config/
sudo ln -sf ~/.config/libreoffice /root/.config/
sudo ln -sf ~/.config/procps /root/.config/
sudo ln -sf ~/.config/systemd /root/.config/
sudo ln -sf ~/.config/bash-env-json /root/.config/
sudo ln -sf ~/.config/dunst /root/.config/
sudo ln -sf ~/.config/htop /root/.config/
sudo ln -sf ~/.config/neofetch /root/.config/
sudo ln -sf ~/.config/ptpython /root/.config/
sudo ln -sf ~/.config/Thunar /root/.config/
sudo ln -sf ~/.config/xfce4 /root/.config/
sudo ln -sf ~/.config/bash-env.nu /root/.config/
sudo ln -sf ~/.config/fastfetch /root/.config/
sudo ln -sf ~/.config/keepassxc /root/.config/
sudo ln -sf ~/.config/nushell /root/.config/
sudo ln -sf ~/.config/pulse /root/.config/
sudo ln -sf ~/.config/tmux /root/.config/
sudo ln -sf ~/.config/yay /root/.config/
sudo ln -sf ~/.config/bpytop /root/.config/
sudo ln -sf ~/.config/fish /root/.config/
sudo ln -sf ~/.config/kitty /root/.config/
sudo ln -sf ~/.config/nvim /root/.config/
sudo ln -sf ~/.config/qtile /root/.config/
sudo ln -sf ~/.config/udiskie /root/.config/
sudo ln -sf ~/.config/zellij /root/.config/
sudo ln -sf ~/.config/carapace /root/.config/
sudo ln -sf ~/.config/GIMP /root/.config/
sudo ln -sf ~/.config/lazydocker /root/.config/
sudo ln -sf ~/.config/pavucontrol.ini /root/.config/
sudo ln -sf ~/.config/rofi /root/.config/
sudo ln -sf ~/.config/vlc /root/.config/


sudo ln -sf ~/.bash_history /root/.bash_history
sudo ln -sf ~/.bash_history-00870.tmp /root/.bash_history-00870.tmp
sudo ln -sf ~/.bash_history-01253.tmp /root/.bash_history-01253.tmp
sudo ln -sf ~/.bash_history-01402.tmp /root/.bash_history-01402.tmp
sudo ln -sf ~/.bash_logout /root/.bash_logout
sudo ln -sf ~/.bash_profile /root/.bash_profile
sudo ln -sf ~/.bashrc /root/.bashrc
sudo ln -sf ~/Contraseñas.kdbx /root/Contraseñas.kdbx
sudo ln -sf ~/.dmrc /root/.dmrc
sudo ln -sf ~/.fehbg /root/.fehbg
sudo ln -sf ~/.gitconfig /root/.gitconfig
sudo ln -sf ~/.gtkrc-2.0 /root/.gtkrc-2.0
sudo ln -sf ~/.gtkrc-2.0.mine /root/.gtkrc-2.0.mine
sudo ln -sf ~/.lesshst /root/.lesshst
sudo ln -sf ~/.osh-update /root/.osh-update
sudo ln -sf ~/.p10k.zsh /root/.p10k.zsh
sudo ln -sf ~/.profile /root/.profile
sudo ln -sf ~/.python_history /root/.python_history
sudo ln -sf ~/renameFile.sh /root/renameFile.sh
sudo ln -sf ~/rofi_log.txt /root/rofi_log.txt
sudo ln -sf ~/.sdirs /root/.sdirs
sudo ln -sf ~/.wget-hsts /root/.wget-hsts
sudo ln -sf ~/.Xauthority /root/.Xauthority
sudo ln -sf ~/.Xresources /root/.Xresources
sudo ln -sf ~/.xsession /root/.xsession
sudo ln -sf ~/.xsession-errors /root/.xsession-errors
sudo ln -sf ~/.xsession-errors.old /root/.xsession-errors.old
sudo ln -sf ~/.zcompdump /root/.zcompdump
sudo ln -sf ~/.zcompdump-asus-5.9 /root/.zcompdump-asus-5.9
sudo ln -sf ~/.zcompdump-asus-5.9.zwc /root/.zcompdump-asus-5.9.zwc
sudo ln -sf ~/.zoxide.nu /root/.zoxide.nu
sudo ln -sf ~/.zshenv /root/.zshenv
sudo ln -sf ~/.zsh_history /root/.zsh_history
sudo ln -sf ~/.zshrc /root/.zshrc

sudo ln -sf ~/.cargo/ /root/

sudo ln -sf ~/.sdkman /root/
sudo ln -sf ~/.luaenv /root/

sudo ln -sf ~/.tmux /root/
sudo ln -sf ~/.cache/zellij /root/.cache/zellij 

sudo ln -sf ~/.config/starship.toml /root/.config/ 
sudo ln -sf ~/.config/volumeicon /root/.config

#pendiente
#pipx install pycrypy
