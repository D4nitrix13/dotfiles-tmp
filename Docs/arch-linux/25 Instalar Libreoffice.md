<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalar LibreOffice***

**Para instalar LibreOffice en Arch Linux:**

1. **Actualizar la base de datos de paquetes y el sistema:**

   ```bash
   sudo pacman -Syu --noconfirm
   ```

2. **Instalar LibreOffice (versión fresca con actualizaciones regulares):**

   ```bash
   sudo pacman -Syu --noconfirm libreoffice-fresh
   ```

   - **`libreoffice-fresh`:** *Suite de oficina completa que incluye Writer, Calc, Impress, Draw, Base, Math, etc.*
     - **Página oficial:** *[LibreOffice](https://www.libreoffice.org/ "https://www.libreoffice.org/")*
     - **Repositorio en Arch Linux:** *[libreoffice-fresh en Arch Linux](https://archlinux.org/packages/extra/x86_64/libreoffice-fresh/ "https://archlinux.org/packages/extra/x86_64/libreoffice-fresh/")*
     - **GitHub:** *[LibreOffice](https://github.com/LibreOffice "https://github.com/LibreOffice")*

3. **Instalar LibreOffice (versión de soporte extendido - ESR):**

   ```bash
   sudo pacman -Syu --noconfirm libreoffice-still
   ```

- **`libreoffice-still`:** *Versión con actualizaciones menos frecuentes pero más estables.*
  - **Página oficial:** *[LibreOffice](https://www.libreoffice.org/ "https://www.libreoffice.org/")*
  - **Repositorio en Arch Linux:** *[libreoffice-still en Arch Linux](https://archlinux.org/packages/extra/x86_64/libreoffice-still/ "https://archlinux.org/packages/extra/x86_64/lib|reoffice-still/")*
  - **GitHub:** *[LibreOffice](https://github.com/LibreOffice "https://github.com/LibreOffice")*

- *Estos comandos permiten instalar LibreOffice sin necesidad de confirmación del usuario, asegurando una instalación sin interrupciones.*
