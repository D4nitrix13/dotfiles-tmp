<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Solución a Ventanas Emergentes de VSCode que se Muestran Muy Grandes**

## **1. Identificar La Clase/Título Real De La Ventana**

*Necesitas identificar con precisión el `wm_class` y `title` de esa ventana emergente para agregarla correctamente a tus `float_rules`.*

## **Usa `xprop`**

**Instálalo si no lo tienes:**

```bash
sudo pacman -Syu --noconfirm --needed xorg-xprop
```

*Luego, ejecuta `xprop` en una terminal y **haz clic sobre la ventana problemática** (la de VSCode que se muestra muy grande).*

**Busca Estas Líneas En La Salida:**

- *`WM_CLASS(STRING) = "..."` → este es el `wm_class`*
- *`WM_NAME(STRING) = "..."` → este es el `title`*

```bash
xprop
```

**Luego Selecciona La Ventana Problemática (La De Vscode Que Se Muestra Muy Grande).**

**Ejemplo de salida:**

```bash
_NET_FRAME_EXTENTS(CARDINAL) = 1, 1, 1, 1
_NET_WM_DESKTOP(CARDINAL) = 1
WM_STATE(WM_STATE):
  window state: Normal
  icon window: 0x0
_NET_WM_STATE(ATOM) = _NET_WM_STATE_MODAL, _NET_WM_STATE_SKIP_TASKBAR, _NET_WM_STATE_ABOVE
WM_HINTS(WM_HINTS):
  Client accepts input or input focus: True
  Initial state is Normal State.
  window id # of group leader: 0x1800001
_GTK_THEME_VARIANT(UTF8_STRING) =
WM_TRANSIENT_FOR(WINDOW): window id # 0x1600004
XdndAware(ATOM) = BITMAP
_NET_WM_OPAQUE_REGION(CARDINAL) = 0, 0, 504, 124
_NET_WM_WINDOW_TYPE(ATOM) = _NET_WM_WINDOW_TYPE_DIALOG
_NET_WM_SYNC_REQUEST_COUNTER(CARDINAL) = 25165935, 25165936
_NET_WM_USER_TIME(CARDINAL) = 524461
_NET_WM_USER_TIME_WINDOW(WINDOW): window id # 0x180006e
WM_CLIENT_LEADER(WINDOW): window id # 0x1800001
_NET_WM_PID(CARDINAL) = 1696
WM_LOCALE_NAME(STRING) = "C.UTF-8"
WM_CLIENT_MACHINE(STRING) = "asus"
WM_NORMAL_HINTS(WM_SIZE_HINTS):
  program specified minimum size: 504 by 124
  program specified maximum size: 504 by 124
  program specified base size: 0 by 0
  window gravity: NorthWest
WM_PROTOCOLS(ATOM): protocols  WM_DELETE_WINDOW, WM_TAKE_FOCUS, _NET_WM_PING, _NET_WM_SYNC_REQUEST
WM_CLASS(STRING) = "code", "Code"
WM_ICON_NAME(STRING) = "Visual Studio Code"
_NET_WM_ICON_NAME(UTF8_STRING) = "Visual Studio Code"
WM_NAME(STRING) = "Visual Studio Code"
_NET_WM_NAME(UTF8_STRING) = "Visual Studio Code"
```

---

### **2. Agrega el Match correcto**

*Usa los valores obtenidos en tu `floating_layout`. Ejemplo:*

```python
Match(wm_class="Code", wm_type="dialog")
```

---

### **4. Herramientas Adicionales**

**Si `xprop` no muestra suficiente info, puedes usar:**

#### **`xwininfo`**

```bash
xwininfo
```

*Seleccionas la ventana y te muestra geometría, nombre y más.*

**Ejemplo de salida:**

```bash
xwininfo

xwininfo: Please select the window about which you
          would like information by clicking the
          mouse in that window.

xwininfo: Window id: 0x18001e1 "Visual Studio Code"

  Absolute upper-left X:  210
  Absolute upper-left Y:  477
  Relative upper-left X:  210
  Relative upper-left Y:  477
  Width: 542
  Height: 124
  Depth: 24
  Visual: 0x2b
  Visual Class: TrueColor
  Border width: 1
  Class: InputOutput
  Colormap: 0x1800006 (not installed)
  Bit Gravity State: NorthWestGravity
  Window Gravity State: NorthWestGravity
  Backing Store State: NotUseful
  Save Under State: no
  Map State: IsViewable
  Override Redirect State: no
  Corners:  +210+477  -1166+477  -1166-477  +210-477
  -geometry 542x124+210+477
```

#### **`wmctrl`**

```bash
sudo pacman -Syu --noconfirm --needed wmctrl
```

```bash
wmctrl -lx
```

```bash
0x0140002d  0 Navigator.firefox     asus Mozilla Firefox
0x02600003  1 Alacritty.Alacritty   asus d4nitrix13@asus:~
```

*Esto Muestra Todas Las Ventanas Activas Con `Wm_Class` Y `Title` (Útil Si La Ventana Desaparece Rápido).*
