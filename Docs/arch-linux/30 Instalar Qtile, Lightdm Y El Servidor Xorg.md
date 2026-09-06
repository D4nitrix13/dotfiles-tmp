<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación y configuración de Qtile***

---

## ***Instalar Qtile, LightDM y el servidor Xorg***

```bash
sudo pacman -Syu --noconfirm qtile lightdm xorg-server
```

- **`qtile`:** *El gestor de ventanas Qtile.*
  - **Página oficial:** *[Qtile](http://www.qtile.org/ "http://www.qtile.org/")*
  - **Repositorio en Arch Linux:** *[qtile en Arch Linux](https://archlinux.org/packages/extra/x86_64/qtile/ "https://archlinux.org/packages/extra/x86_64/qtile/")*
  - **GitHub:** *[qtile/qtile](https://github.com/qtile/qtile "https://github.com/qtile/qtile")*

- **`lightdm`:** *Un gestor de pantalla (display manager) ligero.*
  - **Página oficial:** *No disponible*
  - **Repositorio en Arch Linux:** *[lightdm en Arch Linux](https://archlinux.org/packages/extra/x86_64/lightdm/)*
  - **GitHub:** *[canonical/lightdm](https://github.com/canonical/lightdm)*

- **`xorg-server`:** *El servidor de ventanas Xorg.*
  - **Página oficial:** *[X.Org](https://www.x.org/wiki/ "https://www.x.org/wiki/")*
  - **Repositorio en Arch Linux:** *[xorg-server en Arch Linux](https://archlinux.org/packages/extra/x86_64/xorg-server/ "https://archlinux.org/packages/extra/x86_64/xorg-server/")*
  - **GitHub:** *[XQuartz/xserver](https://github.com/XQuartz/xorg-server "https://github.com/XQuartz/xorg-server")*

- *Este comando instalará Qtile, LightDM y el servidor Xorg sin requerir confirmación del usuario, asegurando una instalación fluida y actualizada.*
