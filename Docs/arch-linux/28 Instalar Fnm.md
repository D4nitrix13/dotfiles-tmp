<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -- "https://github.com/D4nitrix13 --">*
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalar Fnm***

**Fast Node Manager (fnm)** *es un administrador de versiones de Node.js rápido y simple, construido en Rust. Aquí tienes una explicación detallada junto con ejemplos de comandos básicos:*

## *¿Qué es fnm y para qué sirve?*

**fnm** *permite gestionar múltiples versiones de Node.js en tu sistema. Sus principales características incluyen:*

- **Soporte multiplataforma:** *Funciona en macOS, Windows y Linux.*
- **Instalación fácil:** *Se instala rápidamente como un solo fichero ejecutable.*
- **Velocidad:** *Construido para ser rápido en la gestión de versiones.*

---

### ***Ejemplos de Comandos Básicos***

1. **Instalación de fnm:**

   - **Usando el script de instalación: `curl -fsSL https://fnm.vercel.app/install | bash`**

     ```bash
     curl -fsSL https://fnm.vercel.app/install | bash
     Checking dependencies for the installation script...
     Checking availability of curl... OK!
     Checking availability of unzip... OK!
     Downloading https://github.com/Schniz/fnm/releases/latest/download/fnm-linux.zip.. "https://github.com/Schniz/fnm/releases/latest/download/fnm-linux.zip..".
     ######################################################################## 100.0%
     Installing for Bash. Appending the following to /home/d4nitrix13/.bashrc:
 
     # fnm
     FNM_PATH="/home/d4nitrix13/.local/share/fnm"
     if [ -d "$FNM_PATH" ]; then
     export PATH="$FNM_PATH:$PATH"
     eval "`fnm env`"
     fi
 
     In order to apply the changes, open a new terminal or run the following command:
 
     source /home/d4nitrix13/.bashrc
     ```

     ```bash
     source /home/d4nitrix13/.bashrc
     ```

     ```bash
     fnm --version
     fnm 1.37.1
     ```

     - *Esto instala fnm en el directorio por defecto (`$XDG_DATA_HOME/fnm` o `$HOME/.local/share/fnm` en Linux y `$HOME/Library/Application Support/fnm` en macOS).*

     ```bash
     #
     # ~/.bashrc
     #
     
     # Autor: Daniel Benjamin Perez Morales
     # GitHub: https://github.com/DanielPerezMoralesDev1 "https://github.com/D4nitrix13
     # Correo electrónico: danielperezdev@proton.me
     
     # If not running interactively, don't do anything
     [[ $- != *i* ]] && return
     
     alias ls='ls --color=auto'
     alias grep='grep --color=auto'
     PS1='[\u@\h \W]\$ '
     
     # -------------------- Path -------------------- 
     
     # Directorio para binarios
     export PATH="/usr/bin:$PATH" 
     
     # Añadir GCC al PATH (compilador de C)
     export PATH="/usr/bin/gcc:$PATH"
     
     # Añadir Firefox al PATH (navegador web)
     export PATH="/usr/bin/firefox:$PATH"
     
     # Añadir Git al PATH (sistema de control de versiones)
     export PATH="/usr/bin/git:$PATH"
     
     # Añadir Less al PATH (visor de ficheros)
     export PATH="/usr/bin/less:$PATH"
     
     # Añadir Which al PATH (localizar un comando)
     export PATH="/usr/bin/which:$PATH"
     
     # Añadir Man al PATH (páginas del manual)
     export PATH="/usr/bin/man:$PATH"
     
     # Añadir YAY al PATH (ayudante de AUR para Arch Linux)
     export PATH="/usr/bin/yay:$PATH"
     
     # Añadir Fastfetch al PATH (herramienta de información del sistema)
     export PATH="/usr/bin/fastfetch:$PATH"
     
     # Añadir Alacritty al PATH (emulador de terminal)
     export PATH="/usr/bin/alacritty:$PATH"
     
     # Añadir LSD al PATH (comando ls moderno)
     export PATH="/usr/bin/lsd:$PATH"
     
     # Añadir Bat al PATH (clon de cat con resaltado de sintaxis)
     export PATH="/usr/bin/bat:$PATH"
     
     # Añadir Unzip al PATH (herramienta para extraer ficheros .zip)
     export PATH="/usr/bin/unzip:$PATH"
     
     # Añadir Wget al PATH (herramienta para descargar contenido de servidores web)
     export PATH="/usr/bin/wget:$PATH"
     
     # fnm
     FNM_PATH="/home/d4nitrix13/.local/share/fnm"
     if [ -d "$FNM_PATH" ]; then
       export PATH="$FNM_PATH:$PATH"
       eval "`fnm env`"
     fi
     ```

   - **Usando Homebrew (macOS/Linux):**

     ```bash
     brew install fnm
     ```

   - **Usando Winget (Windows):**

     ```bash
     winget install Schniz.fnm
     ```

   - **Usando Scoop (Windows):**

     ```bash
     scoop install fnm
     ```

   - **Usando Cargo (Linux/macOS/Windows):**

     ```bash
     cargo install fnm
     ```

2. **Configuración del entorno:**

   **Después de instalar fnm, debes configurar tu shell para usarlo:**

   - **Bash:**

     ```bash
     eval "$(fnm env --use-on-cd)"
     ```

   - **Zsh:**

     ```zsh
     eval "$(fnm env --use-on-cd)"
     ```

   - **Fish:**

     ```fish
     fnm env --use-on-cd | source
     ```

   - **PowerShell:**

     ```powershell
     fnm env --use-on-cd | Out-String | Invoke-Expression
     ```

   - **Windows Command Prompt (Batch):**

     ```batch
     FOR /f "tokens=*" %%z IN ('fnm env --use-on-cd') DO CALL %%z
     ```

---

### ***Enlaces de Ejemplo***

- **Página de GitHub de fnm:** *[GitHub - fnm](https://github.com/Schniz/fnm "https://github.com/Schniz/fnm")*
- **Documentación de Configuración:** *[Configuration](https://github.com/Schniz/fnm/blob/master/docs/configuration.md "https://github.com/Schniz/fnm/blob/master/docs/configuration.md")*
- **Comandos Disponibles:** *[Usage](https://github.com/Schniz/fnm/blob/master/docs/commands.md "https://github.com/Schniz/fnm/blob/master/docs/commands.md")*

---

### ***Nota***

- *Para más detalles sobre configuración avanzada y comandos adicionales, consulta la [documentación oficial de fnm](https://github.com/Schniz/fnm "https://github.com/Schniz/fnm").*
