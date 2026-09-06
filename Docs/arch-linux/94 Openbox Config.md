<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Openbox Config**

## **1. Modificadores en `rc.xml` de Openbox**

```xml
C = Control
S = Shift
A = Alt
W = Super (tecla Windows)
```

*Esto se refiere a los atajos de teclado (`keybinds`) que se configuran en `~/.config/openbox/rc.xml`.*
**Cada letra representa una tecla modificadora:**

* **`C`:** *Tecla Control (`Ctrl`)*
* **`S`:** *Tecla Shift*
* **`A`:** *Tecla Alt*
* **`W`:** *Tecla Super (generalmente la tecla "Windows" del teclado)*

*Estas se combinan con otras teclas para ejecutar acciones, como abrir un programa o recargar la configuración.*

**Ejemplo:**

```xml
<keybind key="W-C-R">
```

*Significa: cuando presiones **Windows + Control + R**, se ejecutará la acción indicada.*

---

### **2. Por qué no puedes usar `&&` directamente en XML**

*Openbox no interpreta comandos como lo haría Bash, entonces al poner algo como:*

```xml
<command>openbox --reconfigure && notify-send "listo"</command>
```

> [!CAUTION]
> *...el XML no entiende `&&` como Bash, y puede romperse.*

**Solución: escapar `&&` usando HTML/XML:**

```xml
<command>bash -c "openbox --reconfigure &amp;&amp; notify-send 'listo'"</command>
```

* *`&amp;` es la forma de escribir el carácter `&` en XML.*
* *`bash -c "comando1 && comando2"` ejecuta ambos comandos como lo harías en la terminal.*

---

### **3. Instalación de paquetes**

```bash
sudo pacman -Syu --noconfirm openbox tint2 lxappearance-obconf obconf-qt zenity
```

**Explicación por partes:**

* *`sudo`: ejecuta el comando como administrador (root).*
* *`pacman`: es el gestor de paquetes de Arch Linux.*
* *`-Syu`: combina tres opciones:*

  * *`-S`: instala o actualiza paquetes específicos.*
  * *`-y`: actualiza la lista de paquetes desde los repositorios.*
  * *`-u`: actualiza los paquetes instalados en el sistema.*
* *`--noconfirm`: hace que pacman no pida confirmación al instalar. Ten cuidado con esta opción.*
* *`openbox`: el gestor de ventanas.*
* *`tint2`: panel de tareas ligero (barra de tareas).*
* *`lxappearance-obconf`: herramienta para cambiar temas y apariencia.*
* *`obconf-qt`: versión Qt de obconf.*
* *`zenity`: herramienta gráfica para mostrar diálogos en scripts.*

---

### **4. Problema con `obconf`**

> *[openbox context menu entry obconf does not call obconf-qt](https://github.com/lxqt/lxqt/issues/912 "https://github.com/lxqt/lxqt/issues/912")*

**Solución temporal:**

```bash
sudo ln -s /usr/bin/obconf-qt /usr/bin/obconf
```

**Esto crea un *enlace simbólico* (`ln -s`) para que cuando se llame a `obconf`, en realidad se ejecute `obconf-qt`.**

---

### **5. Tema personalizado `Arc-Dark`**

```bash
git clone --depth=1 --verbose --ipv4 --progress https://github.com/dglava/arc-openbox
```

```bash
sudo cp arc-openbox/Arc-Dark /usr/share/themes/Arc-Dark
```

* *Los temas visuales en Openbox se configuran dentro de `~/.config/openbox/rc.xml`.*
* *Para usar el tema Arc-Dark debes asegurarte de tenerlo instalado (normalmente está en `/usr/share/themes/Arc-Dark`).*

```xml
<name>Arc-Dark</name>
```

*Puedes buscar en tu configuración con:*

```bash
grep -ri Arc-Dark ~/.config/openbox/
```

* **Salida**

```bash
/home/d4nitrix13/.config/openbox/rc.xml:    <name>Arc-Dark</name>
```

---

### **6. Cerrar sesión en Openbox**

*Openbox no tiene por defecto botones para minimizar, maximizar o cerrar sesión. Pero puedes hacer click derecho sobre el fondo del escritorio → Log Out para cerrar sesión.*
*Esto se configura en el menú (`menu.xml`).*

---

### **7. Ejemplo de keybind que recarga la configuración**

```xml
<!-- Reload Openbox configuration with Super + Ctrl + R -->
<keybind key="W-C-R">
  <action name="Execute">
    <command>bash -c "openbox --reconfigure &amp;&amp; notify-send -u normal 'Openbox' 'Configuration reloaded successfully.'" </command>
  </action>
</keybind>
```

* *`key="W-C-R"`: Tecla Windows + Control + R.*
* *`openbox --reconfigure`: recarga la configuración del archivo `rc.xml`.*
* *`notify-send`: muestra una notificación en pantalla.*
* *`-u normal`: urgencia "normal".*
