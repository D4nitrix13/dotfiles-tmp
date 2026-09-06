<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***¿Qué es Qtile?***

> [!NOTE]
> **Qtile** *es un gestor de ventanas de mosaico (tiling window manager) altamente configurable y escrito en Python. Los gestores de ventanas de mosaico organizan automáticamente las ventanas en la pantalla sin superposición, maximizando el uso del espacio y la eficiencia del trabajo.*

---

## ***Características principales de Qtile***

1. **Mosaico (Tiling):** *Las ventanas se organizan automáticamente en mosaico.*
2. **Altamente Configurable:** *La configuración se realiza mediante un fichero de configuración en Python, lo que permite una personalización profunda y flexible.*
3. **Extensible:** *Se pueden escribir extensiones y widgets personalizados en Python.*
4. **Ligero:** *Es un gestor de ventanas ligero, adecuado para sistemas con recursos limitados.*
5. **Soporte para múltiples layouts:** *Incluye varios layouts predeterminados y la posibilidad de crear otros nuevos.*

---

### ***Código de configuración de Qtile***

- **El código proporcionado es un ejemplo de configuración de Qtile. A continuación, se desglosan los componentes principales del fichero de configuración:**

---

### ***Importación de módulos y configuraciones básicas***

```python
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"  # La tecla Mod es la tecla Super (generalmente la tecla Windows)
terminal = guess_terminal()  # Intenta adivinar el terminal predeterminado
```

---

#### ***Definición de teclas***

**Se definen varias combinaciones de teclas para controlar las ventanas y el gestor de ventanas:**

```python
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Mover ventanas
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Redimensionar ventanas
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]
```

#### ***Definición de grupos de trabajo***

```python
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
    ])
```

---

#### ***Layouts***

**Definición de layouts disponibles para organizar las ventanas:**

```python
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
]
```

#### ***Widgets y barras***

**Configuración de la barra de estado y widgets:**

```python
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
                widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff")}, name_transform=lambda name: name.upper()),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press <M-r> to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]
```

---

#### ***Mouse y configuraciones adicionales***

**Configuración de eventos del mouse y otras opciones:**

```python
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),
    Match(wm_class="makebranch"),
    Match(wm_class="maketag"),
    Match(wm_class="ssh-askpass"),
    Match(title="branchdialog"),
    Match(title="pinentry"),
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"
```
