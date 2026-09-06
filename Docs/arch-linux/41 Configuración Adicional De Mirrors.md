<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración adicional***

---

## ***Configuración de mirrors***

**Si tienes problemas con los mirrors, puedes utilizar el generador de mirrors de Pacman para actualizar tu lista de mirrors puedes buscar en google `pacman mirrorlist generator`:**

```bash
curl "https://www.archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4" -o mirrorlist.txt
sudo cp ./mirrorlist.txt /etc/pacman.d/mirrorlist
```
