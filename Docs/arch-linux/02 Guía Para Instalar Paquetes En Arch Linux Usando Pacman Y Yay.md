<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Guía para Instalar Paquetes en Arch Linux***

- *Esta guía explica cómo determinar si debes usar `pacman` o `yay` para instalar paquetes en Arch Linux, basado en la información del repositorio del paquete y el enlace proporcionado.*

---

## ***Criterios para elegir el gestor de paquetes***

| **Criterio**                 | **Herramienta** | **Palabra clave en la información del paquete** | **Enlace del paquete**         |
| ---------------------------- | --------------- | ----------------------------------------------- | ------------------------------ |
| *Repositorio oficial*        | *`pacman`*      | *`core`, `extra`, `community`, `multilib`*      | *`https://archlinux.org/`*     |
| *Arch User Repository (AUR)* | *`yay`*         | *`AUR`, `aur.archlinux.org`*                    | *`https://aur.archlinux.org/`* |

---

## ***Ejemplos y Comandos***

---

### ***Paquete en un repositorio oficial (usar `pacman`)***

- **Ejemplo:** *`git`*
  - **Información del paquete:** *`Repository: extra`*
  - **Comando de instalación**:

    ```bash
    sudo pacman -Syu --noconfirm git
    ```

  - **Enlace del paquete:** *[Git en Arch Linux](https://archlinux.org/packages/extra/x86_64/git/ "https://archlinux.org/packages/extra/x86_64/git/")*

---

### ***Paquete en AUR (usar `yay`)***

- **Ejemplo:** *`visual-studio-code-bin`*
  - **Información del paquete:** *`Repository: AUR`*
  - **Comando de instalación**:

    ```bash
    yay -Syu --noconfirm visual-studio-code-bin
    ```

  - **Enlace del paquete:** *[Visual Studio Code en AUR](https://aur.archlinux.org/packages/visual-studio-code-bin/ "https://aur.archlinux.org/packages/visual-studio-code-bin/")*

---

> [!TIP]
> *Usa esta guía para determinar rápidamente qué herramienta de instalación de paquetes debes utilizar según la información proporcionada en la descripción del paquete y el enlace adjunto. Verifica siempre la sección de "Repository" y el enlace correspondiente para tomar la decisión correcta entre `pacman` y `yay`.*
