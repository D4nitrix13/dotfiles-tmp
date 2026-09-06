<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Comandos Para Listar Paquetes Instalados En Arch Linux**

*[Lista De Aplicaciones De Arch Linux](https://wiki.archlinux.org/title/List_of_applications/Utilities "https://wiki.archlinux.org/title/List_of_applications/Utilities")*

## **1. Comando: `pipx`**

**Descripción:** *`pipx` permite instalar y ejecutar aplicaciones Python aisladas en entornos virtuales.*

- **Subcomando:** *`list`*

**Descripción:** *Lista todas las aplicaciones instaladas mediante `pipx`.*

- **Opción:** *`--short`*

**Descripción:** *Muestra solo los nombres de las aplicaciones instaladas, sin detalles adicionales.*

- **Valores**

*No requiere valores adicionales.*

- **Ejemplo**

```bash
pipx list --short | awk '{print $1}'
```

**Explicación:** *Muestra solo los nombres de las aplicaciones instaladas con `pipx`, uno por línea. `awk '{print $1}'` extrae la primera columna de cada línea (el nombre del paquete).*

---

## **2. Comando: `yay`**

**Descripción:** *`yay` es un asistente de instalación de paquetes para Arch Linux compatible con AUR (Arch User Repository).*

- **Subcomando:** *`-Qq`*

**Descripción:**

- **`-Q`:** *Consulta los paquetes instalados en el sistema.*
- **`-q`:** *(quiet) Muestra solo el nombre del paquete, sin información adicional.*

- **Opción:** *`| tee ~/packages/yay/installed.txt`*

**Descripción:** *Redirige la salida al archivo `installed.txt` y la muestra al mismo tiempo por pantalla.*

- **Valores**

*No se especifican valores, ya que se listan todos los paquetes instalados.*

- **Ejemplo**

```bash
yay -Qq | tee ~/packages/yay/installed.txt
```

**Explicación:** *Lista todos los paquetes instalados mediante `yay` y guarda los nombres en el archivo `installed.txt`.*

---

### **3. Comando: `pacman`**

**Descripción:** *Gestor de paquetes de Arch Linux.*

- **Subcomando:** *`-Qq`*

**Descripción:**

- **`-Q`:** *Consulta los paquetes instalados.*
- **`-q`:** *Solo muestra el nombre del paquete.*

- **Opción:** *`| tee ~/packages/pacman/installed.txt`*

**Descripción:** *Igual que antes, redirige la salida al archivo y muestra los datos por pantalla.*

- **Valores**

*No requiere valores.*

- **Ejemplo**

```bash
pacman -Qq | tee ~/packages/pacman/installed.txt
```

**Explicación:** *Lista todos los paquetes instalados con `pacman` y guarda los nombres en `installed.txt`.*

---

### **4. Comando: `npm`**

**Descripción:** *`npm` es el gestor de paquetes para Node.js.*

- **Subcomando:** *`list`*

**Descripción:** *Lista los paquetes instalados.*

#### **Opción**

- **`-g`:** *Lista los paquetes instalados globalmente.*
- **`--depth=0`:** *Solo muestra los paquetes de nivel superior (no sus dependencias).*

#### **Comandos adicionales**

- **`tail -n +2`:** *Omite la primera línea de la salida (cabecera).*
- **`grep -iPo "[A-Za-z0-9].*$"`:** *Extrae la parte que contiene el nombre del paquete ignorando la versión.*
- **`awk -F '@' '{print $1}'`:** *Elimina la versión del paquete.*
- **`tee installed.txt`:** *Guarda la salida en el archivo.*

- **Ejemplo**

```bash
npm list -g --depth=0 | tail -n +2 | grep -iPo "[A-Za-z0-9].*$" --color=never | awk -F '@' '{print $1}' | tee ~/packages/npm/installed.txt
```

**Explicación:** *Lista los paquetes npm instalados globalmente, omite información innecesaria (como versiones),*y guarda los nombres en `installed.txt`.

---

### **5. Comando: `composer`**

**Descripción:** *`composer` es un gestor de dependencias para PHP.*

- **Subcomando:** *`global show`*

**Descripción:** *Muestra una lista de los paquetes globales instalados.*

#### **Comando adicional**

- **`awk '{print $1}'`:** *Extrae solo el nombre del paquete (primera columna).*

- **Ejemplo**

```bash
composer global show | awk '{print $1}'
```

**Explicación:** *Muestra los nombres de los paquetes PHP instalados globalmente con Composer.*

---

### **6. Comando: `cargo`**

**Descripción:** *`cargo` es el gestor de paquetes y sistema de construcción de Rust.*

- **Subcomando:** *`install --list`*

**Descripción:** *Muestra una lista de las herramientas instaladas con `cargo install`.*

- **Comandos adicionales**

- **`grep -v ":"`:** *Filtra líneas que no contienen dos puntos, eliminando información sobre versiones y rutas.*
- **`xargs`:** *Convierte múltiples entradas en una sola línea.*
- **`tr ' ' '\n'`:** *Convierte los elementos separados por espacios en líneas individuales.*
- **`tee ~/packages/cargo/installed.txt`:** *Guarda la salida en un archivo.*

- **Ejemplo**

```bash
cargo install --list | grep -v ":" | xargs | tr ' ' '\n' | tee ~/packages/cargo/installed.txt
```

**Explicación:** *Extrae los nombres de las herramientas instaladas con `cargo install` y las guarda en `~/packages/cargo/installed.txt`.*

---

## **7. Comando: `flatpak`**

**Descripción:** `flatpak` gestiona aplicaciones sandboxed en Linux.
Como algunas versiones no soportan `--format` ni `--no-headers`, este comando usa un filtro para omitir la cabecera *Application ID*.

- **Ejemplo (tu comando):**

```bash
flatpak list --app --columns=application | grep -iEv "Application ID" | tee ~/packages/flatpak/installed.txt
```

**Explicación:**

- `flatpak list --app --columns=application` → muestra la lista de App IDs
- `grep -iEv "Application ID"` → elimina la cabecera
- `tee` → guarda la salida en el archivo y la imprime en pantalla
