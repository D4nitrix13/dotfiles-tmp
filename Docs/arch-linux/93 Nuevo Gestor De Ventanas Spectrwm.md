<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Nuevo Gestor De Ventanas Spectrwm**

---

## **1. Instalación De Spectrwm Con `Yay`**

```bash
yay -Syu --noconfirm spectrwm
```

* **`yay`**
  **Es un *AUR helper* (gestor de paquetes de Arch User Repository). Permite instalar tanto paquetes oficiales de Arch como paquetes de la comunidad (AUR). Internamente combina `pacman` y procesos de compilación.**

* **`-Syu`**
  **Es una combinación de tres subcomandos de `pacman` (el gestor oficial de paquetes de Arch):**

  * **`-S` (*sync*): sincroniza e instala el/los paquete(s) que especifiques.**
  * **`-y` (*refresh*): fuerza la actualización de la base de datos local de paquetes remotos.**
  * **`-u` (*upgrade*): actualiza todos los paquetes instalados que tengan versión nueva disponible.**

  *Juntos (`-Syu`) hacen una **actualización completa del sistema** y luego instalan `spectrwm`.*

* **`--noconfirm`**
  **Indica que no te pida confirmación para ninguna pregunta durante la instalación (todas las “sí/no” responden “sí” automáticamente). Útil para scripts o para evitar pulsar “y” manualmente.**

* **`spectrwm`**
  **Nombre del paquete que contiene el gestor de ventanas “spectrwm”. Al final de la instalación, tendrás configurados los binarios y archivos de configuración por defecto en tu sistema.**

---

## **2. Sesiones Disponibles En `/Usr/Share/Xsessions/`**

```bash
lsd /usr/share/xsessions/
 qtile.desktop   spectrwm.desktop
```

* **`lsd`**
  *Es un reemplazo de `ls` con iconos y colores más vistosos. Funciona igual que `ls`, pero muestra iconos Unicode y coloreado inteligente.*

* **`/usr/share/xsessions/`**
  *Carpeta estándar donde los gestores de sesión (display managers, ej. LightDM, GDM) buscan archivos `.desktop` para ofrecerte distintos entornos de escritorio o gestores de ventanas al iniciar sesión.*

* **Salida**

  * *`qtile.desktop` → sesión de Qtile (otro tiling WM).*
  * *`spectrwm.desktop` → sesión de Spectrwm.*

  *Estos archivos `.desktop` contienen metadatos (nombre, comando para lanzar el WM, ícono) que utiliza el display manager.*

---

## **3. Consultar La Documentación De Spectrwm**

```bash
man spectrwm
```

* **`man`**
  Muestra la página de manual del programa que indiques (aquí, `spectrwm`).
* **Secciones principales**

  1. **NOMBRE**
  2. **SINOPSIS:** *sintaxis de llamada al comando y opciones.*
  3. **DESCRIPCIÓN:** *qué hace y cómo configurarlo.*
  4. **OPCIONES:** *lista de flags (`-x`, `-h`, etc.) y qué valores aceptan.*
  5. **ARCHIVOS:** *ubicación de archivos de configuración (\~/.spectrwm.conf).*
  6. **VER TAMBIÉN:** *referencias relacionadas.*

---

## **4. Repositorio Oficial**

