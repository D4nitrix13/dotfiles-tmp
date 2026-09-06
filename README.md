# Dotfiles

> Configuración personal de escritorio y shell para **CachyOS** sobre **Omarchy** (Hyprland).
> Reproducible, modular, organizado por ámbito funcional, versionado por gestor de paquetes.

[![Arch](https://img.shields.io/badge/Arch-CachyOS-1793D1?logo=arch-linux&logoColor=white)](#)
[![Hyprland](https://img.shields.io/badge/WM-Hyprland-58E1FF?logo=hyprland&logoColor=black)](#)
[![Omarchy](https://img.shields.io/badge/Distro-Omarchy-DB3B79)](#)
[![Neovim](https://img.shields.io/badge/Editor-Neovim-57A143?logo=neovim&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](#)

---

## Tabla de contenidos

- [Descripción general](#descripción-general)
- [Stack tecnológico](#stack-tecnológico)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Bootstrap en una máquina nueva](#bootstrap-en-una-máquina-nueva)
- [Configuraciones destacadas](#configuraciones-destacadas)
- [Mantenimiento](#mantenimiento)
- [Comandos útiles](#comandos-útiles)
- [Créditos y referencias](#créditos-y-referencias)

---

## Descripción general

Este repositorio versiona el directorio `\$HOME` completo de un escritorio
**CachyOS + Omarchy + Hyprland**. La idea es tener un setup reproducible en
cualquier máquina con una instalación fresca del SO base, versionando:

- Configuraciones de usuario (`~/.config/`, `~/Scripts/`, `~/Utils/`, `~/Docs/`).
- Manifiestos de paquetes por gestor (`pacman`, `yay`, `pipx`, `npm`, `cargo`, `flatpak`).
- Scripts de utilidad y binarios personalizados en `~/.local/bin/`.

El modelo de commits sigue **Conventional Commits** en español y está
dividido en **unidades de trabajo revisables**: cada commit es una categoría
funcional autocontenida (`feat(hyprland)`, `feat(omarchy)`, `feat(shell-fish)`,
etc.).

---

## Stack tecnológico

### Sistema base

| Componente | Versión / Detalle |
|---|---|
| Distribución | CachyOS (Arch Linux optimizado) |
| Init | systemd + UWSM |
| Boot | GRUB con LUKS opcional |
| Login | hyprland via `.xsession` |

### Escritorio (Hyprland stack)

| Componente | Rol |
|---|---|
| **Hyprland** | Compositor Wayland + WM tiling principal |
| **Omarchy** | Capa de opinionated defaults (DHH) — temas, hooks, branding |
| **Waybar** | Barra de estado superior |
| **Walker** | Lanzador de aplicaciones (default Omarchy) |
| **Elephant** | Provider de menús contextuales para Walker |
| **Mako** | Daemon de notificaciones |
| **SwayOSD** | OSD de volumen, brillo y caps lock |

### Shells

| Shell | Uso |
|---|---|
| **Fish** | Shell interactivo por defecto (Fisher + plugins) |
| **Zsh** | Alternativa con Powerlevel10k + Zoxide |
| **Bash** | POSIX base, scripts |
| **Nushell** | Shell estructurado para data exploration |

### Terminales (multi-config)

| Emulador | Notas |
|---|---|
| **Ghostty** | Default Omarchy, GPU-accelerated |
| **Alacritty** | Alternativa ligera |
| **Kitty** | GPU, rico en features |
| **Foot** | Nativo Wayland puro |
| **Wezterm** | Lua-config, multiplexer embebido |

### Multiplexers

- **Zellij** (default moderno, con UI descubrible)
- **Tmux** (fallback para servidores remotos)

### Editor

- **Neovim** con **LazyVim** + plugins custom:
  - `blink.cmp`, `flash.nvim`, `fzf-lua`, `harpoon2`
  - LSP via `mason`
  - AI assistants: `copilot.lua`, `claudecode.nvim`, `gemini-cli.nvim`, `codegraph.nvim`

### Herramientas de shell

- **Starship** — prompt rápido multi-shell
- **Carapace** — completion engine multi-shell
- **Atuin** — historial de shell mejorado (no versionado)

### AI & Coding assistants

- **OpenCode** — agente AI CLI principal, con workflow SDD:
  - Agentes `sdd-*` para el ciclo Spec-Driven Development
  - Agentes `jd-*` para judgment-day adversarial review
  - Reviewers `review-*` (riesgo, legibilidad, confiabilidad, resiliencia)
- MCP servers: **context7** (docs), **engram** (memoria persistente), **codegraph** (índice del repo)

### DEs legacy mantenidos

Aunque el flujo activo es Hyprland, se conservan configuraciones (sin paquetes
instalados) para sesiones X11 alternativas:

- BSPWM, Qtile, Openbox, Spectrwm, XMonad
- Polybar, Tint2, XMobar
- Sxhkd, Picom
- Rofi, Dunst

---

## Estructura del repositorio

```
$HOME/
├── .config/                    # Configuraciones de aplicaciones
│   ├── hypr/                   # Compositor Hyprland
│   ├── omarchy/                # Capa Omarchy (temas, hooks, branding)
│   ├── waybar/                 # Barra de estado
│   ├── walker/, elephant/      # Lanzadores
│   ├── mako/, swayosd/         # Notificaciones y OSD
│   ├── fish/                   # Shell Fish
│   ├── zsh -> (no tracked)     # Zsh usa archivos en raíz
│   ├── nushell/                # Shell Nushell
│   ├── carapace/, starship.toml
│   ├── zellij/, tmux/          # Multiplexers
│   ├── nvim/                   # Neovim + LazyVim
│   ├── alacritty/, foot/, ghostty/, kitty/, wezterm/  # Terminales
│   ├── bspwm/, qtile/, openbox/, spectrwm/, xmonad/   # DEs legacy
│   ├── polybar/, tint2/, xmobar/                     # Bars legacy
│   ├── sxhkd/, picom/                               # Auxiliares legacy
│   ├── rofi/, dunst/                                 # Lanzadores/notif legacy
│   ├── ranger/, xfce4/                               # File managers
│   ├── bpytop/, htop/, fastfetch/, neofetch/         # Monitor sistema
│   ├── lazygit/, lazydocker/, ptpython/, pgcli/      # Dev tools
│   ├── opencode/                # AI workflow (SDD)
│   ├── wiremix/, pavucontrol.ini                     # Audio
│   ├── flameshot/              # Capturas de pantalla
│   ├── calcurse/, imv/          # Utilidades
│   ├── composer/               # PHP Composer
│   └── .gitignore              # Exclusiones internas
│
├── .bashrc, .bash_profile, .bash_logout, .profile
├── .zshenv, .zprofile, .zshrc, .p10k.zsh, .zoxide.nu
├── .xsession, .XCompose, .dmrc, gnome.desktop
├── .gitconfig, .gitignore
├── .nanorc, .npmrc, .python-version
├── .vimrc, .vim/               # Vim legacy
├── .theme/                     # Selector de temas
├── .screenlayout/              # Scripts arandr
├── .local/bin/                 # Scripts propios (binarios versionados)
├── Scripts/                    # Utilitarios bash (referenciados por Hyprland)
├── Utils/                      # GRUB, LightDM, desktop themes
├── Docs/                       # Notas, cheatsheets, prompts
├── packages/                   # Manifiestos de paquetes
│   ├── pacman/installed.txt
│   ├── yay/installed.txt
│   ├── pipx/installed.txt
│   ├── npm/installed.txt
│   ├── cargo/installed.txt
│   └── flatpak/installed.txt
├── .sdirs                      # Marcadores de directorios
├── .psqlrc                     # psql pager off
└── .odbcinst.ini               # Driver ODBC mdbtools
```

---

## Bootstrap en una máquina nueva

Este repo **no se instala** como un paquete: se asume que el repo vive en
`\$HOME` (es un dotfiles-as-folder-repo). El flujo es:

### 1. Instalar CachyOS

Desde el ISO oficial con particionado BTRFS + Snapper.

### 2. (Opcional) Instalar Omarchy

```bash
# Seguir https://omarchy.org o usar omarchy-on-cachyos
```

### 3. Clonar el repo

```bash
cd ~ && git clone git@github.com:D4nitrix13/Dotfiles.git .git
# O si tenés contenido previo:
cd ~ && git init && git remote add origin git@github.com:D4nitrix13/Dotfiles.git && git pull
```

### 4. Reinstalar paquetes

```bash
# Paquetes oficiales
sudo pacman -S --needed - < packages/pacman/installed.txt

# Paquetes AUR (requiere yay instalado)
yay -S --needed - < packages/yay/installed.txt

# Pipx tools (si usás)
pipx install < packages/pipx/installed.txt

# NPM globals (si usás)
xargs npm install -g < packages/npm/installed.txt
```

### 5. Aplicar temas / reiniciar Hyprland

```bash
# Recargar Hyprland
hyprctl reload

# Reiniciar waybar
pkill waybar && waybar &
```

---

## Configuraciones destacadas

### Hyprland

- Webapp binds para Obsidian, MiniMax, YouTube y WhatsApp (`SUPER + SHIFT + O/A/Y/ALT+G`)
- Workspaces 6-9 con focus y move explícitos
- `SUPER + GRAVE` para scratchpad
- `SUPER + S` / `SUPER + SHIFT + S` para screenshots (wayland)
- `SUPER + CTRL + R` para reload Hyprland + Waybar

### Neovim

- LazyVim base + extras (LSP, Dap, Format, Testing)
- Plugins custom: blink.cmp, flash.nvim, fzf-lua, harpoon2
- AI: copilot.lua, claudecode.nvim, gemini-cli.nvim, codegraph.nvim
- Lazy lock fijo para reproducibilidad (`lazy-lock.json`)

### OpenCode + SDD

- Agentes `sdd-{explore,propose,spec,design,tasks,apply,verify,archive}`
- Reviewers `review-{risk,readability,reliability,resilience}`
- MCP servers: context7, engram, codegraph
- Permisos granulares por herramienta y tipo de operación

### Shells

- **Fish**: config.fish modular, funciones helper (pj, nvm, tmux auto-attach)
- **Zsh**: Powerlevel10k con segmentos custom (git, k8s, dotnet)
- **Nushell**: bridge a entorno Bash via `bash-env.nu`

---

## Mantenimiento

### Regenerar manifiestos de paquetes

```bash
# Paquetes oficiales explícitos
pacman -Qqen > packages/pacman/installed.txt

# Paquetes AUR explícitos
pacman -Qqem > packages/yay/installed.txt

# Pipx
pipx list --short | awk '{print $1}' > packages/pipx/installed.txt

# NPM globals
npm list -g --depth=0 --parseable | xargs -n1 basename > packages/npm/installed.txt
```

### Auditoría del repo

```bash
# Ver qué se trackea
git ls-files | wc -l

# Tamaño por categoría
git ls-files .config/ | awk -F/ '{print $2}' | sort | uniq -c | sort -rn
```

### Actualizar LazyVim plugins

```bash
nvim --headless "+Lazy update" +qa
git add .config/nvim/lazy-lock.json
git commit -m "chore(nvim): actualizar plugins via Lazy update"
```

---

## Comandos útiles

```bash
# Ver el log de commits categorizado
git log --oneline | head -20

# Buscar archivos por categoría
git ls-files | grep -E "^\\.config/hypr/"

# Backup rápido antes de cambios grandes
git stash --include-untracked

# Ver diferencias de dotfiles sin commitear
git diff --stat
```

---

## Créditos y referencias

- [**Omarchy**](https://omarchy.org) — el sistema de DHH que sustenta el escritorio.
- [**Hyprland**](https://hyprland.org) — compositor Wayland de referencia.
- [**LazyVim**](https://lazyvim.org) — distribución Neovim base.
- [**Starship**](https://starship.rs) — prompt.
- [**OpenCode**](https://opencode.ai) — agente AI CLI.
- [**Atuin**](https://atuin.sh) — historial de shell.
- [**Carapace**](https://carapace.sh) — completion engine.

Inspirado por los dotfiles de la comunidad Arch/CachyOS y por las prácticas
de configuración declarativa del ecosistema NixOS/Homemanager.

---

## Licencia

Este repositorio se distribuye bajo la licencia **MIT**. Ver `LICENSE`
para más detalles.

```
MIT License

Copyright (c) 2025 D4nitrix13

Se concede permiso, sin cargo alguno, a cualquier persona que obtenga una
copia de este software y archivos de documentación asociados...
```