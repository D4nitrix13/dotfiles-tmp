# **Arch Linux - Configuración De Dunst, Picom, Temas De Íconos Y Rofi**

─────────────────────────────────────────────────────  

1. **Configuración de [dunst](https://wiki.archlinux.org/title/Dunst "https://wiki.archlinux.org/title/Dunst")**
─────────────────────────────────────────────────────  

**Comando:** *mkdir*  
**Descripción:** *Crea un nuevo directorio. La opción -p permite crear también directorios padre si no existen, y -v muestra mensajes de confirmación por cada directorio creado.*  
**Ejemplo:**  

```bash
mkdir -pv ~/.config/dunst
```

- **mkdir:** *comando principal para crear directorios.*
- **-p:** *crea la jerarquía completa si aún no existe.*
- **-v:** *muestra información del proceso.*
- **~/.config/dunst:** *ruta destino para la configuración de dunst.*

**Comando:** *cp*  
**Descripción:** *Copia archivos o directorios.*  
**Ejemplo:**  

```bash
cp /etc/dunst/dunstrc ~/.config/dunst/dunstrc
```

- **cp:** *copia un archivo.*
- **`/etc/dunst/dunstrc`:** *archivo de configuración por defecto del sistema.*
- **`~/.config/dunst/dunstrc`:** *copia personalizada en tu configuración de usuario.*

**Propósito:** *personalizar dunst* **sin modificar los archivos del sistema.**  
**Referencia:** *`https://wiki.archlinux.org/title/Dunst`*

─────────────────────────────────────────────────────  
2. **Configuración de [picom](https://wiki.archlinux.org/title/Picom "https://wiki.archlinux.org/title/Picom")**  
─────────────────────────────────────────────────────  

**Comando:** *mkdir*  
**Descripción:** *crea el directorio de configuración de picom.*  
**Ejemplo:**  

```bash
mkdir ~/.config/picom
```

**Archivo relevante:**
`~/.config/picom/picom.conf`
*Este archivo se debe crear o copiar manualmente. Contiene las reglas de composición para transparencias, desenfoques y efectos gráficos en el entorno gráfico.*  
**Referencia:** *`https://wiki.archlinux.org/title/Picom`*

─────────────────────────────────────────────────────  
3. **Instalación de temas de íconos Dracula**  
─────────────────────────────────────────────────────  

**Comando:** *git clone*
**Descripción:** *Clona un repositorio Git de forma eficiente.*

```bash
sudo git clone https://github.com/m4thewz/dracula-icons /usr/share/icons/dracula --depth=1 --verbose --progress --ipv4
```

- **git:** *sistema de control de versiones.*
- **clone:** *subcomando para clonar repositorios.*
- **URL:** *dirección del repositorio a clonar.*
- **`/usr/share/icons/dracula`:** *destino del sistema donde se almacenan iconos.*
- **Opciones:**
  - **--depth=1:** *clona solo el último commit (más rápido, menos peso).*
  - **--verbose:** *muestra detalles de la operación.*
  - **--progress:** *muestra la barra de progreso.*
  - **--ipv4:** *fuerza el uso de IPv4.*

> [!NOTE]
> *sudo es necesario para escribir en `/usr/share/icons`.*

─────────────────────────────────────────────────────  
4. **Instalación de temas para rofi**

─────────────────────────────────────────────────────  

**Comando:** *cd $(mktemp -d)*
**Descripción:**

- **cd:** *cambia de directorio.*
- **$(mktemp -d):** *crea un directorio temporal y entra en él.*
*Esto evita contaminar tu sistema de archivos mientras pruebas temas.*

**Clonación de colecciones de temas:**

```bash
git clone --depth=1 --verbose --ipv4 --progress https://github.com/Murzchnvok/rofi-collection
git clone --depth=1 --verbose --ipv4 --progress https://github.com/newmanls/rofi-themes-collection
```

**Propósito: obtener colecciones de temas `.rasi` para usarlos en rofi.**

**Copiar un tema específico al directorio del sistema:**

```bash
sudo cp ~/utils/rofi-themes/onedark/onedark.rasi /usr/share/rofi/themes/onedark.rasi
```

- **cp:** *copia el archivo del tema.*
- **`~/utils/rofi-themes/onedark/onedark.rasi`:** *ruta de origen (debe existir previamente).*
- **`/usr/share/rofi/themes/onedark.rasi`:** *ubicación estándar donde rofi busca temas.*

**Ejecutar rofi con un tema específico:**

```bash
rofi -show run -theme rofi-collection/dracula/dracula.rasi
```

- **rofi:** *lanzador de aplicaciones.*
- **-show run:** *muestra el modo "ejecutar comando".*
- **-theme `<path>`:** *especifica el archivo `.rasi` de tema.*

─────────────────────────────────────────────────────
