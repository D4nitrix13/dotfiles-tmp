<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación de Themes e Iconos GTK en Arch Linux***

---

## ***Página para Themes GTK***

**Para buscar y descargar temas GTK, puedes visitar la siguiente página:**

- *[Themes](https://www.gnome-look.org/browse/ "https://www.gnome-look.org/browse/")*

---

### ***Descargar y Configurar Material Black GTK Theme***

1. **Buscar en el navegador: Material Black GTK Theme**
    - *Ir a [Material-Black COLORS Complete Desktop](https://www.gnome-look.org/p/1316887 "https://www.gnome-look.org/p/1316887").*
    - *En la sección de ficheros, descarga `Material-Black-Blueberry-2.9.9-07.zip`.*

    ```bash
    lsd
     Material-Black-Blueberry-2.9.9-07.zip
    pwd
    ~/Downloads
    ```

2. **Descargar y Configurar Iconos Material Black COLORS**
    - *Ir a [Material-Black COLORS Icon-Superpack all new 'Suru-GLOW'](https://www.pling.com/p/1333360/ "https://www.pling.com/p/1333360/").*
    - *En la sección de ficheros, descarga `Material-Black-Blueberry-Suru_1.9.3.zip`.*

    ```bash
    lsd
     Material-Black-Blueberry-2.9.9-07.zip   Material-Black-Blueberry-Suru_1.9.3.zip
    pwd
    ~/Downloads
    ```

3. **Descomprimir los ficheros descargados**

    ```bash
    unzip Material-Black-Blueberry-2.9.9-07.zip
    unzip Material-Black-Blueberry-Suru_1.9.3.zip
    ```

    **Verificar el contenido descomprimido:**

    ```bash
    lsd -lA
    drwxr-xr-x d4nitrix13 d4nitrix13 4.0 KB Tue Sep 26 02:10:20 2023  Material-Black-Blueberry
    .rw-r--r-- d4nitrix13 d4nitrix13 391 KB Sun Jun 30 10:53:17 2024  Material-Black-Blueberry-2.9.9-07.zip
    drwxr-xr-x d4nitrix13 d4nitrix13 4.0 KB Tue Jul 14 06:42:36 2020  Material-Black-Blueberry-Suru
    .rw-r--r-- d4nitrix13 d4nitrix13  16 MB Sun Jun 30 10:53:23 2024  Material-Black-Blueberry-Suru_1.9.3.zip
    ```

4. **Copiar los temas e iconos a los directorios correspondientes**

    ```bash
    sudo cp -r Material-Black-Blueberry /usr/share/themes/
    sudo cp -r Material-Black-Blueberry-Suru /usr/share/icons/
    ```

5. **Borrar los ficheros ZIP descargados**

    ```bash
    rm *.zip
    ```

6. **Listar los temas e iconos instalados**

    Para listar los temas:

    ```bash
    lsd /usr/share/themes/
     Default   Emacs   Material-Black-Blueberry   Raleigh
    ```

    **Para listar los iconos:**

    ```bash
    lsd /usr/share/icons/
     Adwaita   AdwaitaLegacy   default   hicolor   Material-Black-Blueberry-Suru   visual-studio-code.png
    ```

---

### ***Aplicar Themes e Iconos***

- *Para aplicar los temas e iconos, puedes utilizar herramientas gráficas como `lxappearance` o configurar manualmente los ficheros de configuración de GTK.*
