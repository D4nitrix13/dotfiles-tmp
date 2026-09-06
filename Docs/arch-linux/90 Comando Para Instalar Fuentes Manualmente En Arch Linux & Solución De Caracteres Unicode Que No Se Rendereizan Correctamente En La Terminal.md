<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Comando Para Instalar Fuentes Manualmente En Arch Linux & Solución De Caracteres Unicode Que No Se Rendereizan Correctamente En La Terminal**

---

## **1. Comando: curl**

**Descripción:** *`curl` es una herramienta para transferir datos desde o hacia un servidor usando distintos protocolos, principalmente HTTP(S).*

**Subcomando:** *No tiene subcomandos como tal, pero se configura con opciones.*

**Opciones:**

- **`-s`:** *Ejecuta en modo silencioso, sin mostrar progreso o errores.*
- **`-S`:** *Muestra errores incluso si `-s` está activo.*
- **`-L`:** *Sigue redirecciones en caso de enlaces que cambian de URL.*
- **`-O`:** *Guarda el archivo con el mismo nombre que tiene en el servidor.*
- **`-X GET`:** *Especifica el método HTTP (aquí, descarga por GET).*

**Valores:**

- *URL del archivo: Aquí se usa el enlace directo al archivo `.zip` en GitHub.*

**Ejemplo:**

```bash
curl -sSLOX GET "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/IosevkaTerm.zip"
```

**Explicación:** *Descarga silenciosamente el archivo `IosevkaTerm.zip` desde GitHub, mostrando errores si ocurren, siguiendo redirecciones, y guardándolo con su nombre original.*

---

### **2. Comando: wget**

**Descripción:** *`wget` también se usa para descargar archivos desde internet, comúnmente mediante HTTP o HTTPS.*

**Opciones:**

- **`-O IosevkaTerm.zip`:** *Guarda el archivo descargado con el nombre especificado.*

**Valores:**

- *URL:* *Enlace de descarga del archivo `.zip`.*

**Ejemplo:**

```bash
wget -O IosevkaTerm.zip "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/IosevkaTerm.zip"
```

**Explicación:** *Descarga el archivo desde la URL y lo guarda localmente como `IosevkaTerm.zip`.*

---

### **3. Comando: sudo mv**

**Descripción:** *`mv` mueve archivos de un lugar a otro.*

**Opciones:** *No se utilizan opciones aquí, solo los argumentos fuente y destino.*

**Valores:**

- **`*.ttf`:** *Todas las fuentes TrueType extraídas.*
- **`/usr/share/fonts/`:** *Directorio global del sistema para instalar fuentes.*

**Ejemplo:**

```bash
sudo mv *.ttf /usr/share/fonts/
```

**Explicación:** *Mueve todas las fuentes TTF al directorio del sistema para que estén disponibles globalmente.*

---

### **4. Comando: fc-list**

**Descripción:** *Lista las fuentes disponibles instaladas en el sistema.*

**Opciones:**

- **`| grep -iPw "IosevkaTerm"`:** *Busca fuentes que coincidan con el nombre `IosevkaTerm` ignorando mayúsculas/minúsculas y considerando coincidencias completas de palabras.*
- **`| cut -d: -f1`:** *Extrae solo la ruta del archivo de fuente.*
- **`| sudo xargs rm`:** *Elimina las fuentes encontradas.*

**Ejemplo:**

```bash
fc-list | grep -iPw "IosevkaTerm" | cut -d: -f1 | sudo xargs rm
```

**Explicación:** *Busca todas las rutas de fuentes `IosevkaTerm` instaladas y las elimina, útil para evitar conflictos antes de reinstalar.*

---

### **5. Comando: pacman**

**Descripción:** *Gestor de paquetes de Arch Linux.*

**Subcomando:**

- **`-Syu`:** *Sincroniza la base de datos de paquetes, actualiza el sistema y permite instalar paquetes nuevos.*

**Opciones:**

- **`--noconfirm`:** *Omite confirmaciones interactivas.*
- **`--needed`:** *Evita reinstalar paquetes que ya están presentes.*

**Valores:**

- **`noto-fonts-emoji`:** *Fuente necesaria para mostrar emojis correctamente.*
- **`p7zip`:** *Paquete que proporciona el comando `7z` para descomprimir archivos `.zip`, `.7z`, entre otros.*

**Ejemplos:**

```bash
sudo pacman -Syu --noconfirm noto-fonts-emoji
```

**Explicación:** *Instala la fuente `Noto Color Emoji` sin confirmar la instalación.*

```bash
sudo pacman -Syu --needed --noconfirm p7zip
```

**Explicación:** *Instala `p7zip` si no está presente, útil para poder usar el comando `7z`.*

---

### **6. Extra: mostrar emoji en terminal / LazyVim**

> [!IMPORTANT]
> *Para resolver el problema de caracteres como `\u{1f4a4}` (`💤`) que no se ven correctamente:*

1. *Asegúrate de tener **fuentes compatibles** como `Noto Color Emoji`.*
2. *Asegúrate de que tu **terminal (Alacritty, Kitty, etc.)** soporte Unicode y esté configurado para usar fuentes que incluyan emojis.*
