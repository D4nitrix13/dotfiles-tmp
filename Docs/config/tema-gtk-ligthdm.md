Excelente elección 😮‍💨
LightDM WebKit2 Greeter es de los más aesthetic para Qtile.

Instalalo:

```bash id="4f9sud"
sudo pacman -S lightdm-webkit2-greeter
```

Luego editá:

```bash id="abgg7d"
sudo nano /etc/lightdm/lightdm.conf
```

y en `[Seat:*]` añadí:

```ini id="zwvf2n"
greeter-session=lightdm-webkit2-greeter
```

Quedando algo así:

```ini id="v8i4zz"
[Seat:*]
greeter-session=lightdm-webkit2-greeter
session-wrapper=/etc/lightdm/Xsession
```

---

Ahora instalá temas:

```bash id="vxv5cm"
pacman -Ss webkit2-greeter
```

Los más famosos:

```bash id="g8md3s"
lightdm-webkit-theme-litarvan
lightdm-webkit-theme-aether
lightdm-webkit-theme-glorious
```

Yo te recomiendo:

```bash id="ib6m0x"
yay -S lightdm-webkit-theme-litarvan
```

porque se ve MUY bien con Qtile/Picom.

---

Después configurás el tema:

```bash id="tuh9tm"
sudo nano /etc/lightdm/lightdm-webkit2-greeter.conf
```

Buscá:

```ini id="72k3v5"
webkit_theme =
```

y poné:

```ini id="5jodr2"
webkit_theme = litarvan
```

---

Luego:

```bash id="jlwm8m"
reboot
```

y listo 🚀

---

Si querés después también podés:

- poner blur
- transparencias
- wallpapers animados
- reloj minimalista
- avatar redondo
- tema cyberpunk/minimal/macOS

porque WebKit2 permite muchísimo styling.
