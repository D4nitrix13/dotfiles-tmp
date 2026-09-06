<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Atajos de teclado definidos en la configuración***

**A continuación se explican los atajos de teclado definidos en la configuración de Qtile y su propósito:**

```python
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Mover el foco a la izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover el foco a la derecha"),
    Key([mod], "j", lazy.layout.down(), desc="Mover el foco hacia abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover el foco hacia arriba"),
    Key([mod], "w", lazy.window.kill(), desc="Cerrar la ventana enfocada"),
    Key([mod], "space", lazy.layout.next(), desc="Mover el foco a la siguiente ventana"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Mover la ventana a la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Mover la ventana a la derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Mover la ventana hacia abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Mover la ventana hacia arriba"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Aumentar la ventana hacia la izquierda"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Aumentar la ventana hacia la derecha"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Aumentar la ventana hacia abajo"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Aumentar la ventana hacia arriba"),
    Key([mod], "n", lazy.layout.normalize(), desc="Restablecer el tamaño de todas las ventanas"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Alternar entre lados divididos y no divididos del stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Abrir terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Alternar entre layouts"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reiniciar Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Cerrar Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Abrir el prompt para ejecutar comandos"),
]
```

---

## ***Explicación de cada atajo***

- **`mod + h`:** *Mover el foco a la ventana de la izquierda.*
- **`mod + j`:** *Mover el foco a la ventana de abajo.*
- **`mod + k`:** *Mover el foco a la ventana de arriba.*
- **`mod + l`:** *Mover el foco a la ventana de la derecha.*
- **`mod + w`:** *Cerrar la ventana enfocada.*
- **`mod + space`:** *Mover el foco a la siguiente ventana.*
- **`mod + shift + h`:** *Mover la ventana enfocada a la izquierda.*
- **`mod + shift + j`:** *Mover la ventana enfocada hacia abajo.*
- **`mod + shift + k`:** *Mover la ventana enfocada hacia arriba.*
- **`mod + shift + l`:** *Mover la ventana enfocada a la derecha.*
- **`mod + control + h`:** *Aumentar la ventana hacia la izquierda.*
- **`mod + control + j`:** *Aumentar la ventana hacia abajo.*
- **`mod + control + k`:** *Aumentar la ventana hacia arriba.*
- **`mod + control + l`:** *Aumentar la ventana hacia la derecha.*
- **`mod + n`:** *Restablecer el tamaño de todas las ventanas al tamaño predeterminado.*
- **`mod + shift + Return`:** *Alternar entre lados divididos y no divididos del stack.*
- **`mod + Return`:** *Abrir un terminal.*
- **`mod + Tab`:** *Alternar entre layouts.*
- **`mod + control + r`:** *Reiniciar Qtile.*
- **`mod + control + q`:** *Cerrar Qtile (Cerrar Session).*
- **`mod + r`:** *Abrir el prompt para ejecutar comandos.*
