<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación y Configuración de `volumeicon`***

**Para instalar `volumeicon`, ejecuta el siguiente comando en tu terminal:**

```bash
sudo pacman -Syu volumeicon --noconfirm
```

**Después de instalarlo, puedes ejecutarlo usando:**

```bash
volumeicon &
```

**Si no ves el icono de volumen, sera por `Use Transparent Background (requires compositor)` asegúrate de hacer clic izquierdo sobre la barra de estado para abrir el menú de configuración de `volumeicon`:**

1. **Preferences**
   - **Device:** *Default*
2. **Status Icon**
   - **Icon Theme:** *White Gnome (default es el valor por defecto)*
      - [x] *Use panel-specific icons if available* 
   - **Left Mouse Button Action**
     - [ ] *Mute Volume*
     - [x] *Show Slider*
   - **Middle Mouse Button Action**
     - [x] *Open Mixer*
     - [ ] *Mute Volume*
   - **Layout Preferences**
     - [ ] *Use Horizontal Slider*
     - [x] *Show Sound Level*
     - [x] *Use Transparent Background (requires compositor)*

**Cierra la ventana de preferencias.**

---

## ***Verificación de la Configuración de `volumeicon`***

**Verifica la configuración en el fichero `volumeicon` usando:**

```bash
bat ~/.config/volumeicon/volumeicon -l ini
```

**Si estas configuraciones están en `false`, cámbialas a `true`:**

```ini
[Hotkeys]
up_enabled=false
down_enabled=false
mute_enabled=false
up=XF86AudioRaiseVolume
down=XF86AudioLowerVolume
mute=XF86AudioMute
```

**Actualiza el fichero a:**

```ini
[Alsa]
card=HD-Audio Generic
channel=Master

[Notification]
show_notification=true
notification_type=0

[StatusIcon]
stepsize=5
onclick=xterm -e 'alsamixer'
theme=White Gnome
use_panel_specific_icons=false
lmb_slider=true
mmb_mute=false
use_horizontal_slider=true
show_sound_level=false
use_transparent_background=false

[Hotkeys]
up_enabled=true
down_enabled=true
mute_enabled=true
up=XF86AudioRaiseVolume
down=XF86AudioLowerVolume
mute=XF86AudioMute
```

1. **[Alsa]:** *Esta sección configura el dispositivo de audio de Alsa que VolumeIcon utilizará. En nuestro caso, está configurado para usar el dispositivo de audio predeterminado (default).*

2. **[Notification]:** *Aquí puedes configurar si deseas que VolumeIcon muestre notificaciones y cómo deben aparecer. En nuestro caso, está configurado para mostrar notificaciones y el tipo de notificación es 0 (probablemente significa una notificación estándar).*

3. **[StatusIcon]:** *Esta sección configura cómo se ve el icono de VolumeIcon y su comportamiento. Puedes ajustar el tamaño del paso del control de volumen, qué sucede cuando haces clic en el icono, el tema del icono, entre otras opciones. También puedes ver que se han configurado las teclas de acceso rápido para subir, bajar y silenciar el volumen, utilizando los códigos de tecla `XF86AudioRaiseVolume`, `XF86AudioLowerVolume` y `XF86AudioMute` respectivamente.*

4. **[Hotkeys]:** *Esta sección configura las teclas de acceso rápido para controlar el volumen. En nuestro caso, las teclas `XF86AudioRaiseVolume`, `XF86AudioLowerVolume` y `XF86AudioMute` están habilitadas para subir, bajar y silenciar el volumen respectivamente.*

> [!WARNING]
> *Si `volumeicon` no funciona en tu laptop seguramente sera debido a problemas con los atajos de teclado si la salida de `volumeicon &` es la siguiente probablemente sea eso de problemas con el atajo del teclado*

```bash
volumeicon &
[2] 11445
** (volumeicon:11445): WARNING **: 11:02:43.475: Binding 'XF86AudioRaiseVolume' failed!
Failed to bind XF86AudioRaiseVolume

** (volumeicon:11445): WARNING **: 11:02:43.475: Binding 'XF86AudioLowerVolume' failed!
Failed to bind XF86AudioLowerVolume

** (volumeicon:11445): WARNING **: 11:02:43.475: Binding 'XF86AudioMute' failed!
Failed to bind XF86AudioMute
```

### ***Nota***

> [!NOTE]
> *Si experimentas problemas con la configuración de `volumeicon` en una laptop y los atajos de teclado no funcionan correctamente, puede ser necesario revisar la configuración de tu sistema para asegurar que los atajos de volumen estén correctamente mapeados y no haya conflictos con otras aplicaciones o configuraciones*
