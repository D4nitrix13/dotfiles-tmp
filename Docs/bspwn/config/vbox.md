No, el comando `vmware-user-suid-wrapper` **es exclusivo de VMware**, y **no existe ni se necesita en VirtualBox**.

---

### 🔍 ¿Qué es `vmware-user-suid-wrapper`?

Es un binario utilizado por las **VMware Tools** para:

* Integración del portapapeles
* Autoajuste de resolución
* Sincronización del mouse
* Arrastrar y soltar entre host y VM

---

### 🖥️ ¿Y en VirtualBox?

En VirtualBox, la funcionalidad equivalente se logra con **Guest Additions**.

#### 📦 Para instalar en una VM con Linux como huésped:

```bash
sudo pacman -S virtualbox-guest-utils
```

> Y luego habilitar los servicios necesarios:

```bash
sudo systemctl enable vboxservice
sudo systemctl start vboxservice
```

#### 🧰 Funciones que proporciona `vboxservice`:

* Sincronización de hora
* Compartir portapapeles
* Autoajuste de resolución
* Carpetas compartidas
* Integración del puntero del mouse

---

### ✅ Verifica que está funcionando:

Puedes ver si el servicio está activo:

```bash
systemctl status vboxservice
```

Y si los módulos están cargados:

```bash
lsmod | grep vbox
```

---

¿Querés que te dé todos los pasos para instalar las **Guest Additions** correctamente en Arch dentro de VirtualBox?