> [https://github.com/conformal/spectrwm](https://github.com/conformal/spectrwm)

* **Repositorio GitHub**
  Contiene el código fuente, ejemplos de configuración y el historial de cambios (commits).
* **Clonar**

  ```bash
  git clone https://github.com/conformal/spectrwm.git
  ```

* Aquí puedes ver issues, proponer mejoras o reportar errores.

---

## **5. Instalación De Dependencias**

```bash
sudo pacman -Syu --noconfirm xlockmore trayer upower pamixer dmenu xterm
```

* **`sudo`**
  Ejecuta el siguiente comando con privilegios de superusuario (root), necesarios para modificar el sistema (instalar paquetes).

* **`pacman -Syu`**
  Igual que antes: refresca bases de datos y actualiza el sistema.

* **`--noconfirm`**
  Mismo comportamiento: no solicita confirmación.

* **Paquetes a instalar**:

  * **`xlockmore`:** *bloqueador de pantalla (screen locker).*
  * **`trayer`:** *bandeja de sistema ligera (system tray) para mostrar iconos de estado.*
  * **`upower`:** *demonio de gestión de energía y batería.*
  * **`pamixer`:** *interfaz de línea de comandos para controlar volumen PulseAudio (subcomando `pamixer --sink …`).*
  * **`dmenu`:** *menú dinámico para lanzar aplicaciones (se integra bien con WMs ligeros).*
  * **`xterm`:** *emulador de terminal básico para X11.*

---

### **¿Por Qué Estas Dependencias?**

* **Interacción básica:** *`dmenu` te permite lanzar apps con atajos de teclado.*
* **Tray & estado:** *`trayer` y `upower` para monitorizar batería y otros íconos.*
* **Audio:** *`pamixer` para subir/bajar volumen sin una interfaz gráfica.*
* **Seguridad:** *`xlockmore` para bloquear la pantalla cuando no estás.*
* **Terminal:** *`xterm` como terminal ligero por defecto.*

**Con esto tienes el desglose de cada comando, cada opción y el propósito de los paquetes involucrados. Si necesitas profundizar en alguna opción concreta (por ejemplo, qué otras flags admite `pacman` o `spectrwm`) puedes consultar:**

```bash
man pacman
man spectrwm
```

---

### **Config Spectrwm**

---

## **1. Opciones Globales**

**Estas opciones controlan el comportamiento general de los espacios de trabajo, enfoque y posicionamiento de nuevas ventanas.**

| *Directiva*          | *Qué hace*                                                                           | *Valores posibles*                              | *Ejemplo*                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| *`workspace_limit`*  | *Número máximo de workspaces que creará spectrwm.*                                   | *Entero ≥ 1*                                    | *`workspace_limit = 6` → Tendrás cinco workspaces numerados 1…6.*                                                                              |
| *`focus_mode`*       | *Modo de enfoque de ventanas.*                                                       | *`default`, `sloppy`, `semi-sloppy`*            | *`focus_mode = default` → sólo enfoca la ventana que hagas clic o con atajo.*                                                                  |
| *`focus_close`*      | *A dónde vuelve el foco cuando cierras una ventana.*                                 | *`previous`, `left`, `right`, `north`, `south`* | *`focus_close = previous` → regresa al último stack o ventana usada.*                                                                          |
| *`focus_close_wrap`* | *Si al cerrar en un stack vacío, salta al otro extremo (wrap-around).*               | *`0` (off), `1` (on)*                           | *`focus_close_wrap = 1` → cerrar la última ventana de un stack lleva al primero.*                                                              |
| *`focus_default`*    | *Regla para seleccionar ventana al cambiar a otro workspace.*                        | *`first`, `last`, `smart`, `default`*           | *`focus_default = last` → al cambiar de workspace, enfoca la última ventana usada ahí.*                                                        |
| *`spawn_position`*   | *Dónde colocar nuevas ventanas dentro del layout.*                                   | *`first`, `last`, `next`, `smart`*              | *`spawn_position = next` → la nueva ventana va a la siguiente posición relativa al foco.*                                                      |
| *`workspace_clamp`*  | *Impide moverte más allá de los workspaces definidos (clamp).*                       | *`0` (off), `1` (on)*                           | *`workspace_clamp = 0` → puedes usar atajos para ir a ws7 aunque no exista y spectrwm los creará dinámicamente (siempre ≤ `workspace_limit`).* |
| *`warp_focus`*       | *Mueve el cursor del ratón al centro de la ventana enfocada automáticamente.*        | *`0` (off), `1` (on)*                           | *`warp_focus = 1` → útil si usas muchos atajos, para no mover manualmente el puntero.*                                                         |
| *`warp_pointer`*     | *Igual que `warp_focus`, pero más “agresivo”: salta siempre al borde de la ventana.* | *`0` (off), `1` (on)*                           | *`warp_pointer = 1`*                                                                                                                           |

---

## **2. Decoración de Ventanas**

**Controlan bordes, colores y separación de ventanas tileadas.**

| **Directiva**               | **Qué hace**                                                                     | **Valores posibles**                           | **Ejemplo**                                                                        |
| --------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- |
| *`border_width`*            | *Grosor (en píxeles) del borde de cada ventana.*                                 | *Entero ≥ 0*                                   | *`border_width = 1` → borde de 1 px.*                                              |
| *`color_focus`*             | *Color del borde de la ventana enfocada.*                                        | *`rgb:RR/GG/BB` (hex en bloques de 2 dígitos)* | *`color_focus = rgb:50/50/50` → gris medio.*                                       |
| *`color_focus_maximized`*   | *Color de borde para ventanas maximizadas y enfocadas.*                          | *Igual que anterior*                           | *`color_focus_maximized = rgb:0f/10/1a` → tono oscuro azulado.*                    |
| *`color_unfocus`*           | *Color de borde de ventanas sin foco.*                                           | *Igual*                                        | *`color_unfocus = rgb:0f/10/1a`.*                                                  |
| *`color_unfocus_maximized`* | *Borde de ventana maximizadas sin foco.*                                         | *Igual*                                        | *`color_unfocus_maximized = rgb:0f/10/1a`.*                                        |
| *`region_padding`*          | *Espacio (en píxeles) entre el área tileada y el borde externo del monitor.*     | *Entero ≥ 0*                                   | *`region_padding = 4` → 4 px alrededor de todo el layout.*                         |
| *`tile_gap`*                | *Gap (en píxeles) entre ventanas dentro del layout tile.*                        | *Entero ≥ 0*                                   | *`tile_gap = 4` → 4 px entre ventanas.*                                            |
| *`disable_border`*          | *Elimina bordes si la barra está oculta y sólo hay una ventana en el workspace.* | *`0` (off), `1` (on)*                          | *`disable_border = 1` → más limpio cuando sólo hay un cliente y no quieres marco.* |

---

## **3. Configuración de la Barra**

**Controla la visibilidad, colores, fuentes, formato y comportamiento de la barra de estado.**

| *Directiva*                                                                  | *Qué hace*                                                                                              | *Valores posibles / Notas*                                                                                 |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| *`bar_enabled`*                                                              | *Mostrar (`1`) u ocultar (`0`) la barra.*                                                               | *`0`/`1`*                                                                                                  |
| *`bar_border_width`*                                                         | *Grosor en píxeles del borde que rodea la barra.*                                                       | *Entero ≥ 0*                                                                                               |
| *`bar_action_expand`*                                                        | *Si al hacer clic con ratón, abre menú de acción expandido (`1`).*                                      | *`0`/`1`*                                                                                                  |
| *`bar_border[1]` / `bar_border_unfocus[1]`*                                  | *Colores de borde de la barra: enfocado y desenfocado para pantalla “1” (multi-monitor).*               | *`rgb:RR/GG/BB`*                                                                                           |
| *`bar_color[1]` / `bar_color_selected[1]`*                                   | *Color de fondo normal y seleccionado de la barra.*                                                     | *`Null`*                                                                                                   |
| *`bar_font_color[1]`*                                                        | *Colores de fuente por defecto (puedes listar varios, comma-separated).*                                | *`rgb:..., rgb:..., ...`*                                                                                  |
| *`bar_font_color_selected`*                                                  | *Color de fuente del elemento activo.*                                                                  | *Nombre de color (`black`, `white`, etc.)*                                                                 |
| *`bar_font`*                                                                 | *Fuentes utilizadas. Sintaxis: `Fuente: tamaño[, Fuente2: tamaño2 …]`.*                                 | *`UbuntuMono Nerd Font:size=16, Cascadia Code NF:size=12, ...`*                                            |
| *`bar_action`*                                                               | *Script que se lanza al hacer clic en la barra.*                                                        | *Ruta absoluta: `~/.config/spectrwm/baraction.sh`*                                                         |
| *`bar_justify`*                                                              | *Alineación del texto: `left`, `center`, `right`.*                                                      | *`bar_justify = center`*                                                                                   |
| *`bar_format`*                                                               | *Formato de los campos (workspaces, layout, ventanas, fecha…). Usa códigos internos (`+W`, `+D`, etc.)* | *Ejemplo: `+\|L+@fn=2; +@fn=0;+@fg=1; +D+@fn=1;+@fg=2;+3<+W+\|R+@fn=2;+A` (ver manual para cada token).`* |
| *`workspace_indicator`*                                                      | *Cómo mostrar indicadores de workspaces (`listcurrent`, `listactive`, `markcurrent`, `printnames`).*    | *Múltiples separados por comas.*                                                                           |
| *`bar_at_bottom`*                                                            | *Poner la barra arriba (`0`) o abajo (`1`).*                                                            | *`0`/`1`*                                                                                                  |
| *`stack_enabled`*                                                            | *Mostrar stack (número de ventanas ocultas en layout)*                                                  | *`0`/`1`*                                                                                                  |
| *`clock_enabled`*                                                            | *Mostrar reloj de sistema.*                                                                             | *`0`/`1`*                                                                                                  |
| *`# clock_format`*                                                           | *(Comentado) Formato de fecha/hora si activas `clock_enabled`.*                                         | *Estilo `strftime`: `%a %b %d %R %Z %Y`.*                                                                  |
| *`iconic_enabled`*                                                           | *Botón para minimizar (iconizar) ventanas.*                                                             | *`0`/`1`*                                                                                                  |
| *`maximize_hide_bar`*                                                        | *Ocultar barra al maximizar ventana.*                                                                   | *`0`/`1`*                                                                                                  |
| *`window_class_enabled` / `window_instance_enabled` / `window_name_enabled`* | *Mostrar clase/instancia/nombre de ventana en barra.*                                                   | *`0`/`1` cada uno.*                                                                                        |
| *`verbose_layout`*                                                           | *Mostrar nombre completo de layout (tile, monocle, etc.).*                                              | *`0`/`1`*                                                                                                  |
| *`urgent_enabled`*                                                           | *Indicador de ventanas con estado urgent (ej. chats, notificaciones).*                                  | *`0`/`1`*                                                                                                  |

```bash
+|L+@fn=2; +@fn=0;+@fg=1; +D+@fn=1;+@fg=2;+3<+W+|R+@fn=2;+A
```

1. **`+|L`**

   * *`+|` = “reset” del estilo de texto y comienzo de nueva zona (nueva línea)*
   * *`L` = justificar **Left** (alinear a la izquierda)*

2. **`+@fn=2;`**

   * *Selecciona la **fuente 2** (índice 2) de la lista `bar_font`*
   * *`;` marca fin del comando*

3. **``**

   * *Carácter literal: el icono de Arch Linux (proporcionado por tu Nerd Font)*

4. **``** *(espacio)*

   * *Carácter normal para separar bloques*

5. **`+@fn=0;`**

   * *Vuelve a la **fuente 0** (índice 0)*

6. **`+@fg=1;`**

   * *Cambia el **color de primer plano** (foreground) al índice 1 de `bar_font_color`*

7. **``** *(espacio)*

   * *Otro espacio literal*

8. **`+D`**

   * *Muestra el **nombre del workspace** activo*

9. **`+@fn=1;`**

   * *Selecciona la **fuente 1***

10. **`+@fg=2;`**

    * *Cambia el foreground al índice 2 de `bar_font_color`*

11. **`+3<`**

    * *Inserta **3 espacios***

      * *`+num<` = un espacio (pad)*
      * *Prefijo `3` = repetir 3 veces*

12. **`+W`**

    * *Muestra el **nombre de la ventana** (título `_NET_WM_NAME`)*

13. **`+|R`**

    * *`+|` = reset estilo y nueva zona (nueva línea)*
    * *`R` = justificar **Right** (alinear a la derecha)*

14. **`+@fn=2;`**

    * *Vuelve a la **fuente 2***

15. **`+A`**

    * *Ejecuta el **script** definido en `bar_action` y muestra su salida*

---

## **4. Workspaces**

*Nombras los espacios y asignas íconos (requieren una Nerd Font instalada).*

```conf
name = ws[1]:󰈹   # Navegador
name = ws[2]:   # Editor de código
name = ws[3]:   # Terminal
name = ws[4]:󱍙   # Música
name = ws[5]:   # Imágenes
name = ws[6]:󰌨   # Miscelánea
```

* **Sintaxis:** *`name = ws[N]:ICON Texto opcional`*
* **ICON** *se especifica como un carácter Unicode provisto por tu Nerd Font.*

---

## **5. Tecla Modificadora**

```conf
modkey = Mod4
```

* **`Mod4`** *normalmente es la tecla “Windows” o “Super”.*
* *Valores comunes: `Mod1` (Alt), `Mod4` (Super).*

---

## **6. Atajos de Teclado (Bindings)**

### **6.1 Ventanas**

| *Acción*                | *Directiva*                                                        | *Descripción*                                           |
| ----------------------- | ------------------------------------------------------------------ | ------------------------------------------------------- |
| *Enfocar siguiente*     | *`bind[focus_next] = MOD+j`*                                       | *Con `Super+j` mueves foco abajo/adelante en el stack.* |
| *Enfocar anterior*      | *`bind[focus_prev] = MOD+k`*                                       | *`Super+k` mueve foco arriba/atrás.*                    |
| *Agrandar master*       | *`bind[master_grow] = MOD+l`*                                      | *`Super+l` aumenta tamaño del área master.*             |
| *Encoger master*        | *`bind[master_shrink] = MOD+h`*                                    | *`Super+h` reduce tamaño del área master.*              |
| *Flotar / tile*         | *`bind[float_toggle] = MOD+Shift+f`*                               | *Alterna entre modo flotante y tileado.*                |
| *Mover ventana down/up* | *`bind[swap_next] = MOD+Shift+j \| bind[swap_prev] = MOD+Shift+k`* | *Intercambia posición de ventanas en el stack.*         |
| *Cambiar layout*        | *`bind[cycle_layout] = MOD+Tab`*                                   | *Cicla entre layouts (tile, monocle, etc.).*            |
| *Cerrar ventana*        | *`bind[wind_del] = MOD+w`*                                         | *Mata/Cierra la ventana activa.*                        |
| *Reiniciar spectrwm*    | *`bind[restart] = MOD+Control+r`*                                  | *Recarga configuración sin cerrar sesión X.*            |
| *Salir de spectrwm*     | *`bind[quit] = MOD+Control+q`*                                     | *Cierra tu sesión de window manager.*                   |

### **6.2 Workspaces**

| *Acción*                       | *Bind*                                                                       | *Descripción*                                    |
| ------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------ |
| *Ir a ws N*                    | *`bind[ws_1] = MOD+1` …*                                                     | *`Super+1` → workspace 1, etc.*                  |
| *Mover ventana a ws N*         | *`bind[mvws_1] = MOD+Shift+1` …*                                             | *`Super+Shift+1` mueve la ventana a ws 1.*       |
| *Mover espacio a otro monitor* | *`bind[rg_move_next] = MOD+Control+j \| bind[rg_move_prev] = MOD+Control+k`* | *Envía workspace al monitor siguiente/anterior.* |

### **6.3 Lanzar Aplicaciones**

*Usan la directiva `program[...]` para definir comando y `bind[...]` para atajo.*

| *Alias*               | *program\[...]*                    | *bind\[...]*                       | *Qué hace*                              |
| --------------------- | ---------------------------------- | ---------------------------------- | --------------------------------------- |
| *Menú de apps*        | *`program[rofi] = rofi -show run`* | *`bind[rofi] = MOD+m`*             | *Abre rofi para ejecutar aplicaciones.* |
| *Navegación rofi*     | *`program[nav] = rofi -show`*      | *`bind[nav] = MOD+Shift+m`*        | *Abre rofi en otro modo.*               |
| *Terminal*            | *`program[alacritty] = alacritty`* | *`bind[alacritty] = MOD+Return`*   | *Lanza Alacritty.*                      |
| *Navegador*           | *`program[firefox] = firefox`*     | *`bind[firefox] = MOD+b`*          | *Lanza Firefox.*                        |
| *Explorador archivos* | *`program[thunar] = thunar`*       | *`bind[thunar] = MOD+e`*           | *Lanza Thunar.*                         |
| *Pantallazo completo* | *`program[scrot_full] = scrot`*    | *`bind[scrot_full] = MOD+s`*       | *Captura pantalla entera.*              |
| *Pantallazo área*     | *`program[scrot_area] = scrot -s`* | *`bind[scrot_area] = MOD+Shift+s`* | *Captura área seleccionada.*            |

**Puedes añadir más `program[...]`**

---

## **7. Hardware: Volumen y Brillo**

| *Acción*        | *program\[...]*                                                 | *bind\[...]*                              |
| --------------- | --------------------------------------------------------------- | ----------------------------------------- |
| *Bajar volumen* | *`program[voldown] = pactl set-sink-volume @DEFAULT_SINK@ -5%`* | *`bind[voldown] = XF86AudioLowerVolume`*  |
| *Subir volumen* | *`program[volup]   = pactl set-sink-volume @DEFAULT_SINK@ +5%`* | *`bind[volup]   = XF86AudioRaiseVolume`*  |
| *Mute/Unmute*   | *`program[mute]   = pactl set-sink-mute @DEFAULT_SINK@ toggle`* | *`bind[mute]    = XF86AudioMute`*         |
| *Subir brillo*  | *`program[brup]   = brightnessctl set +10%`*                    | *`bind[brup]    = XF86MonBrightnessUp`*   |
| *Bajar brillo*  | *`program[brdown] = brightnessctl set 10%-`*                    | *`bind[brdown]  = XF86MonBrightnessDown`* |

– *Usa las teclas multimedia especiales (`XF86…`) para control directo.*

---

## **8. Autostart (Ejecutar al inicio)**

```conf
autorun = ws[1]:~/.config/spectrwm/autostart.sh
```

* **`ws[1]:`** *→ lanza el script en el workspace 1.*
* **Ruta** *→ `~/.config/spectrwm/autostart.sh` debe ser ejecutable (`chmod +x`).*
* *Dentro de ese script puedes iniciar:*

  * *Demonios (picom, nm-applet, etc.)*
  * *Servicios de notificaciones*
  * *Comprobaciones de red*
  * *Lo que necesites para tu entorno de trabajo.*

---

### **Siguientes pasos**

1. **Revisa el manual de cada sección para detalles adicionales:**

   ```bash
   man spectrwm
   man brightnessctl
   man pactl
   ```

2. *Ajusta valores de colores y gaps según tu estética.*
3. *Crea tu `autostart.sh` para poblar tu entorno (tray, compositor, keyring, etc.).*

* *File `~/.config/spectrwm/spectrwm.conf`*

```ìni
# Spectrwm Config File
# https://github.com/conformal/spectrwm

workspace_limit  = 6
focus_mode       = default
focus_close      = previous
focus_close_wrap = 1
focus_default    = last
spawn_position   = next
workspace_clamp  = 0
warp_focus       = 1
warp_pointer     = 1

# Window Decorations

border_width            = 1
color_focus             = rgb:50/50/50
color_focus_maximized   = rgb:0f/10/1a
color_unfocus           = rgb:0f/10/1a
color_unfocus_maximized = rgb:0f/10/1a
region_padding          = 4
tile_gap                = 4

# Remove window border when bar is disabled and there is only one window in workspace
disable_border          = 1

# ---------------------------------- Bar -----------------------------------

bar_enabled             = 1
bar_border_width        = 0
bar_action_expand       = 1
bar_border[1]           = rgb:00/80/80
bar_border_unfocus[1]   = rgb:00/40/40
bar_color[1]            = rgb:0f/10/1a
bar_color_selected[1]   = rgb:00/80/80
bar_font_color[1]       = rgb:a6/ac/cd, rgb:f0/f0/f0, rgb:4c/56/6a
bar_font_color_selected = black
bar_font                = UbuntuMono Nerd Font:size=16, Cascadia Code NF:size=12, UbuntuMono Nerd Font:size=13
bar_action              = ~/.config/spectrwm/baraction.sh
bar_justify             = center
bar_format              = +|L+@fn=2; +@fn=0;+@fg=1; +D+@fn=1;+@fg=2;+3<+W+|R+@fn=2;+A
# Arch icon: nf-linux-archlinux (https://www.nerdfonts.com/cheat-sheet)
workspace_indicator     = listcurrent,listactive,markcurrent,printnames
bar_at_bottom           = 0
stack_enabled           = 1
clock_enabled           = 0
# clock_format          = %a %b %d %R %Z %Y
iconic_enabled          = 0
maximize_hide_bar       = 0
window_class_enabled    = 0
window_instance_enabled = 0
window_name_enabled     = 0
verbose_layout          = 1
urgent_enabled          = 1

# ------------------------------- Workspaces -------------------------------

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
name = ws[1]:󰈹  # 󰈹 : Browser (nf-md-firefox)
name = ws[2]:  #  : Code editor (nf-dev-vscode)
name = ws[3]:  #  : Terminal (nf-dev-terminal)
name = ws[4]:󱍙  # 󱍙 : Music folder (nf-md-folder_music)
name = ws[5]:  #  : Image viewer (nf-fa-image)
name = ws[6]:󰌨  # 󰌨 : Layers or misc (nf-md-layers)

# ---------------------------------- Keys ----------------------------------

modkey = Mod4

# ---------------- Windows -----------------

# Switch between windows in current stack pane
bind[focus_next]    = MOD+j
bind[focus_prev]    = MOD+k
# Change window sizes
bind[master_grow]   = MOD+l
bind[master_shrink] = MOD+h
# Toggle floating
bind[float_toggle]  = MOD+Shift+f
# Move windows up or down in current stack
bind[swap_next]     = MOD+Shift+j
bind[swap_prev]     = MOD+Shift+k
# Toggle between layouts
bind[cycle_layout]  = MOD+Tab
# Kill window
bind[wind_del]      = MOD+w
# Restart
bind[restart]       = MOD+Control+r
# Quit
bind[quit]          = MOD+Control+q

# --------------- Workspaces ---------------

# Go to workspace N
bind[ws_1]          = MOD+1
bind[ws_2]          = MOD+2
bind[ws_3]          = MOD+3
bind[ws_4]          = MOD+4
bind[ws_5]          = MOD+5
bind[ws_6]          = MOD+6

# Move window to workspace N
bind[mvws_1]        = MOD+Shift+1
bind[mvws_2]        = MOD+Shift+2
bind[mvws_3]        = MOD+Shift+3
bind[mvws_4]        = MOD+Shift+4
bind[mvws_5]        = MOD+Shift+5
bind[mvws_6]        = MOD+Shift+6

# Send workspace to next / prev screen
bind[rg_move_next]  = MOD+Control+j
bind[rg_move_prev]  = MOD+Control+k

# ------------------ Apps ------------------

# Menu
program[rofi]       = rofi -show run
bind[rofi]          = MOD+m
# Nav
program[nav]        = rofi -show
bind[nav]           = MOD+Shift+m

# Terminal
program[alacritty]  = alacritty
bind[alacritty]     = MOD+Return

# Browser
program[firefox]    = firefox
bind[firefox]       = MOD+b

# File explorer
program[thunar]     = thunar
bind[thunar]        = MOD+e

# Redshift
# program[redon]      = redshift -O 2400
# bind[redon]         = MOD+r
# program[redoff]     = redshift -x
# bind[redoff]        = MOD+Shift+r

# Screenshot
program[scrot_full]  = scrot
bind[scrot_full]     = MOD+s

program[scrot_area]  = scrot -s
bind[scrot_area]     = MOD+Shift+s

# ---------------- Hardware ----------------

# Volume
program[voldown]    = pactl set-sink-volume @DEFAULT_SINK@ -5%
bind[voldown]       = XF86AudioLowerVolume
program[volup]      = pactl set-sink-volume @DEFAULT_SINK@ +5%
bind[volup]         = XF86AudioRaiseVolume
program[mute]       = pactl set-sink-mute @DEFAULT_SINK@ toggle
bind[mute]          = XF86AudioMute

# Brightness
program[brup]       = brightnessctl set +10%
bind[brup]          = XF86MonBrightnessUp
program[brdown]     = brightnessctl set 10%-
bind[brdown]        = XF86MonBrightnessDown

# -------------------------------- Autorun ---------------------------------

autorun = ws[1]:~/.config/spectrwm/autostart.sh
```

---

**File `~/.config/spectrwm/baraction.sh`**

```bash
#!/bin/bash
# baraction.sh For Spectrwm Status Bar

icon() {
    echo -n "+@fg=1;$1 +@fg=0;"
}

percentage() {
    current=`echo $1 | sed 's/%//'`
    if [ $current -le 25 ]; then 
        echo -n "$(icon $2)"
    elif [ $current -le 50 ]; then
        echo -n "$(icon $3)"
    elif [ $current -le 75 ]; then
        echo -n "$(icon $4)"
    else
        echo -n "$(icon $5)"
    fi
}

# Icon
# nf-md-calendar_clock -> 󰃰
# Date
dte() {
    dte="$(date +"$(icon 󰃰) %d/%m/%Y $(icon ) %H:%M:%S %p ")"
    echo -e "$dte"
}

# Disk
hdd() {
    device="/dev/nvme1n1p3"
    hdd="$(df -h $device | awk 'NR==2{print $3, $5}')"
    echo -e "HDD: [$hdd]"
}

# Icon
# nf-fa-memory -> 
# Ram
mem() {
    mem=$(free | awk '/Mem/ {printf "%.2f MiB/%.2f MiB\n", $3 / 1024.0, $2 / 1024.0 }')
    echo -e "Mem: [ $mem ]"
}

# Cpu
cpu() {
    read cpu a b c previdle rest < /proc/stat
    prevtotal=$((a + b + c + previdle))
    sleep 0.5
    read cpu a b c idle rest < /proc/stat
    total=$((a + b + c + idle))
    declare -i cpu=$((100 * ((total - prevtotal) - (idle - previdle) ) / (total - prevtotal)))
    printf "Cpu: [ %.1f%% ]" "$cpu"
}

# Battery
bat() {
    bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT0 | 
        grep percentage |
        sed 's/ *percentage: *//g'`
        # nf-fa-battery_1 -> 
        # nf-fa-battery_2 -> 
        # nf-fa-battery_3 -> 
        # nf-fa-battery_4 -> 
    echo -n "$(percentage $bat            )  $bat"
} 

