# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# GitLab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

tput civis

if status is-interactive
    # Commands to run in interactive sessions can go here
end

if test (uname) = Darwin
    # macOS
    set BREW_BIN /opt/homebrew/bin/brew
else
    # Linux
    set BREW_BIN /home/linuxbrew/.linuxbrew/bin/brew
end

eval ($BREW_BIN shellenv)

# if not set -q TMUX
#     tmux
# end

# if not set -q ZELLIJ 
#  zellij
# end

starship init fish | source
zoxide init fish | source
atuin init fish | source

# set -gx PROJECT_PATHS ~/dir1 ~/dir2 ~/dir3

set -x PATH $HOME/.cargo/bin $PATH
set -x PATH $HOME/.config/composer/vendor/bin $PATH

set -Ux CARAPACE_BRIDGES 'zsh,fish,bash,inshellisense'
mkdir -p ~/.config/fish/completions
carapace --list | awk '{print $1}' | xargs -I{} touch ~/.config/fish/completions/{}.fish
carapace _carapace | source

set -x LS_COLORS "di=38;5;67:ow=48;5;60:ex=38;5;132:ln=38;5;144:*.tar=38;5;180:*.zip=38;5;180:*.jpg=38;5;175:*.png=38;5;175:*.mp3=38;5;175:*.wav=38;5;175:*.txt=38;5;223:*.sh=38;5;132"
set -g fish_greeting ""

## alias
set os_type (uname)
if test $os_type = 'Linux'
    alias ls='ls --color=auto'
end

set -e os_type

alias fzfbat='fzf --preview="bat --theme=gruvbox-dark --color=always {}"'
alias fzfnvim='nvim (fzf --preview="bat --theme=gruvbox-dark --color=always {}")'
alias _tmux_='tmux attach-session -d -t "Session "'

alias resetcursor="echo -ne '\e[5 q'"

resetcursor

tput cnorm

## everforest
# set -l foreground d3c6aa
# set -l selection 2d4f67
# set -l comment 859289
# set -l red e67e80
# set -l orange ff9e64
# set -l yellow dbbc7f
# set -l green a7c080
# set -l purple d699b6
# set -l cyan 7fbbb3
# set -l pink d699b6

# kanagawa dragon colors
set -l foreground C5C9C5 # dragonWhite - un blanco suave para texto principal
set -l selection 2D4F67 # waveBlue2 - azul oscuro para selección
set -l comment 7A8382 # dragonGray3 - gris para comentarios
set -l red C4746E # dragonRed - rojo suave
set -l orange B98D7B # dragonOrange2 - naranja suave
set -l yellow C4B28A # dragonYellow - amarillo cálido
set -l green 87A987 # dragonGreen - verde pastel
set -l purple 957FB8 # oniViolet - púrpura suave
set -l cyan 8EA4A2 # dragonAqua - verde azulado
set -l pink D27E99 # sakuraPink - rosa suave

# Syntax Highlighting Colors
set -g fish_color_normal $foreground
set -g fish_color_command $cyan
set -g fish_color_keyword $pink
set -g fish_color_quote $yellow
set -g fish_color_redirection $foreground
set -g fish_color_end $orange
set -g fish_color_error $red
set -g fish_color_param $purple
set -g fish_color_comment $comment
set -g fish_color_selection --background=$selection
set -g fish_color_search_match --background=$selection
set -g fish_color_operator $green
set -g fish_color_escape $pink
set -g fish_color_autosuggestion $comment

# Completion Pager Colors
set -g fish_pager_color_progress $comment
set -g fish_pager_color_prefix $cyan
set -g fish_pager_color_completion $foreground
set -g fish_pager_color_description $comment

set -gx PATH $HOME/.luaenv/bin $PATH
eval "$(luaenv init -)"

# Created by `pipx` on 2024-11-15 01:32:47
set PATH $PATH /home/d4nitrix13/.local/bin

source ~/.phpbrew/phpbrew.fish

# Load pyenv automatically by appending
# the following to
# ~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
# and ~/.bashrc (for interactive shells) :

set -x PYENV_ROOT $HOME/.pyenv

if test -d $PYENV_ROOT/bin
    set -x PATH $PYENV_ROOT/bin $PATH
end

status is-interactive; and source (pyenv init - | psub)

# Pyenv (Docs)
# set -Ux PYENV_ROOT $HOME/.pyenv
# fish_add_path $PYENV_ROOT/bin
# pyenv init - fish | source

# Eliminate Repeated Routes
set -x PATH (echo $PATH | tr ' ' '\n' | sort -u)

# clear -T xterm-256color && /home/linuxbrew/.linuxbrew/bin/tmux clear-history || clear -T xterm-256color || clear
