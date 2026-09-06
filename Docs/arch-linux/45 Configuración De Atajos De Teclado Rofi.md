<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de Atajos de Teclado***

```bash
sudo pacman -Syu rofi --noconfirm
```

**A continuación se muestra cómo añadir atajos de teclado para abrir el menú y para la navegación entre ventanas utilizando `rofi`:**

```python
# ------------ App Configs ------------
# Menu
Key([mod], "m", lazy.spawn("rofi -show drun")),

# Window Nav
Key([mod, "shift"], "m", lazy.spawn("rofi -show window")),
```

**Tu fichero de configuracion se veria:**

```python
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me 

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # ------------ App Configs ------------
    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show window")),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
```

- **`Key([mod], "m", ...)`:** *Define un atajo de teclado con la tecla `Mod` (tecla de modificación, como `Mod1` o `Mod4`) más la tecla `m`.*
- **`lazy.spawn("rofi -show drun")`:** *Al presionar la combinación de teclas, se ejecuta el comando `rofi -show drun`, que muestra un menú de aplicaciones disponibles.*

- ***Rofi** es una aplicación liviana y altamente configurable utilizada principalmente como un lanzador de aplicaciones y un selector de ventanas en sistemas operativos basados en Linux. Rofi se ha convertido en una herramienta popular entre los usuarios de entornos de escritorio minimalistas y administradores de ventanas flotantes o en mosaico (tiling window managers) debido a su flexibilidad y eficiencia.*

---

## ***Características de Rofi***

1. **Lanzador de Aplicaciones:** *Permite buscar y ejecutar aplicaciones rápidamente.*
2. **Selector de Ventanas:** *Ofrece la capacidad de cambiar entre ventanas abiertas de manera eficiente.*
3. **Selector de Ejecutables:** *Puede ser utilizado para ejecutar comandos específicos directamente.*
4. **Selector de SSH:** *Facilita la conexión a servidores SSH desde una interfaz gráfica.*
5. **Personalización y Temas:** *Altamente personalizable con temas y configuraciones visuales para adaptarse a las preferencias del usuario.*
6. **Compatibilidad:** *Funciona bien con una variedad de administradores de ventanas y entornos de escritorio.*
7. **Extensible:** *Soporta la creación de scripts personalizados para ampliar sus funcionalidades.*

---

### ***Instalación de Rofi***

**Para instalar Rofi en Arch Linux, puedes usar el gestor de paquetes `pacman`:**

```bash
sudo pacman -Syu rofi
```

---

### ***Uso Básico de Rofi***

**Una vez instalado, puedes ejecutar Rofi utilizando el siguiente comando:**

```bash
rofi -show drun
```

- *Este comando abre Rofi en modo lanzador de aplicaciones, mostrando las aplicaciones disponibles.*

---

### ***Modos de Rofi***

**Rofi tiene varios modos que puedes utilizar según tus necesidades:**

1. **drun:** *Modo lanzador de aplicaciones.*

   ```bash
   rofi -show drun
   ```

2. **run:** *Modo para ejecutar comandos.*

   ```bash
   rofi -show run
   ```

3. **window:** *Modo selector de ventanas.*

   ```bash
   rofi -show window
   ```

4. **ssh:** *Modo para conexiones SSH.*

   ```bash
   rofi -show ssh
   ```

### ***Configuración de Rofi***

*Rofi es altamente configurable mediante ficheros de configuración. El fichero de configuración principal suele encontrarse en `~/.config/rofi/config.rasi`.*

---

#### ***Ejemplo de Configuración Default (`config.rasi`)***

```bash
@theme "/usr/share/rofi/themes/android_notification.rasi"
```

- **Default Config Theme**

