# ***Instalación y configuración de cbatticon y las notificaciones en Arch Linux***

---

## ***Paso 1: Instalación de `cbatticon`***

1. **Actualizar e instalar `cbatticon`:**

   ```bash
   sudo pacman -Syu --noconfirm cbatticon
   ```

2. **Ejecutar `cbatticon`:**

   ```bash
   cbatticon &
   ```

   - *Añadimos esto al fichero `~/.config/qtile/autostart.sh`*

   ```bash
   # systray battery icon
   cbatticon -u 5 &
   ```

   **Fichero `autostart.sh`:**

   ```bash
   #!/bin/sh

   # Autor: Daniel Benjamin Perez Morales
   # GitHub: https://github.com/D4nitrix13
   # Gitlab: https://gitlab.com/D4nitrix13
   # Correo electrónico: danielperezdev@proton.me 

   # systray battery icon
   cbatticon -u 5 &

   # Iniciar el icono de volumen en la bandeja del sistema
   # systray volume
   volumeicon &
   ```

   - *Si ves el mensaje "¡No se ha encontrado ninguna batería ni fuente de alimentación!", significa que `cbatticon` no detecta una batería conectada o fuentes de alimentación en tu sistema.*

---

### ***Paso 2: Configuración de Notificaciones***

1. **Instalar dependencias para notificaciones:**

   ```bash
   sudo pacman -Syu --noconfirm notification-daemon libnotify
   ```

   - *Esto instalará `notification-daemon` para gestionar las notificaciones y `libnotify` para interactuar con él.*

2. **Configurar el servicio de notificaciones:**

   **Abre el fichero de servicio de D-Bus para `org.freedesktop.Notifications`:**

   ```bash
   sudo nano /usr/share/dbus-1/services/org.freedesktop.Notifications.service
   ```

   **Agrega el siguiente contenido al fichero:**

   ```ini
   # Autor: Daniel Benjamin Perez Morales
   # GitHub: https://github.com/D4nitrix13
   # Gitlab: https://gitlab.com/D4nitrix13
   # Correo electrónico: danielperezdev@proton.me 

   [D-BUS Service]
   Name=org.freedesktop.Notifications
   Exec=/usr/lib/notification-daemon-1.0/notification-daemon
   ```

   - *Guarda y cierra el fichero.*

---

### ***Paso 3: Probar las notificaciones***

1. **Enviar una notificación de prueba:**

   ```bash
   notify-send "Hello $USER" "This is a test notification."
   ```

   - *Deberías ver una notificación emergente en tu escritorio.*

---

### ***Paso 4: Reiniciar Qtile si las notificaciones no aparecen***

> [!WARNING]
> **Si las notificaciones no aparecen después de configurar todo correctamente, reinicia tu sesión en Qtile para aplicar los cambios:**

```bash
mod4 + ctrl + q
```

---

### ***Resumen***

- *Instalaste `cbatticon` para monitorear la batería y alimentación en tu sistema.*
- *Configuraste `notification-daemon` y `libnotify` para gestionar y mostrar notificaciones.*
- *Probaste las notificaciones usando `notify-send` y reiniciaste Qtile si no aparecían las notificaciones.*

- *Esto debería asegurarte de tener un buen funcionamiento de las notificaciones y el icono de la batería en tu entorno de Qtile en Arch Linux. Para más detalles, consulta la [documentación oficial de notificaciones de escritorio en Arch Linux](https://wiki.archlinux.org/title/Desktop_notifications "https://wiki.archlinux.org/title/Desktop_notifications").*
