<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Configuracion De Tema Para Grub Fuente Y Personalizacion De Tamaño**

---

## **1. Determinar La Resolución De Pantalla**

```bash
xrandr | grep '*' --color=never | awk '{print $1}'
```

- **Comando principal:** *`xrandr`*
  *Proporciona información sobre las salidas de pantalla (resoluciones soportadas, activas, desconectadas, etc.).*

- **Subcomando:** *No aplica. Se usa directamente.*

- **Opciones:**
  - **`| grep '*'`:** *Filtra las resoluciones activas (marcadas con `*`).*
  - **`--color=never`:** *Desactiva el resaltado de colores en la salida.*
  - **`| awk '{print $1}'`:** *Extrae únicamente la resolución (ej. `1920x1080`).*

- **Valores:** *No requiere entrada adicional.*

- **Ejemplo práctico:**

  ```bash
  xrandr | grep '*' --color=never | awk '{print $1}'
  ```

  **Salida esperada: `1920x1080`**

  **Si se quiere obtener solo la altura (ej. 1080):**

  ```bash
  xrandr | grep '*' --color=never | awk '{print $1}' | cut -dx -f2
  ```

  **Salida esperada: `1080`**

---

## **2. Descargar Un Tema GRUB Según La Resolución**

```bash
curl -sSLOX GET "<URL>"
```

- **Comando principal:** *`curl`*
  **Herramienta de línea de comandos para transferencias de archivos desde o hacia un servidor.**

- **Subcomando:** *No aplica directamente, pero tiene múltiples opciones que modifican su comportamiento.*

- **Opciones:**
  - **`-s`:** *Silencioso. Oculta la barra de progreso.*
  - **`-S`:** *Muestra errores si ocurren (aunque esté en modo silencioso).*
  - **`-L`:** *Sigue redirecciones si las hay.*
  - **`-O`:** *Guarda el archivo con el mismo nombre que tiene en el servidor.*
  - **`-X GET`:** *Especifica que se trata de una solicitud HTTP GET.*

- **Valores:**
  - **`<URL>`:** *Enlace completo al archivo del tema. Debe estar entre comillas si incluye caracteres especiales (`&`, `?`, etc.).*

- **Ejemplo práctico:**

  **Descargar Tema Vimix 1080p:**

    ```bash
    curl -sSLOX GET "https://ocs-dl.fra1.cdn.digitaloceanspaces.com/data/files/1460753224/Vimix-1080p.tar.xz?response-content-disposition=attachment%3B%2520Vimix-1080p.tar.xz&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=RWJAQUNCHT7V2NCLZ2AL%2F20250419%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250419T182817Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=56671887e63be4159234379866cdcd32d9e87c5e9b1ad22a01e5375a1e5d5452"
    ```

  **Descargar Tema Vimix 2K:**

    ```bash
    curl -sSLOX GET "https://ocs-dl.fra1.cdn.digitaloceanspaces.com/data/files/1460753224/Vimix-2k.tar.xz?response-content-disposition=attachment%3B%2520Vimix-2k.tar.xz&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=RWJAQUNCHT7V2NCLZ2AL%2F20250419%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250419T183305Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=5981f4c755a184199542cfc9c7e630ae50bca35bfb2fed0331ec84a0b67bfb62"
    ```

  **Descargar Tema Vimix 4K:**

    ```bash
    curl -sSLOX GET "https://ocs-dl.fra1.cdn.digitaloceanspaces.com/data/files/1460753224/Vimix-4k.tar.xz?response-content-disposition=attachment%3B%2520Vimix-4k.tar.xz&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=RWJAQUNCHT7V2NCLZ2AL%2F20250419%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250419T183200Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=3259a380584e33bbdb94634ee8aa34ed585c869baa0922d40fe67bdafe03c8e6"
    ```

---

## **3. Cambiar La Fuente Del Menú GRUB**