```bash
/*******************************************************************************
 * ROFI Color theme
 * User: Rasi
 * Copyright: Rasmus Steinke
 *******************************************************************************/

* {
    selected-normal-foreground:  rgba ( 255, 255, 255, 100 % );
    foreground:                  rgba ( 193, 193, 193, 100 % );
    normal-foreground:           @foreground;
    alternate-normal-background: rgba ( 39, 50, 56, 100 % );
    red:                         rgba ( 220, 50, 47, 100 % );
    selected-urgent-foreground:  rgba ( 255, 24, 68, 100 % );
    blue:                        rgba ( 38, 139, 210, 100 % );
    urgent-foreground:           rgba ( 255, 24, 68, 100 % );
    alternate-urgent-background: rgba ( 39, 50, 56, 100 % );
    active-foreground:           rgba ( 128, 203, 196, 100 % );
    lightbg:                     rgba ( 238, 232, 213, 100 % );
    selected-active-foreground:  rgba ( 128, 203, 196, 100 % );
    alternate-active-background: rgba ( 39, 50, 56, 100 % );
    background:                  rgba ( 39, 50, 56, 100 % );
    bordercolor:                 rgba ( 39, 50, 56, 100 % );
    alternate-normal-foreground: @foreground;
    normal-background:           rgba ( 39, 50, 56, 100 % );
    lightfg:                     rgba ( 88, 104, 117, 100 % );
    selected-normal-background:  rgba ( 57, 66, 73, 100 % );
    border-color:                @foreground;
    spacing:                     2;
    separatorcolor:              rgba ( 30, 37, 41, 100 % );
    urgent-background:           rgba ( 39, 50, 56, 100 % );
    selected-urgent-background:  rgba ( 57, 66, 73, 100 % );
    alternate-urgent-foreground: @urgent-foreground;
    background-color:            rgba ( 0, 0, 0, 0 % );
    alternate-active-foreground: @active-foreground;
    active-background:           rgba ( 39, 50, 56, 100 % );
    selected-active-background:  rgba ( 57, 66, 73, 100 % );
}
window {
    background-color: @background;
    border:           1;
    padding:          5;
}
mainbox {
    border:  0;
    padding: 0;
}
message {
    border:       1px dash 0px 0px ;
    border-color: @separatorcolor;
    padding:      1px ;
}
textbox {
    text-color: @foreground;
}
listview {
    fixed-height: 0;
    border:       2px dash 0px 0px ;
    border-color: @separatorcolor;
    spacing:      2px ;
    scrollbar:    true;
    padding:      2px 0px 0px ;
}
element {
    border:  0;
    padding: 1px ;
}
element-text {
    background-color: inherit;
    text-color:       inherit;
}
element.normal.normal {
    background-color: @normal-background;
    text-color:       @normal-foreground;
}
element.normal.urgent {
    background-color: @urgent-background;
    text-color:       @urgent-foreground;
}
element.normal.active {
    background-color: @active-background;
    text-color:       @active-foreground;
}
element.selected.normal {
    background-color: @selected-normal-background;
    text-color:       @selected-normal-foreground;
}
element.selected.urgent {
    background-color: @selected-urgent-background;
    text-color:       @selected-urgent-foreground;
}
element.selected.active {
    background-color: @selected-active-background;
    text-color:       @selected-active-foreground;
}
element.alternate.normal {
    background-color: @alternate-normal-background;
    text-color:       @alternate-normal-foreground;
}
element.alternate.urgent {
    background-color: @alternate-urgent-background;
    text-color:       @alternate-urgent-foreground;
}
element.alternate.active {
    background-color: @alternate-active-background;
    text-color:       @alternate-active-foreground;
}
scrollbar {
    width:        4px ;
    border:       0;
    handle-width: 8px ;
    padding:      0;
}
mode-switcher {
    border:       2px dash 0px 0px ;
    border-color: @separatorcolor;
}
button.selected {
    background-color: @selected-normal-background;
    text-color:       @selected-normal-foreground;
}
inputbar {
    spacing:    0;
    text-color: @normal-foreground;
    padding:    1px ;
}
case-indicator {
    spacing:    0;
    text-color: @normal-foreground;
}
entry {
    spacing:    0;
    text-color: @normal-foreground;
}
prompt {
    spacing:    0;
    text-color: @normal-foreground;
}
inputbar {
    children:   [ prompt,textbox-prompt-colon,entry,case-indicator ];
}
textbox-prompt-colon {
    expand:     false;
    str:        ":";
    margin:     0px 0.3em 0em 0em ;
    text-color: @normal-foreground;
}
```

---

#### ***Configuración Theme (`~/.config/rofi/config.rasi`)***

```bash
@theme "/usr/share/rofi/themes/Arc-Dark.rasi"
```

---

### ***Personalización de Temas***

- *Puedes personalizar la apariencia de Rofi utilizando temas. Hay muchos temas disponibles en línea, y puedes crear los tuyos propios.*

**Para aplicar un tema, usa el siguiente comando:**

```bash
rofi -show drun -theme <Path-Theme>
```

---

### ***Conclusión***

- *Rofi es una herramienta poderosa y flexible que mejora la eficiencia en el manejo de aplicaciones y ventanas en entornos de escritorio de Linux. Su capacidad de personalización y su variedad de modos lo hacen adecuado para una amplia gama de usos, desde un simple lanzador de aplicaciones hasta un selector de ventanas avanzado o una herramienta de conexión SSH.*