# Icon
# nf-md-brightness_7 -> 󰃠
# nf-md-brightness_6 -> 󰃟
# nf-md-brightness_5 -> 󰃞
# nf-md-brightness_4 -> 󰃝
# Brightness
br() {
    br=`brightnessctl | grep Current | cut -d"(" -f2 | sed "s/)//"`
    echo -n "$(percentage $br 󰃝  󰃞  󰃟  󰃠 ) [ $br ]"
}

# Icon
# nf-fa-volume_xmark -> 
# nf-fa-volume_off -> 
# nf-fa-volume_down -> 
# nf-md-volume_high -> 󰕾
# nf-fa-volume_high -> 
# Volume
vol() {
    declare -i vol=`pamixer --get-volume`
    if [[ `pamixer --get-mute` == "true" ]]; then
        echo -n "$(icon ) $vol%"
    else
        echo -n "$(percentage $vol   󰕾 ) $vol%"
    fi
}

declare -i SLEEP_SEC=1
while :; do
    # echo -n "$(br) "
    # echo -n "$(hdd) "
    # echo -n "$(mem) "
    # echo -n "$(cpu) "
    # if [ -d /org/freedesktop/UPower/devices/battery_BAT0 ]; then
    #     echo -n "$(bat) "
    # fi

    echo -n "$(vol) "
    echo "$(dte)"
 sleep $SLEEP_SEC

done
```

* **File `~/.config/spectrwm/autostart.sh`**

```bash
#!/bin/bash

# Keyborad Latam
if [[ "$(setxkbmap -query | tail -n 1 | xargs | awk '{print $2}')" != "latam" ]]; then
  setxkbmap latam
fi

trayer \
  --edge top \
  --align right \
  --monitor 0 \
  --widthtype request \
  --heighttype request \
  --height 20 \
  --alpha 0 \
  --transparent true \
  --tint 0x0F101A \
  --SetDockType false \
  --SetPartialStrut false \
  --iconspacing 5 \
  --margin 300 &>/dev/null & disown

if [ -f ~/.theme/set-themes.py ]; then
  python ~/.theme/set-themes.py "spectrwm" &
fi
```
