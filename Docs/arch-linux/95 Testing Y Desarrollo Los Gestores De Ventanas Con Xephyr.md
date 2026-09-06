<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Testing Y Desarrollo Los Gestores De Ventanas Con Xephyr**

## **Instalación de herramientas necesarias**

* *[Xephyr](https://wiki.archlinux.org/title/Xephyr "https://wiki.archlinux.org/title/Xephyr")*

```bash
sudo pacman -Syu --noconfirm xorg-server-xephyr python-xdg firejail
```

### **Desglose línea por línea**

* *`sudo`: ejecuta el comando como superusuario (root).*
* *`pacman`: es el gestor de paquetes de Arch Linux.*
* *`-Syu`: combina tres opciones:*

  * *`-S`: sincroniza (instala o actualiza) paquetes.*
  * *`-y`: actualiza la base de datos de paquetes.*
  * *`-u`: actualiza todos los paquetes del sistema.*
* *`--noconfirm`: evita que te pregunte “¿quieres continuar?”; acepta todo por defecto.*
* *`xorg-server-xephyr`: es un servidor X anidado, una “ventana dentro de tu entorno gráfico” donde puedes probar otros entornos.*
* *`python-xdg`: biblioteca de Python para leer rutas estándar de archivos en Linux.*
* *`firejail`: herramienta de sandboxing que aísla aplicaciones por seguridad (opcional para pruebas seguras).*

---

## **Uso de Xephyr para probar entornos gráficos (WM o DE)**

```bash
Xephyr -br -ac -noreset -screen 1920x1080 :1 &>/dev/null & disown
```

### **¿Qué hace esto?**

*Ejecuta **Xephyr**, que es como un “mini escritorio dentro de tu escritorio”.*

### **Desglose de opciones**

* *`-br`: usa un fondo negro (black root).*
* *`-ac`: desactiva el control de acceso (permite que cualquier cliente gráfico use Xephyr).*
* *`-noreset`: evita que Xephyr se cierre cuando se cierre el último cliente gráfico.*
* *`-screen 1920x1080`: define el tamaño de la ventana que actuará como nueva “pantalla virtual”.*
* *`:1`: es el número del servidor de pantalla virtual (el sistema principal normalmente usa `:0`).*
* *`&>/dev/null`: redirige toda la salida (estándar y errores) a `/dev/null` para que no se vea nada en la terminal.*
* *`&`: ejecuta el proceso en segundo plano.*
* *`disown`: hace que el proceso siga corriendo incluso si cierras la terminal.*

---

### **Luego exportas la variable de entorno `DISPLAY`**

```bash
export DISPLAY=:1
```

*Esto le indica a cualquier programa gráfico que se inicie que debe ejecutarse en la pantalla virtual `:1` (la de Xephyr).*

---

### **Ejemplos de uso con gestores de ventanas**

```bash
export DISPLAY=:1
spectrwm
```

* *`spectrwm`: inicia este gestor de ventanas dentro de Xephyr.*

```bash
export DISPLAY=:1
qtile start
```

* *`qtile start`: inicia Qtile. El comando puede cambiar según la versión; a veces se usa solo `qtile`.*

---

## **Usar Openbox en Xephyr**

**Con Openbox no se puede lanzar directamente como un *entorno de sesión completo*, pero puedes lanzar componentes gráficos dentro:**

```bash
Xephyr -br -ac -noreset -screen 1920x1080 :1 &>/dev/null & disown
```

```bash
export DISPLAY=:1
alacritty &
openbox &
```

* *`alacritty &`: abre la terminal `alacritty` dentro de Xephyr (en segundo plano).*
* *`openbox &`: lanza el gestor de ventanas `openbox` dentro de esa pantalla virtual.*

---

## **Personalización de teclas (mod4 vs mod1)**

* *`Mod4`: generalmente es la **tecla Windows**.*
* *`Mod1`: generalmente es la **tecla Alt**.*

### **¿Por qué se cambia?**

*Algunos usuarios prefieren usar `Alt` como modificador principal en lugar de la tecla Windows, especialmente si están en un teclado sin esa tecla o prefieren otra ergonomía.*
