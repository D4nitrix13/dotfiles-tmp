<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación y Configuración de Temas e Iconos GTK***

---

## ***Instalar LXAppearance***

1. **Instalar LXAppearance:**

    ```bash
    sudo pacman -Syu --noconfirm lxappearance
    ```

2. **Abrir LXAppearance:**

    ```bash
    lxappearance
    ```

    - *También puedes añadir LXAppearance a tu configuración de Qtile para abrirlo fácilmente con un atajo de teclado.*

3. **Seleccionar y Aplicar Temas e Iconos:**
    - *En LXAppearance, selecciona los temas e iconos que prefieras y haz clic en "Apply" para aplicarlos.*
    - *Al hacer esto, LXAppearance actualizará automáticamente los ficheros `~/gtkrc-2.0` y `~/.config/gtk-3.0/settings.ini`.*

---

### ***Ficheros de Configuración GTK***

---

#### ***Fichero `~/gtkrc-2.0`***

```ini
# DO NOT EDIT! This file will be overwritten by LXAppearance.
# Any customization should be done in ~/.gtkrc-2.0.mine instead.

include "/home/user/.gtkrc-2.0.mine"
gtk-theme-name="Material-Black-Blueberry"
gtk-icon-theme-name="Material-Black-Blueberry-Suru"
gtk-font-name="Noto Sans 11"
gtk-cursor-theme-size=0
gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
gtk-toolbar-icon-size=GTK_ICON_SIZE_SMALL_TOOLBAR
gtk-button-images=0
gtk-menu-images=0
gtk-enable-event-sounds=0
gtk-enable-input-feedback-sounds=0
gtk-xft-antialias=1
gtk-xft-hinting=1
gtk-xft-hintstyle="hintfull"
gtk-xft-rgba="rgb"
```

---

#### ***Fichero `~/.config/gtk-3.0/settings.ini`***

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
gtk-xft-hintstyle=hintfull
gtk-xft-rgba=rgb
gtk-decoration-layout=menu:close
# gtk-application-prefer-dark-theme=1
```

---

### ***Opción Alternativa (No Recomendada)***

**No se recomienda modificar directamente los ficheros en `/usr/share/gtk-2.0/gtkrc` y `/usr/share/gtk-3.0/settings.ini`, pero si decides hacerlo:**

1. **Crear los ficheros si no existen:**

    ```bash
    sudo touch /usr/share/gtk-2.0/gtkrc /usr/share/gtk-3.0/settings.ini
    ```

2. **Agregar el contenido correspondiente:**

    - **Fichero `/usr/share/gtk-2.0/gtkrc`:**

        ```ini
        gtk-icon-theme-name = "Adwaita"
        gtk-theme-name = "Adwaita"
        gtk-font-name = "Cantarell 11"
        ```

    - **Fichero `/usr/share/gtk-3.0/settings.ini`:**

        ```ini
        [Settings]
        gtk-icon-theme-name = Adwaita
        gtk-theme-name = Adwaita
        gtk-font-name = Cantarell 11
        ```

### ***Aplicar Cambios***

**Para aplicar los cambios, es necesario reiniciar la sesión de Qtile:**

```bash
mod4 + ctrl + q
```
