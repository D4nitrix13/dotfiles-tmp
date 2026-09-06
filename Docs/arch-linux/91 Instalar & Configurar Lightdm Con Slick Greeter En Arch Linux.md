<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Instalar & Configurar Lightdm Con Slick Greeter En Arch Linux**

```bash
sudo pacman -Syu --noconfirm --needed lightdm-slick-greeter
```

- **`lightdm-slick-greeter`:** *Greeter moderno y elegante para LightDM basado en GTK+.*
  - **ArchWiki:** *[LightDM](https://wiki.archlinux.org/title/LightDM "https://wiki.archlinux.org/title/LightDM")*
  - **Guía externa:** *[LinuxGenie: instalar y configurar LightDM](https://linuxgenie.net/install-configure-lightdm-display-manager-arch-linux/ "https://linuxgenie.net/install-configure-lightdm-display-manager-arch-linux/")*
  - **Página del paquete:** *[lightdm-slick-greeter en Arch](https://archlinux.org/packages/extra/x86_64/lightdm-slick-greeter/ "https://archlinux.org/packages/extra/x86_64/lightdm-slick-greeter/")*

---

## **Habilitar y configurar LightDM**

1. **Editar el archivo de configuración de LightDM:**

   ```bash
   sudo nano /etc/lightdm/lightdm.conf
   ```

    **Default Config:**

    ```ini
    #
    # General configuration
    #
    # start-default-seat = True to always start one seat if none are defined in the configuration
    # greeter-user = User to run greeter as
    # minimum-display-number = Minimum display number to use for X servers
    # minimum-vt = First VT to run displays on
    # lock-memory = True to prevent memory from being paged to disk
    # user-authority-in-system-dir = True if session authority should be in the system location
    # guest-account-script = Script to be run to setup guest account
    # logind-check-graphical = True to on start seats that are marked as graphical by logind
    # log-directory = Directory to log information to
    # run-directory = Directory to put running state in
    # cache-directory = Directory to cache to
    # sessions-directory = Directory to find sessions
    # remote-sessions-directory = Directory to find remote sessions
    # greeters-directory = Directory to find greeters
    # backup-logs = True to move add a .old suffix to old log files when opening new ones
    # dbus-service = True if LightDM provides a D-Bus service to control it
    #
    [LightDM]
    #start-default-seat=true
    #greeter-user=lightdm
    #minimum-display-number=0
    #minimum-vt=7 # Setting this to a value < 7 implies security issues, see FS#46799
    #lock-memory=true
    #user-authority-in-system-dir=false
    #guest-account-script=guest-account
    logind-check-graphical=true
    #log-directory=/var/log/lightdm
    run-directory=/run/lightdm
    #cache-directory=/var/cache/lightdm
    #sessions-directory=/usr/share/lightdm/sessions:/usr/share/xsessions:/usr/share/wayland-sessions
    #remote-sessions-directory=/usr/share/lightdm/remote-sessions
    #greeters-directory=$XDG_DATA_DIRS/lightdm/greeters:$XDG_DATA_DIRS/xgreeters
    #backup-logs=true
    #dbus-service=true

    #
    # Seat configuration
    #
    # Seat configuration is matched against the seat name glob in the section, for example:
    # [Seat:*] matches all seats and is applied first.
    # [Seat:seat0] matches the seat named "seat0".
    # [Seat:seat-thin-client*] matches all seats that have names that start with "seat-thin-client".
    #
    # type = Seat type (local, xremote)
    # pam-service = PAM service to use for login
    # pam-autologin-service = PAM service to use for autologin
    # pam-greeter-service = PAM service to use for greeters
    # xserver-command = X server command to run (can also contain arguments e.g. X -special-option)
    # xmir-command = Xmir server command to run (can also contain arguments e.g. Xmir -special-option)
    # xserver-config = Config file to pass to X server
    # xserver-layout = Layout to pass to X server
    # xserver-allow-tcp = True if TCP/IP connections are allowed to this X server
    # xserver-share = True if the X server is shared for both greeter and session
    # xserver-hostname = Hostname of X server (only for type=xremote)
    # xserver-display-number = Display number of X server (only for type=xremote)
    # xdmcp-manager = XDMCP manager to connect to (implies xserver-allow-tcp=true)
    # xdmcp-port = XDMCP UDP/IP port to communicate on
    # xdmcp-key = Authentication key to use for XDM-AUTHENTICATION-1 (stored in keys.conf)
    # greeter-session = Session to load for greeter
    # greeter-hide-users = True to hide the user list
    # greeter-allow-guest = True if the greeter should show a guest login option
    # greeter-show-manual-login = True if the greeter should offer a manual login option
    # greeter-show-remote-login = True if the greeter should offer a remote login option
    # user-session = Session to load for users
    # allow-user-switching = True if allowed to switch users
    # allow-guest = True if guest login is allowed
    # guest-session = Session to load for guests (overrides user-session)
    # session-wrapper = Wrapper script to run session with
    # greeter-wrapper = Wrapper script to run greeter with
    # guest-wrapper = Wrapper script to run guest sessions with
    # display-setup-script = Script to run when starting a greeter session (runs as root)
    # display-stopped-script = Script to run after stopping the display server (runs as root)
    # greeter-setup-script = Script to run when starting a greeter (runs as root)
    # session-setup-script = Script to run when starting a user session (runs as root)
    # session-cleanup-script = Script to run when quitting a user session (runs as root)
    # autologin-guest = True to log in as guest by default
    # autologin-user = User to log in with by default (overrides autologin-guest)
    # autologin-user-timeout = Number of seconds to wait before loading default user
    # autologin-session = Session to load for automatic login (overrides user-session)
    # autologin-in-background = True if autologin session should not be immediately activated
    # exit-on-failure = True if the daemon should exit if this seat fails
    #
    [Seat:*]
    #type=local
    #pam-service=lightdm
    #pam-autologin-service=lightdm-autologin
    #pam-greeter-service=lightdm-greeter
    #xserver-command=X
    #xmir-command=Xmir
    #xserver-config=
    #xserver-layout=
    #xserver-allow-tcp=false
    #xserver-share=true
    #xserver-hostname=
    #xserver-display-number=
    #xdmcp-manager=
    #xdmcp-port=177
    #xdmcp-key=
    #greeter-session=example-gtk-gnome
    #greeter-hide-users=false
    #greeter-allow-guest=true
    #greeter-show-manual-login=false
    #greeter-show-remote-login=true
    #user-session=default
    #allow-user-switching=true
    #allow-guest=true
    #guest-session=
    session-wrapper=/etc/lightdm/Xsession
    #greeter-wrapper=
    #guest-wrapper=
    #display-setup-script=
    #display-stopped-script=
    #greeter-setup-script=
    #session-setup-script=
    #session-cleanup-script=
    #autologin-guest=false
    #autologin-user=
    #autologin-user-timeout=0
    #autologin-in-background=false
    #autologin-session=
    #exit-on-failure=false

    #
    # XDMCP Server configuration
    #
    # enabled = True if XDMCP connections should be allowed
    # port = UDP/IP port to listen for connections on
    # listen-address = Host/address to listen for XDMCP connections (use all addresses if not present)
    # key = Authentication key to use for XDM-AUTHENTICATION-1 or blank to not use authentication (stored in keys.conf)
    # hostname = Hostname to report to XDMCP clients (defaults to system hostname if unset)
    #
    # The authentication key is a 56 bit DES key specified in hex as 0xnnnnnnnnnnnnnn.  Alternatively
    # it can be a word and the first 7 characters are used as the key.
    #
    [XDMCPServer]
    #enabled=false
    #port=177
    #listen-address=
    #key=
    #hostname=

    #
    # VNC Server configuration
    #
    # enabled = True if VNC connections should be allowed
    # command = Command to run Xvnc server with
    # port = TCP/IP port to listen for connections on
    # listen-address = Host/address to listen for VNC connections (use all addresses if not present)
    # width = Width of display to use
    # height = Height of display to use
    # depth = Color depth of display to use
    #
    [VNCServer]
    #enabled=false
    #command=Xvnc
    #port=5900
    #listen-address=
    #width=1024
    #height=768
    #depth=8
    ```

   **Cambiar:**

   ```ini
   #greeter-session=example-gtk-gnome
   ```

   **Por:**

   ```ini
   greeter-session=lightdm-slick-greeter
   ```

   **Quedará El Fichero De Configuración De La Siguiente Manera:**

    ```ini
    #
    # General configuration
    #
    # start-default-seat = True to always start one seat if none are defined in the configuration
    # greeter-user = User to run greeter as
    # minimum-display-number = Minimum display number to use for X servers
    # minimum-vt = First VT to run displays on
    # lock-memory = True to prevent memory from being paged to disk
    # user-authority-in-system-dir = True if session authority should be in the system location
    # guest-account-script = Script to be run to setup guest account
    # logind-check-graphical = True to on start seats that are marked as graphical by logind
    # log-directory = Directory to log information to
    # run-directory = Directory to put running state in
    # cache-directory = Directory to cache to
    # sessions-directory = Directory to find sessions
    # remote-sessions-directory = Directory to find remote sessions
    # greeters-directory = Directory to find greeters
    # backup-logs = True to move add a .old suffix to old log files when opening new ones
    # dbus-service = True if LightDM provides a D-Bus service to control it
    #
    [LightDM]
    #start-default-seat=true
    #greeter-user=lightdm
    #minimum-display-number=0
    #minimum-vt=7 # Setting this to a value < 7 implies security issues, see FS#46799
    #lock-memory=true
    #user-authority-in-system-dir=false
    #guest-account-script=guest-account
    logind-check-graphical=true
    #log-directory=/var/log/lightdm
    run-directory=/run/lightdm
    #cache-directory=/var/cache/lightdm
    #sessions-directory=/usr/share/lightdm/sessions:/usr/share/xsessions:/usr/share/wayland-sessions
    #remote-sessions-directory=/usr/share/lightdm/remote-sessions
    #greeters-directory=$XDG_DATA_DIRS/lightdm/greeters:$XDG_DATA_DIRS/xgreeters
    #backup-logs=true
    #dbus-service=true

    #
    # Seat configuration
    #
    # Seat configuration is matched against the seat name glob in the section, for example:
    # [Seat:*] matches all seats and is applied first.
    # [Seat:seat0] matches the seat named "seat0".
    # [Seat:seat-thin-client*] matches all seats that have names that start with "seat-thin-client".
    #
    # type = Seat type (local, xremote)
    # pam-service = PAM service to use for login
    # pam-autologin-service = PAM service to use for autologin
    # pam-greeter-service = PAM service to use for greeters
    # xserver-command = X server command to run (can also contain arguments e.g. X -special-option)
    # xmir-command = Xmir server command to run (can also contain arguments e.g. Xmir -special-option)
    # xserver-config = Config file to pass to X server
    # xserver-layout = Layout to pass to X server
    # xserver-allow-tcp = True if TCP/IP connections are allowed to this X server
    # xserver-share = True if the X server is shared for both greeter and session
    # xserver-hostname = Hostname of X server (only for type=xremote)
    # xserver-display-number = Display number of X server (only for type=xremote)
    # xdmcp-manager = XDMCP manager to connect to (implies xserver-allow-tcp=true)
    # xdmcp-port = XDMCP UDP/IP port to communicate on
    # xdmcp-key = Authentication key to use for XDM-AUTHENTICATION-1 (stored in keys.conf)
    # greeter-session = Session to load for greeter
    # greeter-hide-users = True to hide the user list
    # greeter-allow-guest = True if the greeter should show a guest login option
    # greeter-show-manual-login = True if the greeter should offer a manual login option
    # greeter-show-remote-login = True if the greeter should offer a remote login option
    # user-session = Session to load for users
    # allow-user-switching = True if allowed to switch users
    # allow-guest = True if guest login is allowed
    # guest-session = Session to load for guests (overrides user-session)
    # session-wrapper = Wrapper script to run session with
    # greeter-wrapper = Wrapper script to run greeter with
    # guest-wrapper = Wrapper script to run guest sessions with
    # display-setup-script = Script to run when starting a greeter session (runs as root)
    # display-stopped-script = Script to run after stopping the display server (runs as root)
    # greeter-setup-script = Script to run when starting a greeter (runs as root)
    # session-setup-script = Script to run when starting a user session (runs as root)
    # session-cleanup-script = Script to run when quitting a user session (runs as root)
    # autologin-guest = True to log in as guest by default
    # autologin-user = User to log in with by default (overrides autologin-guest)
    # autologin-user-timeout = Number of seconds to wait before loading default user
    # autologin-session = Session to load for automatic login (overrides user-session)
    # autologin-in-background = True if autologin session should not be immediately activated
    # exit-on-failure = True if the daemon should exit if this seat fails
    #
    [Seat:*]
    #type=local
    #pam-service=lightdm
    #pam-autologin-service=lightdm-autologin
    #pam-greeter-service=lightdm-greeter
    #xserver-command=X
    #xmir-command=Xmir
    #xserver-config=
    #xserver-layout=
    #xserver-allow-tcp=false
    #xserver-share=true
    #xserver-hostname=
    #xserver-display-number=
    #xdmcp-manager=
    #xdmcp-port=177
    #xdmcp-key=
    #greeter-session=example-gtk-gnome

    # Set New Theme Lightdm
    greeter-session=lightdm-slick-greeter

    #greeter-hide-users=false
    #greeter-allow-guest=true
    #greeter-show-manual-login=false
    #greeter-show-remote-login=true
    #user-session=default
    #allow-user-switching=true
    #allow-guest=true
    #guest-session=
    session-wrapper=/etc/lightdm/Xsession
    #greeter-wrapper=
    #guest-wrapper=
    #display-setup-script=
    #display-stopped-script=
    #greeter-setup-script=
    #session-setup-script=
    #session-cleanup-script=
    #autologin-guest=false
    #autologin-user=
    #autologin-user-timeout=0
    #autologin-in-background=false
    #autologin-session=
    #exit-on-failure=false

    #
    # XDMCP Server configuration
    #
    # enabled = True if XDMCP connections should be allowed
    # port = UDP/IP port to listen for connections on
    # listen-address = Host/address to listen for XDMCP connections (use all addresses if not present)
    # key = Authentication key to use for XDM-AUTHENTICATION-1 or blank to not use authentication (stored in keys.conf)
    # hostname = Hostname to report to XDMCP clients (defaults to system hostname if unset)
    #
    # The authentication key is a 56 bit DES key specified in hex as 0xnnnnnnnnnnnnnn.  Alternatively
    # it can be a word and the first 7 characters are used as the key.
    #
    [XDMCPServer]
    #enabled=false
    #port=177
    #listen-address=
    #key=
    #hostname=

    #
    # VNC Server configuration
    #
    # enabled = True if VNC connections should be allowed
    # command = Command to run Xvnc server with
    # port = TCP/IP port to listen for connections on
    # listen-address = Host/address to listen for VNC connections (use all addresses if not present)
    # width = Width of display to use
    # height = Height of display to use
    # depth = Color depth of display to use
    #
    [VNCServer]
    #enabled=false
    #command=Xvnc
    #port=5900
    #listen-address=
    #width=1024
    #height=768
    #depth=8
    ```

2. **Copiar el archivo de configuración base del greeter:**

   ```bash
   sudo cp /usr/share/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/slick-greeter.conf
   ```

    **Contenido Del Fichero `/etc/lightdm/slick-greeter.conf`:**

    ```ini
    # LightDM GTK Configuration
    # Available configuration options listed below.
    # Please list the configuration options that you want to use after [greeter] without the # for example:
    # [greeter]
    # example-option=example-value
    #
    # Appearance:
    #  theme-name = GTK theme to use
    #  icon-theme-name = Icon theme to use
    #  cursor-theme-name = Cursor theme to use
    #  cursor-theme-size = Cursor size to use
    #  background = Background file to use, either an image path or a color (e.g. #772953)
    #  user-background = false|true ("true" by default)  Display user background (if available)
    #  transition-duration = Length of time (in milliseconds) to transition between background images ("500" by default)
    #  transition-type = ease-in-out|linear|none  ("ease-in-out" by default)
    #
    # Fonts:
    #  font-name = Font to use
    #  xft-antialias = false|true  Whether to antialias Xft fonts
    #  xft-dpi = Resolution for Xft in dots per inch (e.g. 96)
    #  xft-hintstyle = none|slight|medium|hintfull  What degree of hinting to use
    #  xft-rgba = none|rgb|bgr|vrgb|vbgr  Type of subpixel antialiasing
    #
    # Login window:
    #  active-monitor = Monitor to display greeter window (name or number). Use #cursor value to display greeter at monitor with cursor. Can be a semicolon separated list
    #  position = x y ("50% 50%" by default)  Login window position
    #  default-user-image = Image used as default user icon, path or #icon-name
    #  hide-user-image = false|true ("false" by default)
    #  round-user-image = false|true ("true" by default)
    #  highlight-logged-user  = false|true ("true" by default)
    #
    # Panel:
    #  panel-position = top|bottom ("top" by default)
    #  clock-format = strftime-format string, e.g. %H:%M
    #  indicators = semi-colon ";" separated list of allowed indicator modules. Built-in indicators include "~a11y", "~language", "~session", "~power", "~clock", "~host", "~spacer", "~layout". Unity indicators can be represented by short name (e.g. "sound", "power"), service file name, or absolute path
    #  keyboard-layouts = semi-colon ";" separated list keyboard layouts to be listed by the "~layout" indicator (empty by default which provides all available layouts)
    #
    # Accessibility:
    #  a11y-states = states of accessibility features: "name" - save state on exit, "-name" - disabled at start (default value for unlisted), "+name" - enabled at start. Allowed names: contrast, font, keyboard, reader.
    #  keyboard = command to launch on-screen keyboard (e.g. "onboard")
    #  keyboard-position = x y[;width height] ("50%,center -0;50% 25%" by default)  Works only for "onboard"
    #  reader = command to launch screen reader (e.g. "orca")
    #  at-spi-enabled = false|true ("true" by default) Enables accessibility at-spi-command if the greeter is built with it enabled
    #
    # Security:
    #  allow-debugging = false|true ("false" by default)
    #  screensaver-timeout = Timeout (in seconds) until the screen blanks when the greeter is called as lockscreen
    #
    # Session:
    #  default-session = session manager to be started when none has been selected by the user and no one is set as last used (unset by default)
    #
    # Template for per-monitor configuration:
    #  [monitor: name]
    #  background = overrides default value
    #  user-background = overrides default value
    #  laptop = false|true ("false" by default) Marks monitor as laptop display
    #  transition-duration = overrides default value
    #
    [greeter]
    #background=
    #user-background=
    #theme-name=
    #icon-theme-name=
    #font-name=
    #xft-antialias=
    #xft-dpi=
    #xft-hintstyle=
    #xft-rgba=
    #indicators=
    #clock-format=
    #keyboard=
    #reader=
    #position=
    #screensaver-timeout=
    ```

3. **Editar el archivo para establecer un fondo personalizado:**

   ```bash
   sudo nano /etc/lightdm/slick-greeter.conf
   ```

   **Agregar o modificar la sección:**

   ```ini
   [Greeter]
   background=/usr/share/backgrounds/629-Wallpaper.jpg
   ```

   **El Fichero slick-Greeter.conf Debería Quedar De La Siguiente Manera:**

    ```ini
    # LightDM GTK Configuration
    # Available configuration options listed below.
    # Please list the configuration options that you want to use after [greeter] without the # for example:
    # [greeter]
    # example-option=example-value
    #
    # Appearance:
    #  theme-name = GTK theme to use
    #  icon-theme-name = Icon theme to use
    #  cursor-theme-name = Cursor theme to use
    #  cursor-theme-size = Cursor size to use
    #  background = Background file to use, either an image path or a color (e.g. #772953)
    #  user-background = false|true ("true" by default)  Display user background (if available)
    #  transition-duration = Length of time (in milliseconds) to transition between background images ("500" by default)
    #  transition-type = ease-in-out|linear|none  ("ease-in-out" by default)
    #
    # Fonts:
    #  font-name = Font to use
    #  xft-antialias = false|true  Whether to antialias Xft fonts
    #  xft-dpi = Resolution for Xft in dots per inch (e.g. 96)
    #  xft-hintstyle = none|slight|medium|hintfull  What degree of hinting to use
    #  xft-rgba = none|rgb|bgr|vrgb|vbgr  Type of subpixel antialiasing
    #
    # Login window:
    #  active-monitor = Monitor to display greeter window (name or number). Use #cursor value to display greeter at monitor with cursor. Can be a semicolon separated list
    #  position = x y ("50% 50%" by default)  Login window position
    #  default-user-image = Image used as default user icon, path or #icon-name
    #  hide-user-image = false|true ("false" by default)
    #  round-user-image = false|true ("true" by default)
    #  highlight-logged-user  = false|true ("true" by default)
    #
    # Panel:
    #  panel-position = top|bottom ("top" by default)
    #  clock-format = strftime-format string, e.g. %H:%M
    #  indicators = semi-colon ";" separated list of allowed indicator modules. Built-in indicators include "~a11y", "~language", "~session", "~power", "~clock", "~host", "~spacer", "~layout". Unity indicators can be represented by short name (e.g. "sound", "power"), service file name, or absolute path
    #  keyboard-layouts = semi-colon ";" separated list keyboard layouts to be listed by the "~layout" indicator (empty by default which provides all available layouts)
    #
    # Accessibility:
    #  a11y-states = states of accessibility features: "name" - save state on exit, "-name" - disabled at start (default value for unlisted), "+name" - enabled at start. Allowed names: contrast, font, keyboard, reader.
    #  keyboard = command to launch on-screen keyboard (e.g. "onboard")
    #  keyboard-position = x y[;width height] ("50%,center -0;50% 25%" by default)  Works only for "onboard"
    #  reader = command to launch screen reader (e.g. "orca")
    #  at-spi-enabled = false|true ("true" by default) Enables accessibility at-spi-command if the greeter is built with it enabled
    #
    # Security:
    #  allow-debugging = false|true ("false" by default)
    #  screensaver-timeout = Timeout (in seconds) until the screen blanks when the greeter is called as lockscreen
    #
    # Session:
    #  default-session = session manager to be started when none has been selected by the user and no one is set as last used (unset by default)
    #
    # Template for per-monitor configuration:
    #  [monitor: name]
    #  background = overrides default value
    #  user-background = overrides default value
    #  laptop = false|true ("false" by default) Marks monitor as laptop display
    #  transition-duration = overrides default value
    #
    [Greeter]
    background=/usr/share/backgrounds/629-Wallpaper.jpg
    #user-background=
    #theme-name=
    #icon-theme-name=
    #font-name=
    #xft-antialias=
    #xft-dpi=
    #xft-hintstyle=
    #xft-rgba=
    #indicators=
    #clock-format=
    #keyboard=
    #reader=
    #position=
    #screensaver-timeout=
    ```

4. **Crear un directorio para almacenar los fondos de pantalla (opcional pero recomendado):**

   ```bash
   sudo mkdir -pv /usr/share/backgrounds
   ```

   **Luego puedes copiar imágenes allí:**
