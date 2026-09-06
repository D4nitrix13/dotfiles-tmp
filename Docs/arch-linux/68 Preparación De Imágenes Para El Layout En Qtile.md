<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Preparación de Imágenes para Qtile***

1. **Crear directorio para imágenes:**
   **Para almacenar imágenes utilizadas en el layout de Qtile, primero creamos un directorio llamado `img` dentro de la configuración de Qtile:**

   ```bash
   mkdir -p /home/d4nitrix13/.config/qtile/img
   ```

2. **Colocar imagen `bar1.png`:**
   **Colocamos la imagen `bar1.png` dentro del directorio `img` recién creado. La ruta completa de la imagen es:**

   ```bash
   /home/d4nitrix13/.config/qtile/img/bar1.png
   ```

3. **Verificar la estructura del directorio Qtile:**
   **Para confirmar que la imagen se ha colocado correctamente, podemos visualizar la estructura del directorio `~/.config/qtile` usando el comando `tree`:**

   ```bash
   tree -C ~/.config/qtile/
   ```

   Resultado esperado:

   ```bash
   /home/d4nitrix13/.config/qtile/
   ├── autostart.sh
   ├── config.py
   ├── img
   │   ├── bar1.png
   │   ├── bar2.png
   │   ├── bar3.png
   │   └── bar4.png
   └── __pycache__
       ├── config.cpython-311.pyc
       └── config.cpython-312.pyc

   2 directories, 7 files
   ```

4. **Listar contenido detallado del directorio Qtile:**
   - **Además, podemos listar el contenido de `~/.config/qtile` detalladamente utilizando `lsd` para verificar los permisos y propietarios de los ficheros:**

   ```bash
   lsd ~/.config/qtile/ -l
   ```

   ```bash
   drwxr-xr-x d4nitrix13 d4nitrix13 4.0 KB Wed Jun 26 04:45:42 2024  __pycache__
   .rwxr--r-- d4nitrix13 d4nitrix13  40 B  Sun Jun  9 11:23:47 2024  autostart.sh
   .rw-r--r-- d4nitrix13 d4nitrix13  16 KB Wed Jun 26 04:45:40 2024  config.py
   drwxr-xr-x d4nitrix13 d4nitrix13 4.0 KB Wed Jun 26 04:41:48 2024  img
   ```

5. **Listar imágenes en el directorio `img`:**
   **Verificamos las imágenes específicamente dentro del directorio `img` para asegurarnos de que `bar1.png` está presente junto con otras imágenes:**

   ```bash
   lsd ~/.config/qtile/img/ -l
   ```

   ```bash
   .rw-r--r-- d4nitrix13 d4nitrix13 2.8 KB Wed Jun 26 04:41:48 2024  bar1.png
   .rw-r--r-- d4nitrix13 d4nitrix13 2.5 KB Wed Jun 26 04:41:48 2024  bar2.png
   .rw-r--r-- d4nitrix13 d4nitrix13 2.6 KB Wed Jun 26 04:41:48 2024  bar3.png
   .rw-r--r-- d4nitrix13 d4nitrix13 3.6 KB Wed Jun 26 04:41:48 2024  bar4.png
   ```

## ***Instalación de GIMP y Descarga de Imagen Adicional***

1. **Instalación de GIMP:**
   **Para editar imágenes, como descargar y manipular `bar2.png`, instalamos GIMP:**

   ```bash
   sudo pacman -Syu gimp --noconfirm
   ```

2. **Reiniciar sesión:**
   **Después de instalar paquetes como GIMP, es recomendable reiniciar la sesión para aplicar los cambios:**
   - *Presiona `Ctrl + Alt + F2` para cambiar a una consola virtual.*
   - *Inicia sesión nuevamente después de reiniciar.*

### ***Descarga de Imagen Adicional***

1. **Descargar `bar2.png`:**
   **Descargamos la imagen `bar2.png` desde la siguiente URL y la guardamos en el directorio `img`:**

   ```text
   https://import.cdn.thinkific.com/220744/bar2-200817-151001.png
   ```
