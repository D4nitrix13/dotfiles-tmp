<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Clonar El Repositorio De Yay Desde Aur E Instalar***

**Para clonar el repositorio de YAY desde el Arch User Repository (AUR), utiliza el siguiente comando:**

```bash
git clone https://aur.archlinux.org/yay-git.git
```

- **`git clone`:** *Comando utilizado para clonar repositorios de Git.*
- **URL del repositorio en AUR:** *[yay-git en AUR](https://aur.archlinux.org/yay-git.git "https://aur.archlinux.org/yay-git.git")*

- *Este comando clonará el repositorio de YAY desde el AUR, permitiéndote instalar y gestionar paquetes desde el Arch User Repository en Arch Linux. Puedes obtener más información sobre Arch Linux en su [página oficial](https://www.archlinux.org/).*

---

## ***Comando en sistemas Arch Linux para instalar YAY desde el Arch User Repository (AUR). Aquí está desglosado paso a paso***

```bash
git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
```

```bash
git clone https://aur.archlinux.org/yay.git 
cd yay
makepkg -si
```

1. **`sudo pacman -S --needed git base-devel`**:
   - `sudo`: *Ejecuta el comando con privilegios de superusuario.*
   - `pacman -S`: *Comando de pacman para instalar paquetes.*
   - `--needed`: *Instala solo los paquetes que no están ya instalados.*
   - `git base-devel`: *Instala los paquetes `git` y `base-devel`.*
     - `git`: *Herramienta de control de versiones necesaria para clonar repositorios desde el AUR.*
     - `base-devel`: *Grupo de paquetes esenciales para compilar e instalar software en Arch Linux, que incluye herramientas como `gcc` y `make`.*

2. **`git clone https://aur.archlinux.org/yay.git`**:
   - `git clone`: *Clona el repositorio de `yay.git` desde el Arch User Repository (AUR) hacia tu sistema local.*
   - `https://aur.archlinux.org/yay.git`: *URL del repositorio `yay` en el AUR.*

3. **`cd yay`**:
   - *Cambia al directorio recién clonado `yay`.*

4. **`makepkg -si`**:
   - `makepkg`: *Comando utilizado para compilar e instalar paquetes desde el AUR.*
   - `-s`: *Descarga e instala las dependencias necesarias para compilar el paquete.*
   - `-i`: *Instala el paquete recién compilado después de su construcción.*

**En resumen, este comando completo realiza las siguientes acciones:**

- *Actualiza el sistema y asegura que `git` y `base-devel` estén instalados.*
- *Clona el repositorio de YAY desde el AUR.*
- *Navega al directorio del repositorio clonado.*
- *Compila el paquete YAY (`makepkg`) y lo instala (`-si`).*

- *Es útil para automatizar la instalación de YAY y asegurarse de que todas las dependencias necesarias estén presentes para compilar el paquete desde el AUR en Arch Linux.*
