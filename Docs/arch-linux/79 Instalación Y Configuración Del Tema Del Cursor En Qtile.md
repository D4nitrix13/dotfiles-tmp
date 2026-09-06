<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación y Configuración del Tema del Cursor en Qtile***

---

## ***Instalación de `xcb-util-cursor`***

1. **Instalar `xcb-util-cursor`:**

    ```bash
    sudo pacman -Syu --noconfirm xcb-util-cursor
    ```

2. **¿Para qué sirve `xcb-util-cursor`?**

    - *El paquete `xcb-util-cursor` permite que el tema del cursor se mantenga constante en todo el sistema, asegurando que se vea de forma consistente en el escritorio, navegadores y cualquier otra aplicación.*

3. **Enlaces oficiales:**
   - *[Página oficial de xcb-util-cursor](https://xcb.freedesktop.org/ "https://xcb.freedesktop.org/")*
   - *[Página oficial de Arch Linux para xcb-util-cursor](https://archlinux.org/packages/extra/x86_64/xcb-util-cursor/ "https://archlinux.org/packages/extra/x86_64/xcb-util-cursor/")*
   - *[Repositorio GitHub de xcb-util-cursor](https://github.com/freedesktop/xcb-util-cursor "https://github.com/freedesktop/xcb-util-cursor")*

---

### ***Instalación del Tema de Cursor Breeze***

1. **Descargar el tema Breeze desde GNOME-Look:**
   - *[Breeze en GNOME-Look](https://www.gnome-look.org/p/999927 "https://www.gnome-look.org/p/999927")*

2. **Descargar el fichero `165371-Breeze.tar.gz`:**

    ```bash
    cd ~/Downloads
    ```

    - *Asegúrate de que el fichero descargado esté en el directorio `Downloads`.*

3. **Descomprimir el fichero:**

    ```bash
    tar -xzvf 165371-Breeze.tar.tar
    ```

4. **Verificar el contenido del directorio descomprimido:**

    ```bash
    lsd Breeze/
     cursors   index.theme
    ```

    - *Deberías ver los directorios `cursors` y el fichero `index.theme`.*

5. **Mover el tema descomprimido a `/usr/share/icons/`:**

    ```bash
    sudo mv Breeze/ /usr/share/icons/
    ```

6. **Modificar el fichero `/usr/share/icons/default/index.theme` para usar el tema Breeze:**

    ```bash
    sudo nano /usr/share/icons/default/index.theme
    ```

    **Cambia el contenido a:**

    ```ini
    # Autor: Daniel Benjamin Perez Morales
    # GitHub: https://github.com/D4nitrix13
    # Gitlab: https://gitlab.com/D4nitrix13
    # Correo electrónico: danielperezdev@proton.me

    [Icon Theme]
    Inherits=Breeze
    ```

---

### ***Configuración del Tema de Cursor en Arch Linux***

1. **Modificar el fichero `~/.config/gtk-3.0/settings.ini`:**

    ```bash
    nano ~/.config/gtk-3.0/settings.ini
    ```

    Asegúrate de que contenga:

    ```ini
    # Autor: Daniel Benjamin Perez Morales
    # GitHub: https://github.com/D4nitrix13
    # Gitlab: https://gitlab.com/D4nitrix13
    # Correo electrónico: danielperezdev@proton.me

    [Settings]
    gtk-theme-name=Material-Black-Blueberry
    gtk-icon-theme-name=Material-Black-Blueberry-Suru
    gtk-font-name=Noto Sans 11
    gtk-cursor-theme-name=Breeze
    gtk-cursor-theme-size=0
    gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
    gtk-toolbar-icon-size=GTK_ICON_SIZE_SMALL_TOOLBAR
    gtk-button-images=0
    gtk-menu-images=0
    gtk-enable-event-sounds=0
    gtk-enable-input-feedback-sounds=0
    gtk-xft-antialias=1
    gtk-xft-hinting=1
    gtk-xft-hintstyle=hintfull
    gtk-xft-rgba=rgb
    gtk-decoration-layout=menu:close
    # gtk-application-prefer-dark-theme=1
    ```

2. **Modificar el fichero `~/.gtkrc-2.0.mine` si es necesario:**

    ```bash
    touch ~/.gtkrc-2.0.mine
    nano ~/.gtkrc-2.0.mine
    ```

    **Agrega:**

    ```ini
    # Autor: Daniel Benjamin Perez Morales
    # GitHub: https://github.com/D4nitrix13
    # Gitlab: https://gitlab.com/D4nitrix13
    # Correo electrónico: danielperezdev@proton.me

    gtk-cursor-theme-name="Breeze"
    ```

---

### ***Uso de LXAppearance para la Configuración del Cursor***

1. **Instalar LXAppearance:**

    ```bash
    sudo pacman -Syu --noconfirm lxappearance
    ```

2. **Abrir LXAppearance:**

    ```bash
    lxappearance
    ```

3. **Seleccionar el Tema del Cursor:**
    - *En LXAppearance, ve a la sección de cursores, selecciona `Breeze` y haz clic en "Apply".*

---

### ***Aplicar Cambios***

*Para aplicar los cambios, es necesario reiniciar la sesión de Qtile:*

```bash
mod4 + ctrl + q
```

---

### ***Resumen***

- *Instalaste `xcb-util-cursor` para asegurar la consistencia del cursor.*
- *Descargaste y descomprimiste el tema Breeze.*
- *Moviste el tema a `/usr/share/icons/` y configuraste `default/index.theme`.*
- *Modificaste `settings.ini` y opcionalmente `~/.gtkrc-2.0.mine`.*
- *Usaste LXAppearance para aplicar el tema del cursor.*
