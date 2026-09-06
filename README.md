# Dotfiles

> Configuración personal de escritorio y shell para **CachyOS** sobre **Omarchy** (Hyprland).
> Reproducible, modular, organizado por ámbito funcional, versionado por gestor de paquetes.

[![Arch](https://img.shields.io/badge/Arch-CachyOS-1793D1?logo=arch-linux&logoColor=white)](https://cachyos.org)
[![Hyprland](https://img.shields.io/badge/WM-Hyprland-58E1FF?logo=hyprland&logoColor=black)](https://hyprland.org)
[![Omarchy](https://img.shields.io/badge/Distro-Omarchy-DB3B79)](https://omarchy.org)
[![Neovim](https://img.shields.io/badge/Editor-Neovim-57A143?logo=neovim&logoColor=white)](https://neovim.io)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

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

Este repositorio versiona el directorio `$HOME` completo de un escritorio
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

| Componente   | Versión / Detalle               |
| ------------ | ------------------------------- |
| Distribución | CachyOS (Arch Linux optimizado) |
| Init         | systemd + UWSM                  |
| Boot         | GRUB con LUKS opcional          |
| Login        | hyprland via `.xsession`        |

### Escritorio (Hyprland stack)

| Componente   | Rol                                                         |
| ------------ | ----------------------------------------------------------- |
| **Hyprland** | Compositor Wayland + WM tiling principal                    |
| **Omarchy**  | Capa de opinionated defaults (DHH) — temas, hooks, branding |
| **Waybar**   | Barra de estado superior                                    |
| **Walker**   | Lanzador de aplicaciones (default Omarchy)                  |
| **Elephant** | Provider de menús contextuales para Walker                  |
| **Mako**     | Daemon de notificaciones                                    |
| **SwayOSD**  | OSD de volumen, brillo y caps lock                          |

### Shells

| Shell       | Uso                                              |
| ----------- | ------------------------------------------------ |
| **Fish**    | Shell interactivo por defecto (Fisher + plugins) |
| **Zsh**     | Alternativa con Powerlevel10k + Zoxide           |
| **Bash**    | POSIX base, scripts                              |
| **Nushell** | Shell estructurado para data exploration         |

### Terminales (multi-config)

| Emulador      | Notas                            |
| ------------- | -------------------------------- |
| **Ghostty**   | Default Omarchy, GPU-accelerated |
| **Alacritty** | Alternativa ligera               |
| **Kitty**     | GPU, rico en features            |
| **Foot**      | Nativo Wayland puro              |
| **Wezterm**   | Lua-config, multiplexer embebido |

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

```text
$HOME/
├── .config/
│   ├── hypr/
│   ├── omarchy/
│   ├── waybar/
│   ├── walker/
│   ├── elephant/
│   ├── mako/
│   ├── swayosd/
│   ├── fish/
│   ├── nushell/
│   ├── carapace/
│   ├── starship.toml
│   ├── zellij/
│   ├── tmux/
│   ├── nvim/
│   ├── alacritty/
│   ├── foot/
│   ├── ghostty/
│   ├── kitty/
│   ├── wezterm/
│   ├── bspwm/
│   ├── qtile/
│   ├── openbox/
│   ├── spectrwm/
│   ├── xmonad/
│   ├── polybar/
│   ├── tint2/
│   ├── xmobar/
│   ├── sxhkd/
│   ├── picom/
│   ├── rofi/
│   ├── dunst/
│   ├── ranger/
│   ├── xfce4/
│   ├── bpytop/
│   ├── htop/
│   ├── fastfetch/
│   ├── neofetch/
│   ├── lazygit/
│   ├── lazydocker/
│   ├── ptpython/
│   ├── pgcli/
│   ├── opencode/
│   ├── wiremix/
│   ├── pavucontrol.ini
│   ├── flameshot/
│   ├── calcurse/
│   ├── imv/
│   ├── composer/
│   ├── hyprland-preview-share-picker/
│   ├── haders
│   ├── qt5ct/
│   ├── qt6ct/
│   ├── bash-env-json
│   ├── bash-env.nu
│   ├── user-dirs.dirs
│   ├── user-dirs.locale
│   ├── mimeapps.list
│   ├── xdg-terminals.list
│   ├── gnome-xdg-terminals.list
│   ├── .gitignore
│   └── .gsd-keyboard.settings-ported
│
├── .bashrc
├── .bash_profile
├── .bash_logout
├── .profile
├── .zshenv
├── .zprofile
├── .zshrc
├── .p10k.zsh
├── .zoxide.nu
├── .xsession
├── .XCompose
├── .dmrc
├── gnome.desktop
├── .gitconfig
├── .gitignore
├── .nanorc
├── .npmrc
├── .python-version
├── .vimrc
├── .vim/
├── .theme/
├── .screenlayout/
├── .local/bin/
├── Scripts/
├── Utils/
├── Docs/
├── packages/
│   ├── pacman/installed.txt
│   ├── yay/installed.txt
│   ├── pipx/installed.txt
│   ├── npm/installed.txt
│   ├── cargo/installed.txt
│   └── flatpak/installed.txt
├── .sdirs
├── .psqlrc
└── .odbcinst.ini
```

### Notas sobre archivos sueltos

| Archivo / Directorio | Propósito |
|---|---|
| `.gitignore` (raíz) | Exclusiones globales: navegadores, IA, caches, historiales, secretos |
| `.gitconfig` | Identidad del autor + helpers de difftool/Neovim |
| `.xsession` | Arranque sesión X11, paths, ejecución Hyprland via UWSM |
| `.XCompose` | Combinaciones de teclas para caracteres acentuados y símbolos |
| `.dmrc` | Sesión predeterminada del display manager |
| `gnome.desktop` | Entrada `.desktop` legacy de GNOME |
| `.zshrc` y familia | Configuración Zsh con Powerlevel10k + Zoxide |
| `.bashrc` y familia | Configuración Bash POSIX |
| `.vimrc`, `.vim/` | Vim legacy como fallback de Neovim |
| `.theme/` | Selector y catálogo de temas del sistema |
| `.screenlayout/` | Scripts `arandr` para layouts de monitores |
| `.local/bin/` | Binarios propios (4 scripts: percentage, battery, brightness, volume) |
| `.nanorc` | Ajustes del editor Nano |
| `.npmrc` | Defaults globales de npm |
| `.python-version` | Versión de Python fijada por pyenv |
| `Scripts/` | Scripts bash para Hyprland/sxhkd (screenshot, portScan, lock, etc.) |
| `Utils/` | Recursos opcionales (GRUB, LightDM, desktop themes) |
| `Docs/` | Notas, cheatsheets, prompts reutilizables |
| `packages/` | Manifiestos de paquetes por gestor |
| `.sdirs` | Marcadores de directorios para shells |
| `.psqlrc` | Desactiva pager de `psql` para output directo |
| `.odbcinst.ini` | Registra driver ODBC de mdbtools |
| `packages/pacman/installed.txt` | Paquetes oficiales explícitos (458) |
| `packages/yay/installed.txt` | Paquetes AUR explícitos (14) |

### Notas sobre subdirectorios clave

| Directorio | Propósito |
|---|---|
| `.config/hypr/` | Compositor Hyprland (bindings, monitors, idle, lock) |
| `.config/omarchy/` | Capa Omarchy: temas activos, hooks, branding |
| `.config/waybar/` | Barra de estado superior |
| `.config/walker/`, `elephant/` | Lanzador + provider de menús |
| `.config/mako/`, `swayosd/` | Notificaciones y OSD de volumen/brillo |
| `.config/fish/` | Shell Fish (config, conf.d, functions, themes) |
| `.config/nushell/` | Shell Nushell (config, env, history, bash-env bridge) |
| `.config/zellij/`, `tmux/` | Multiplexers de terminal |
| `.config/nvim/` | Neovim con LazyVim y plugins custom |
| `.config/{alacritty,foot,ghostty,kitty,wezterm}/` | Emuladores de terminal (multi-config) |
| `.config/{bspwm,qtile,openbox,spectrwm,xmonad}/` | DEs legacy X11 (sin paquetes instalados) |
| `.config/{polybar,tint2,xmobar}/` | Status bars legacy |
| `.config/{sxhkd,picom}/` | Auxiliares legacy de WMs X11 |
| `.config/{rofi,dunst}/` | Lanzador y notificador legacy |
| `.config/{ranger,xfce4}/` | Gestores de archivos |
| `.config/{bpytop,htop,fastfetch,neofetch}/` | Monitorización del sistema |
| `.config/{lazygit,lazydocker,ptpython,pgcli}/` | Herramientas de desarrollo (TUI/CLI) |
| `.config/opencode/` | OpenCode AI: agentes SDD, MCP servers |
| `.config/{wiremix,pavucontrol.ini}` | Audio (PipeWire/Pulse) |
| `.config/flameshot/` | Captura de pantalla |
| `.config/{calcurse,imv}/` | Utilidades (calendario, visor imágenes) |
| `.config/composer/` | PHP Composer |
| `.config/qt5ct/`, `qt6ct/` | Configuración de estilo Qt (Kvantum) |

---

## Bootstrap en una máquina nueva

Este repo **no se instala** como un paquete: se asume que el repo vive en
`$HOME` (es un dotfiles-as-folder-repo). El flujo es:

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

### Configuración de shells

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

- [**Omarchy**](https://omarchy.org "Omarchy — sistema operativo de DHH (37signals). Distribución opinionated sobre Arch Linux con Hyprland, configs prearmadas y temas sincronizados. https://omarchy.org") — el sistema de DHH que sustenta el escritorio.
- [**Hyprland**](https://hyprland.org "Hyprland — compositor Wayland dinámico para Linux con animaciones, bordes redondeados, gestos y Tiling. Escrito en C++/wlroots. https://hyprland.org") — compositor Wayland de referencia.
- [**LazyVim**](https://lazyvim.org "LazyVim — distribución Neovim basada en lazy.nvim. Incluye LSP, Treesitter, autopairs, formatting, completion. Configurable via lua/ y plugins lazy extras. https://lazyvim.org") — distribución Neovim base.
- [**Starship**](https://starship.rs "Starship — prompt de shell cross-platform escrito en Rust. Configurable via starship.toml con segmentos para git, kubernetes, node, python, docker. https://starship.rs") — prompt.
- [**OpenCode**](https://opencode.ai "OpenCode — agente AI CLI open source con soporte para múltiples providers (Anthropic, OpenAI, Google, Bedrock). Workflow SDD nativo con agentes sdd-*. https://opencode.ai") — agente AI CLI.
- [**Atuin**](https://atuin.sh "Atuin — reemplazo del historial de shell con búsqueda full-text, sincronización opcional cifrada end-to-end y TUI. Soporta fish, zsh, bash, nushell. https://atuin.sh") — historial de shell.
- [**Carapace**](https://carapace.sh "Carapace — completion engine multi-shell (Bash, Fish, Zsh, Nushell, Oil, elvish, powershell) escrito en Go. Genera completions consistentes desde spec files declarativos. https://carapace.sh") — completion engine.
- [**Neovim**](https://neovim.io "Neovim — fork hiperextensible de Vim. LSP nativo, Treesitter, Lua como lenguaje de configuración first-class. https://neovim.io") — editor.
- [**Ghostty**](https://ghostty.org "Ghostty — emulador de terminal con aceleración GPU escrito por Mitchell Hashimoto (HashiCorp). Multiplataforma, rápido, y respeta los estándares. https://ghostty.org") — terminal default Omarchy.
- [**Btop**](https://github.com/aristocratos/btop "Btop — monitor de recursos TUI estilo bashtop. CPU, memoria, red, discos y procesos en una interfaz colorida y configurable. https://github.com/aristocratos/btop") — monitor del sistema.
- [**CachyOS**](https://cachyos.org "CachyOS — distribución Arch Linux optimizada con kernel BBR, BORE scheduler, perfiles CPU optimizados por arquitectura. Default para este setup. https://cachyos.org") — distribución base.

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
