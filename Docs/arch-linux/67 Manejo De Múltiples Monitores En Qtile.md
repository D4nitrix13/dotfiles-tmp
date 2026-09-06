<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Manejo de múltiples monitores en Qtile***

**Para manejar múltiples monitores en Qtile, puedes usar la herramienta `xrandr` para configurar la resolución y la disposición de tus pantallas.**

---

## ***¿Qué es xrandr?***

- *`xrandr` (X Resize, Rotate and Reflect Extension) es una utilidad de línea de comandos para gestionar las configuraciones de pantalla en sistemas que utilizan el servidor X. Con `xrandr`, puedes cambiar la resolución, la orientación, la rotación, y otros parámetros de los monitores conectados a tu sistema.*

---

### ***Explicación detallada de la salida de xrandr***

**Cuando ejecutas el comando `xrandr` sin argumentos, muestra una lista de las pantallas conectadas y sus resoluciones soportadas. Aquí tienes un ejemplo de salida y su explicación:**

```bash
xrandr
Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 16384 x 16384
DVI-D-1 disconnected primary (normal left inverted right x axis y axis)
HDMI-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 521mm x 293mm
   1920x1080     60.00*+  59.96    50.00    59.94    59.93  
   1680x1050     59.95    59.88  
   1400x1050     59.98  
   1600x900      59.95    60.00    59.82  
   1280x1024     60.02  
   1440x900      59.90  
   1400x900      59.96    59.88  
   1280x960      60.00  
   1440x810      59.97  
   1368x768      59.88    59.85  
   1280x800      59.99    59.97    59.81    59.91  
   1280x720      60.00    59.99    59.86    60.00    50.00    59.94    59.74  
   1024x768      60.04    70.07    60.00  
   960x720       60.00  
   928x696       60.05  
   896x672       60.01  
   1024x576      59.95    59.96    59.90    59.82  
   960x600       59.93    60.00  
   960x540       59.96    59.99    59.63    59.82  
   800x600       70.00    65.00    60.00    72.19    60.32    56.25  
   840x525       60.01    59.88  
   864x486       59.92    59.57  
   720x576       50.00  
   700x525       59.98  
   800x450       59.95    59.82  
   720x480       60.00    59.94  
   640x512       60.02  
   700x450       59.96    59.88  
   640x480       60.00    72.81    66.67    60.00    59.94  
   720x405       59.51    58.99  
   720x400       70.08  
   684x384       59.88    59.85  
   640x400       59.88    59.98  
   640x360       59.86    59.83    59.84    59.32  
   512x384       70.07    60.00  
   512x288       60.00    59.92  
   480x270       59.63    59.82  
   400x300       72.19    60.32    56.34  
   432x243       59.92    59.57  
   320x240       72.81    60.05  
   360x202       59.51    59.13  
   320x180       59.84    59.32  
DP-1 disconnected (normal left inverted right x axis y axis)
HDMI-2 disconnected (normal left inverted right x axis y axis)
```

---

#### ***Explicación de los componentes***

- **Screen 0:** *Indica el número de la pantalla gestionada por el servidor X.*
- **minimum 320 x 200, current 1920 x 1080, maximum 16384 x 16384:** *Muestra las resoluciones mínima, actual y máxima soportadas.*
- **DVI-D-1 disconnected primary:** *Indica que el puerto DVI-D-1 está desconectado y es el principal por defecto.*
- **HDMI-1 connected 1920x1080+0+0:** *Indica que el puerto HDMI-1 está conectado con una resolución de 1920x1080 y desplazamiento (offset) de 0x0.*
- **521mm x 293mm:** *Dimensiones físicas del monitor.*
- **Resoluciones listadas:** *Muestra las resoluciones soportadas y sus respectivas frecuencias de refresco.*

---

### ***Comandos útiles de xrandr***

---

#### ***Configurar resolución y disposición de monitores***

**Para configurar las resoluciones de los monitores, puedes usar el siguiente comando:**

```bash
xrandr --output eDP-1 --mode 1920x1080 --output HDMI-1 --mode 1920x1080
```

- **eDP-1** *es comúnmente el monitor de una laptop.*
- **HDMI-1** *se refiere a un monitor externo conectado a través de un puerto HDMI.*

---

#### ***Establecer un monitor como primario***

**Para establecer un monitor como el principal o primario:**

```bash
xrandr --output eDP-1 --primary --mode 1920x1080 --output HDMI-1 --mode 1920x1080
```

---

### ***Herramienta gráfica: arandr***

- *Para facilitar la configuración de múltiples monitores, puedes instalar `arandr`, una herramienta gráfica que proporciona una interfaz amigable para gestionar las pantallas.*

```bash
sudo pacman -Syu arandr --noconfirm
```

- *Al ejecutar `arandr`, se abrirá una aplicación gráfica donde puedes ajustar la configuración de tus monitores. Después de realizar los cambios, haz clic en el botón "Aplicar" para aplicar los ajustes. Luego, reinicia el gestor de ventanas Qtile con la combinación de teclas `Mod4 + Ctrl + r`.*

- *Esta configuración debería ayudarte a manejar eficientemente múltiples monitores en Qtile, ya sea a través de la línea de comandos con `xrandr` o mediante la interfaz gráfica de `arandr`.*

---

### ***Información de los repositorios y las páginas oficiales de `xrandr` y `arandr` en Arch Linux:***

---

### ***xrandr***

- **Repositorio GitLab (parte del proyecto xorg):** *[xrandr](https://gitlab.freedesktop.org/xorg/app/xrandr "https://gitlab.freedesktop.org/xorg/app/xrandr")*
- **Página oficial en Arch Linux:** *[xorg-xrandr](https://archlinux.org/packages/extra/x86_64/xorg-xrandr/ "https://archlinux.org/packages/extra/x86_64/xorg-xrandr/")*

---

### ***arandr***

- **Repositorio GitHub:** *[arandr](https://github.com/chrysn/arandr "https://github.com/chrysn/arandr")*
- **Página oficial en Arch Linux:** *[arandr](https://archlinux.org/packages/community/any/arandr/ "https://archlinux.org/packages/community/any/arandr/")*

- *Estas páginas te proporcionarán la información necesaria para obtener los binarios y acceder a la documentación oficial.*
