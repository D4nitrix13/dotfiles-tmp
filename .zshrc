# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# GitLab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Linuxbrew
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"

# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Composer Path
export PATH=$HOME/.config/composer/vendor/bin:$PATH

# Rustup
export PATH="$PATH:$HOME/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin"

# Luaenv
export PATH="$HOME/.luaenv/bin:$PATH"
eval "$(luaenv init -)"

# Path to your Oh My Zsh installation.
export ZSH="/home/d4nitrix13/.oh-my-zsh"

# Colors ls
export LS_COLORS="di=38;5;67:ow=48;5;60:ex=38;5;132:ln=38;5;144:*.tar=38;5;180:*.zip=38;5;180:*.jpg=38;5;175:*.png=38;5;175:*.mp3=38;5;175:*.wav=38;5;175:*.txt=38;5;223:*.sh=38;5;132"
if [[ "$(uname)" == "Linux" ]]; then
  alias ls='ls --color=auto'
else
  alias ls='gls --color=auto'
fi

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="powerlevel10k/powerlevel10k" 
#"robbyrussell"
#"heapbytes"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
# plugins=(git)
plugins=(
  copypath
  copyfile
  copybuffer
  command-not-found
  web-search
  git                         # Funciones y alias para git
  docker                      # Comandos útiles para Docker
  docker-compose              # Comandos útiles para Docker Compose
  ubuntu                      # Funciones y alias para ubuntu
  rust                        # Funciones y alias para rust
  # zsh-syntax-highlighting    # Resaltado de sintaxis
  fast-syntax-highlighting    # Resaltado de sintaxis rápido
  zsh-autocomplete            # Autocompletado avanzado
  zsh-autosuggestions         # Sugerencias de comandos
  zoxide                      # Navegación rápida por directorios
  pip                         # Atajos para manejar paquetes de Python
  pyenv                       # Soporte para Pyenv
  poetry                      # Soporte para Poetry (gestión de dependencias en Python)
  composer                    # Comandos para Composer (gestión de dependencias PHP)
  nvm                         # Node Version Manager
  kubectl                     # Alias para Kubernetes
  fzf                         # Comandos para usar `fzf` (selector de línea de comandos)
  zsh-completions
)

autoload -U compinit; compinit
fpath+=~/.oh-my-zsh/custom/plugins/zsh-completions/src
# rm -f ~/.zcompdump*; compinit

eval "$(zoxide init zsh)"
source $ZSH/oh-my-zsh.sh
source "$HOME/.sdkman/bin/sdkman-init.sh"

HISTSIZE=10000           # Número de comandos que se mantienen en la memoria
SAVEHIST=10000           # Número de comandos que se guardan en el archivo de historial
HISTFILE=~/.zsh_history  # Archivo de historial (por defecto es ~/.zsh_history)

setopt append_history    # Añade los nuevos comandos al final del historial, en vez de sobrescribirlos
setopt hist_ignore_dups  # No guarda comandos duplicados consecutivos
setopt hist_ignore_space # No guarda comandos que comienzan con un espacio
setopt share_history     # Comparte el historial entre todas las sesiones de Zsh abiertas

# User configuration
export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='nvim'
fi

# Compilation flags
export ARCHFLAGS="-arch $(uname -m)"

# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
alias _tmux_='tmux attach-session -d -t "Session "'
alias _zellij_="zellij --session 'Session '"

alias resetcursor="echo -ne '\e[5 q'"

resetcursor

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - zsh)"

# Eliminate Repeated Routes
export PATH="$(echo $PATH | tr ':' '\n' | sort -u | tr '\n' ':')"
