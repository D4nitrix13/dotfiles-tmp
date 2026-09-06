<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Configuración De Cbatticon, Pacman, Cronie, Notificaciones & Instalación De Utilidades Y Dependencias**

────────────────────────────────────────────────────────────

1. **Configuración de cbatticon en autostart.sh de Qtile**
────────────────────────────────────────────────────────────

**Comando:** *cbatticon*
**Descripción:** *cbatticon es un monitor gráfico para el estado de la batería que se integra en la bandeja del sistema.*
*No tiene subcomandos, pero sí acepta opciones.*

**Opciones:**

- **-u:** *Define el intervalo de actualización en segundos.*

*Valores:*

- **5:** *Actualiza cada 5 segundos el estado de la batería.*

**Ejemplo práctico:**
**Archivo:** *~/.config/qtile/autostart.sh*

```bash
if [ -f /sys/class/power_supply/BAT0/status ]; then
    cbatticon -u 5 &
fi
```

**Explicación:** *Si existe el archivo que indica la presencia de batería (BAT0), se lanza cbatticon con actualización cada 5 segundos. El & permite que se ejecute en segundo plano.*

────────────────────────────────────────────────────────────
2. **Instalación de utilidades esenciales y dependencias**
────────────────────────────────────────────────────────────

**Comando principal:** *pacman*
**Descripción:** *Pacman es el gestor de paquetes oficial de Arch Linux. Instala, actualiza, elimina y gestiona paquetes.*

**Subcomando:** *-Syu*
**Descripción:** *Sincroniza la base de datos de paquetes y actualiza el sistema.*

- **-S:** *Instala paquetes.*
- **-y:** *Sincroniza la base de datos de paquetes.*
- **-u:** *Actualiza todos los paquetes del sistema.*

*Opciones:*

- **--noconfirm:** *Omite cualquier confirmación de usuario.*

**Valores:**

- **Nombres de paquetes a instalar.**

**Ejemplos prácticos:**

**Instalación de herramientas gráficas y de ventanas:**

```bash
sudo pacman -Syu --noconfirm wmctrl xorg-xprop xorg-xwininfo xorg-xrandr
```

**Explicación:** *Instala herramientas útiles para manipular ventanas en Xorg.*

**Instalación de utilidades para monitoreo y scripting:**

```bash
sudo pacman -Syu --noconfirm psutils python-pip python-psutil
```

**Explicación:** *Instala utilidades para gestión de procesos y scripting en Python.*

**Paquetes adicionales:**

```bash
sudo pacman -Syu pacman-contrib --noconfirm
sudo pacman -Syu python-dbus-fast --noconfirm
sudo pacman -Syu --noconfirm lightdm-slick-greeter
sudo pacman -Syu upower --noconfirm
```

- **pacman-contrib:** *contiene scripts y utilidades adicionales como paccache.*
- **python-dbus-fast:** *implementación eficiente del protocolo D-Bus para Python.*
- **lightdm-slick-greeter:** *pantalla de inicio de sesión visual para LightDM.*
- **upower:** *backend de gestión de energía, útil para cbatticon y otras herramientas de batería.*

────────────────────────────────────────────────────────────
3. **Configuración de tareas cron (cronie)**
────────────────────────────────────────────────────────────

**Comando:** *pacman*
**Ejemplo:**

```bash
sudo pacman -Syu cronie --noconfirm
```

**Explicación:** *Instala cronie, un daemon que permite ejecutar tareas programadas con cron.*

**Comando:** *systemctl*
**Subcomando:** *enable*
**Descripción:** *Activa un servicio para que se inicie automáticamente en el arranque.*

**Ejemplo:**

```bash
sudo systemctl enable cronie.service
```

**Explicación:** *Habilita cronie en el arranque.*

────────────────────────────────────────────────────────────
4. **Definición de editores por defecto**
────────────────────────────────────────────────────────────

**Comando:** *export*
**Descripción:** *Asigna variables de entorno para la sesión actual.*

**Ejemplo:**

```bash
export VISUAL="nvim"
export EDITOR="nvim"
```

**Explicación:** *Define Neovim como editor de texto predeterminado para tareas como edición de mensajes de git o crontabs.*

────────────────────────────────────────────────────────────
5. **Organización de directorios personales y de root**
────────────────────────────────────────────────────────────

**Comando:** *mkdir*
**Descripción:** *Crea directorios.*
**Opciones:**

- **-p:** *Crea directorios padre si no existen.*
- **-v:** *Muestra mensajes por cada creación.*

**Ejemplos:**

```bash
sudo mkdir /root/Scripts -pv
mkdir /home/d4nitrix13/Scripts -pv
```

**Explicación:** *Crea directorios Scripts para root y el usuario.*

────────────────────────────────────────────────────────────
6. **Configuración de picom y dunst**
────────────────────────────────────────────────────────────

**Picom:**

```bash
mkdir ~/.config/picom -pv
touch ~/.config/picom/picom.conf
```

- **mkdir:** *crea el directorio de configuración de picom.*
- **touch:** *crea un archivo vacío de configuración llamado picom.conf.*

**Dunst:**

```bash
mkdir ~/.config/dunst -pv
cp /etc/dunst/dunstrc ~/.config/dunst/dunstrc
```

- **mkdir:** *crea el directorio de configuración de dunst.*
- **cp:** *copia la configuración por defecto del sistema al directorio de usuario para personalizarla.*

────────────────────────────────────────────────────────────
