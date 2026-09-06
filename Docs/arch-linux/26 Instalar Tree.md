<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalar `tree`***

- **Para instalar `tree` en Arch Linux, utiliza el gestor de paquetes `pacman`, el administrador de paquetes por defecto en Arch Linux. Sigue estos pasos desde la terminal:**

1. **Actualizar la base de datos de paquetes:** *Es recomendable actualizar la base de datos de paquetes antes de la instalación:*

   ```bash
   sudo pacman -Syu --noconfirm
   ```

2. **Instalar `tree`:** *Instala `tree` utilizando el siguiente comando:*

   ```bash
   sudo pacman -Syu --noconfirm tree
   ```

   - **`tree`:** *Utilidad para visualizar estructuras de directorios en forma de árbol.*
     - **Página oficial:** *No disponible*
     - **Repositorio en Arch Linux:** [tree en Arch Linux](https://archlinux.org/packages/extra/x86_64/tree/ "https://archlinux.org/packages/extra/x86_64/tree/")
     - **GitHub:** *No disponible*

3. **Verificar la instalación:** *Para confirmar que `tree` se ha instalado correctamente, verifica la versión:*

   ```bash
   tree --version
   ```

   - *Esto mostrará la versión de `tree` instalada en tu sistema, asegurando una instalación exitosa.*

4. **Uso básico:** *Utiliza `tree` para visualizar la estructura jerárquica de directorios. Por ejemplo, para ver la estructura de directorios desde tu ubicación actual en la terminal:*

   ```bash
   tree -C .
   ```

   - *Esto muestra la estructura de directorios comenzando desde el directorio actual.*

- *Con estos pasos, puedes instalar y comenzar a utilizar `tree` en tu sistema Arch Linux de manera fluida y sin necesidad de confirmación adicional del usuario.*
