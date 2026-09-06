<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de Temas e Iconos GTK***

---

## ***Crear y Configurar `gtkrc-2.0` para GTK2***

1. **Crear el fichero `gtkrc-2.0` en el directorio `home` si no existe:**

    ```bash
    touch ~/gtkrc-2.0
    ```

2. **Agregar el siguiente contenido al fichero `gtkrc-2.0`:**

    ```ini
    # Autor: Daniel Benjamin Perez Morales
    # GitHub: https://github.com/D4nitrix13
    # Gitlab: https://gitlab.com/D4nitrix13
    # Correo electrónico: danielperezdev@proton.me

    gtk-theme-name="Material-Black-Blueberry"
    gtk-icon-theme-name="Material-Black-Blueberry-Suru"
    gtk-font-name="Noto Sans 11"
    gtk-cursor-theme-name="Breeze_Default"
    gtk-cursor-theme-size=0
    gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
    gtk-toolbar-icon-size=GTK_ICON_SIZE_SMALL_TOOLBAR
    gtk-button-images=0
    gtk-menu-images=0
    gtk-enable-event-sounds=0
    gtk-enable-input-feedback-sounds=0
    gtk-xft-antialias=1
    gtk-xft-hinting=1
    gtk-xft-hintstyle="hintslight"
    gtk-xft-rgba="rgb"
    ```

3. **Para cambiar el tema, modifica el contenido de las siguientes líneas:**

    ```ini
    gtk-theme-name="Material-Black-Blueberry"
    gtk-icon-theme-name="Material-Black-Blueberry-Suru"
    ```

---

### ***Crear y Configurar `settings.ini` para GTK3***

1. **Crear el fichero `settings.ini` en el directorio `~/.config/gtk-3.0` si no existe:**

    ```bash
    touch ~/.config/gtk-3.0/settings.ini
    ```

2. **Agregar el siguiente contenido al fichero `settings.ini`:**

    ```ini
    # Autor: Daniel Benjamin Perez Morales
    # GitHub: https://github.com/D4nitrix13
    # Gitlab: https://gitlab.com/D4nitrix13
    # Correo electrónico: danielperezdev@proton.me

    [Settings]
    gtk-theme-name=Material-Black-Blueberry
    gtk-icon-theme-name=Material-Black-Blueberry-Suru
    gtk-font-name=Noto Sans 11
    gtk-cursor-theme-name=Breeze_Default
    gtk-cursor-theme-size=0
    gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
    gtk-toolbar-icon-size=GTK_ICON_SIZE_SMALL_TOOLBAR
    gtk-button-images=0
    gtk-menu-images=0
    gtk-enable-event-sounds=0
    gtk-enable-input-feedback-sounds=0
    gtk-xft-antialias=1
    gtk-xft-hinting=1
    gtk-xft-hintstyle=hintslight
    gtk-xft-rgba=rgb
    gtk-decoration-layout=menu:close
    # gtk-application-prefer-dark-theme=1
    ```

3. **Para cambiar el tema, modifica el contenido de las siguientes líneas:**

    ```ini
    gtk-theme-name=Material-Black-Blueberry
    gtk-icon-theme-name=Material-Black-Blueberry-Suru
    ```

---

### ***Aplicar Cambios***

*Para aplicar los cambios, es necesario reiniciar la sesión de Qtile:*

```bash
mod4 + ctrl + q
```