*Foro Recomendado: [Grub Menu Font Size](https://www.baeldung.com/linux/grub-menu-font-size "https://www.baeldung.com/linux/grub-menu-font-size")*

```bash
grub-mkfont --output=/boot/grub/fonts/ubuntuMonoBoldItalic.pf2 /usr/share/fonts/TTF/UbuntuMonoNerdFontMono-BoldItalic.ttf
```

- **Comando principal:** *`grub-mkfont`*
  **Convierte fuentes TTF u OTF en formato `.pf2`, que es compatible con GRUB.**

- **Opciones:**
  - **`--output=`:** *Especifica la ruta y nombre del archivo `.pf2` de salida.*

- **Valores:**
  - **Archivo fuente `.ttf` o `.otf`:** *Debe ser una fuente existente en tu sistema.*
  - **Ruta de salida:** *Debe ser accesible por GRUB (idealmente `/boot/grub/fonts/`).*

- **Ejemplo práctico:**

  ```bash
  grub-mkfont --output=/boot/grub/fonts/ubuntuMonoBoldItalic.pf2 /usr/share/fonts/TTF/UbuntuMonoNerdFontMono-BoldItalic.ttf
  ```

---

## **4. Configurar La Fuente En GRUB**

```bash
echo "GRUB_FONT=/boot/grub/fonts/ubuntuMonoBoldItalic.pf2" | sudo tee -a /etc/default/grub
```

- **Comando principal:** *`echo`*
  **Imprime una cadena de texto.**

- **Subcomando:** *`| sudo tee -a`*
  **Añade la línea al archivo `/etc/default/grub` con privilegios de superusuario.**

- **Opciones:**
  - **`-a`:** *Agrega (append) al final del archivo, sin sobrescribir.*

- **Valores:**
  - **Ruta del archivo `.pf2` generado previamente.**

- **Ejemplo práctico:**

  ```bash
  echo "GRUB_FONT=/boot/grub/fonts/ubuntuMonoBoldItalic.pf2" | sudo tee -a /etc/default/grub
  ```

---

## **5. Regenerar El Archivo De Configuración De GRUB**

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

- **Comando principal:** *`grub-mkconfig`*
  **Genera un nuevo archivo de configuración para GRUB basado en los archivos actuales.**

- **Opciones:**
  - **`-o`:** *Indica la ubicación del archivo de salida.*

- **Valores:**
  - **`/boot/grub/grub.cfg`:** *Ruta estándar del archivo de configuración de GRUB.*

- **Ejemplo práctico:**

  ```bash
  sudo grub-mkconfig -o /boot/grub/grub.cfg
  ```

---

## **Recomendaciones De Temas GRUB**

**[Sitio Oficial De Temas GRUB](https://www.gnome-look.org/browse?cat=109&ord=rating "https://www.gnome-look.org/browse?cat=109&ord=rating")**

*Tema recomendado:* **Grub-theme-vimix**  
**[Descargar Tema Recomendado](https://www.gnome-look.org/p/1009236 "https://www.gnome-look.org/p/1009236")**

**Escoge según tu resolución (puedes descargar con `curl` como se explicó arriba):**

- *1080p → `Vimix-1080p.tar.xz`*
- *2K → `Vimix-2k.tar.xz`*
- *4K → `Vimix-4k.tar.xz`*

---

## **1. Comando: tar**

```bash
tar -xvf Vimix-1080p.tar.xz
```

### **Comando principal: tar**

*Tar (Tape ARchive) es una utilidad en sistemas UNIX/Linux para empaquetar y desempaquetar archivos y directorios. Se usa comúnmente para crear archivos comprimidos (como .tar, .tar.gz, .tar.xz) o para extraerlos.*

### **Subcomando: -xvf**

**Estos son en realidad opciones combinadas, pero se explican individualmente:**

### **Opciones**

- **-x:** *Extrae archivos desde un archivo .tar.*
- **-v:** *(Verbose) Muestra el proceso de extracción archivo por archivo en la terminal.*
- **-f:** *Especifica el nombre del archivo que se va a desempaquetar. Debe ir seguido del nombre del archivo.*

### **Valores**

- **Vimix-1080p.tar.xz:** *Es el nombre del archivo comprimido que se desea extraer. El valor cambia según la resolución:*
  - *`Vimix-1080p.tar.xz`*
  - *`Vimix-2k.tar.xz`*
  - *`Vimix-4k.tar.xz`*

### **Ejemplo práctico**

```bash
tar -xvf Vimix-2k.tar.xz
```

*Explicación: Extrae el contenido del archivo Vimix-2k.tar.xz mostrando en pantalla los archivos extraídos.*

---

## **2. Comando: cd**

```bash
cd Vimix-2k
```

### **Comando principal: cd**

*cd (change directory) permite navegar entre directorios en una terminal.*

### **Subcomando: —**

**No aplica. cd no tiene subcomandos.**

- **Opciones**

**No hay opciones típicas para cd, solo se pasa como valor el directorio de destino.**

- **Valores**

- **Vimix-2k:** *Es el nombre de la carpeta extraída, que contiene los archivos y scripts necesarios para instalar el tema GRUB correspondiente a la resolución 2k.*
  **Otros valores posibles son:**
  - *Vimix-1080p*
  - *Vimix-4k*

- **Ejemplo práctico**

```bash
cd Vimix-4k
```

*Explicación: Entra a la carpeta que contiene el tema GRUB para resolución 4K.*

---

## **3. Comando: sudo ./install.sh**

```bash
sudo ./install.sh
```

### **Comando principal: sudo**

**sudo (superuser do) permite ejecutar comandos con privilegios de superusuario.**

### **Subcomando: ./install.sh**

*Este no es un subcomando de sudo, sino un script ejecutable en el directorio actual. El punto (`.`) seguido de una barra (`/`) indica que se va a ejecutar un archivo desde el directorio actual.*

- **Opciones**

- *No hay opciones en este caso, aunque sudo puede recibir algunas como `-E`, `-u`, etc. Aquí se usa directamente para ejecutar el script con permisos de administrador.*

- **Valores**

- **./install.sh:** *Es un script de shell que contiene las instrucciones para instalar el tema Vimix en GRUB. Requiere privilegios para copiar archivos a /boot/grub/themes y modificar la configuración.*

- **Ejemplo práctico**

```bash
sudo ./install.sh
```

*Explicación: Ejecuta el script de instalación del tema GRUB como administrador.*

---

## *Flujo completo para instalar tema Vimix en resolución 1080p*

```bash
tar -xvf Vimix-1080p.tar.xz
cd Vimix-1080p
sudo ./install.sh
```

**Explicación paso a paso:**

1. *Se descomprime el archivo tar.xz del tema correspondiente a 1080p.*
2. *Se entra al directorio donde se descomprimió el tema.*
3. *Se ejecuta el script de instalación con privilegios de superusuario.*
