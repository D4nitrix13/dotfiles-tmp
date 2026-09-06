<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración De Git***

1. **Instalación de `less`:** *Puedes instalar `less` en Arch Linux ejecutando el siguiente comando en tu terminal:*

   ```bash
   sudo pacman -Syu --noconfirm less
   ```

   - **Repositorio en Arch Linux:** *[less](https://archlinux.org/packages/core/x86_64/less/ "https://archlinux.org/packages/core/x86_64/less/")*
   - **Página oficial de `less`:** *[GNU less](https://www.greenwoodsoftware.com/less/ "https://www.greenwoodsoftware.com/less/")*
   - **Repositorio en GitHub:** *[vbwagner/less](https://github.com/vbwagner/less "https://github.com/vbwagner/less")*

   - *Esto instalará `less` y debería resolver el error.*

2. **Asegurarse de que `less` esté en tu PATH:** *Después de instalar `less`, verifica que su ubicación esté incluida en tu variable de entorno `PATH`. Puedes hacer esto ejecutando `echo $PATH` y verificando si la ubicación de `less` está incluida en la salida.*

3. **Configuración de otro paginador:** **Si prefieres utilizar otro paginador en lugar de `less`, puedes configurar Git para que use otro paginador. Por ejemplo, puedes configurar Git para que use `more` ejecutando el siguiente comando:**

   ```bash
   git config --global core.pager more
   ```

   *Esto configurará `more` como el paginador predeterminado en lugar de `less`.*

---

## ***Para instalar el comando `man` en Arch Linux y acceder a las páginas de manual, sigue estos pasos:***

1. *Abre una terminal en tu sistema Arch Linux.*

2. *Actualiza la lista de paquetes ejecutando el siguiente comando:*

   ```bash
   sudo pacman -Syu
   ```

3. *Luego, instala el paquete `man-db` utilizando el siguiente comando:*

   ```bash
   sudo pacman -Syu --noconfirm man-db
   ```

   - **Repositorio en Arch Linux:** *[man-db](https://archlinux.org/packages/core/x86_64/man-db/ "https://archlinux.org/packages/core/x86_64/man-db/")*
   - **Página oficial de `man-db`:** *[man-db](https://www.nongnu.org/man-db/ "https://www.nongnu.org/man-db/")*
   - **Repositorio en GitHub:** *[man-db/main](https://github.com/giraldeau/man-db-2.6.3 "https://github.com/giraldeau/man-db-2.6.3")*

- *Esto instalará `man-db`, que incluye el comando `man` y otras utilidades relacionadas. Una vez completada la instalación, deberías poder utilizar el comando `man` para acceder a las páginas de manual en tu sistema Arch Linux sin problemas. Puedes probar ejecutando `man git` para ver la página de manual del comando Git, por ejemplo.*
