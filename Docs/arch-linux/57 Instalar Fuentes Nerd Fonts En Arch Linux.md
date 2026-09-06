<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalar fuentes Nerd Fonts en Arch Linux***

**Para instalar y listar las fuentes Nerd Fonts en Arch Linux, sigue los siguientes pasos:**

1. **Actualizar el sistema y las herramientas necesarias:**

   ```bash
   sudo pacman -Syu binutils --noconfirm
   ```

2. **Instalar fuentes específicas usando `yay`:**

   - **Ubuntu Mono Nerd Font:**

     ```bash
     yay -Syu ttf-ubuntu-mono-nerd --noconfirm
     ```

   - **Fira Code Nerd Font:**

     ```bash
     yay -Syu ttf-firacode-nerd --noconfirm
     ```

   - **Cascadia Code:**

     ```bash
     yay -Syu ttf-cascadia-code --noconfirm
     ```

   - **Victor Mono:**

     ```bash
     yay -Syu ttf-victor-mono-nerd --noconfirm
     ```

   - **Mononoki:**

     ```bash
     yay -Syu ttf-mononoki-nerd --noconfirm
     ```

   - **Agave:**

     ```bash
     yay -Syu ttf-agave-nerd --noconfirm
     ```

3. **Listar las fuentes instaladas:**

   - **Fira Code Nerd Font:**

    ```bash
    fc-list | grep -iE "firacode*"
    ```

    **Salida esperada:**

    ```bash
    fc-list | grep -iE "firacode*"
    /usr/share/fonts/TTF/FiraCodeNerdFontPropo-Bold.ttf: FiraCode Nerd Font Propo:style=Bold
    /usr/share/fonts/TTF/FiraCodeNerdFont-Bold.ttf: FiraCode Nerd Font:style=Bold
    /usr/share/fonts/TTF/FiraCodeNerdFont-Light.ttf: FiraCode Nerd Font,FiraCode Nerd Font Light:style=Light,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontPropo-SemiBold.ttf: FiraCode Nerd Font Propo,FiraCode Nerd Font Propo SemBd:style=SemiBold,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontMono-Retina.ttf: FiraCode Nerd Font Mono,FiraCode Nerd Font Mono Ret:style=Retina,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontMono-Regular.ttf: FiraCode Nerd Font Mono:style=Regular
    /usr/share/fonts/TTF/FiraCodeNerdFont-Medium.ttf: FiraCode Nerd Font,FiraCode Nerd Font Med:style=Medium,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFont-Retina.ttf: FiraCode Nerd Font,FiraCode Nerd Font Ret:style=Retina,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontPropo-Retina.ttf: FiraCode Nerd Font Propo,FiraCode Nerd Font Propo Ret:style=Retina,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontPropo-Light.ttf: FiraCode Nerd Font Propo,FiraCode Nerd Font Propo Light:style=Light,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFont-SemiBold.ttf: FiraCode Nerd Font,FiraCode Nerd Font SemBd:style=SemiBold,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontMono-Bold.ttf: FiraCode Nerd Font Mono:style=Bold
    /usr/share/fonts/TTF/FiraCodeNerdFontMono-SemiBold.ttf: FiraCode Nerd Font Mono,FiraCode Nerd Font Mono SemBd:style=SemiBold,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontMono-Light.ttf: FiraCode Nerd Font Mono,FiraCode Nerd Font Mono Light:style=Light,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontMono-Medium.ttf: FiraCode Nerd Font Mono,FiraCode Nerd Font Mono Med:style=Medium,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFont-Regular.ttf: FiraCode Nerd Font:style=Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontPropo-Medium.ttf: FiraCode Nerd Font Propo,FiraCode Nerd Font Propo Med:style=Medium,Regular
    /usr/share/fonts/TTF/FiraCodeNerdFontPropo-Regular.ttf: FiraCode Nerd Font Propo:style=Regular
    ```

   - **Ubuntu Mono Nerd Font:**

     ```bash
     fc-list | grep -iE "ubuntu*"
     ```

     **Salida esperada:**

    ```bash
    fc-list | grep -iE "ubuntu*"
    /usr/share/fonts/TTF/UbuntuMonoNerdFontMono-Bold.ttf: UbuntuMono Nerd Font Mono:style=Bold
    /usr/share/fonts/TTF/UbuntuMonoNerdFont-Regular.ttf: UbuntuMono Nerd Font:style=Regular
    /usr/share/fonts/TTF/UbuntuMonoNerdFontPropo-Italic.ttf: UbuntuMono Nerd Font Propo:style=Italic
    /usr/share/fonts/TTF/UbuntuMonoNerdFontMono-Regular.ttf: UbuntuMono Nerd Font Mono:style=Regular
    /usr/share/fonts/TTF/UbuntuMonoNerdFont-Italic.ttf: UbuntuMono Nerd Font:style=Italic
    /usr/share/fonts/TTF/UbuntuMonoNerdFontMono-Italic.ttf: UbuntuMono Nerd Font Mono:style=Italic
    /usr/share/fonts/TTF/UbuntuMonoNerdFontPropo-Bold.ttf: UbuntuMono Nerd Font Propo:style=Bold
    /usr/share/fonts/TTF/UbuntuMonoNerdFont-BoldItalic.ttf: UbuntuMono Nerd Font:style=Bold Italic
    /usr/share/fonts/TTF/UbuntuMonoNerdFont-Bold.ttf: UbuntuMono Nerd Font:style=Bold
    /usr/share/fonts/TTF/UbuntuMonoNerdFontPropo-BoldItalic.ttf: UbuntuMono Nerd Font Propo:style=Bold Italic
    /usr/share/fonts/TTF/UbuntuMonoNerdFontPropo-Regular.ttf: UbuntuMono Nerd Font Propo:style=Regular
    /usr/share/fonts/TTF/UbuntuMonoNerdFontMono-BoldItalic.ttf: UbuntuMono Nerd Font Mono:style=Bold Italic
    ```

   - **Cascadia Code:**

    ```bash
    fc-list | grep -iE "cascadia*"
    ```

    **Salida esperada:**

    ```bash
    fc-list | grep -iE "cascadia*"
    /usr/share/fonts/TTF/CascadiaMonoNFItalic.ttf: Cascadia Mono NF:style=Light Italic
    /usr/share/fonts/TTF/CascadiaCodeNF.ttf: Cascadia Code NF:style=Bold
    /usr/share/fonts/TTF/CascadiaCodePL.ttf: Cascadia Code PL:style=Bold
    /usr/share/fonts/TTF/CascadiaCode.ttf: Cascadia Code:style=ExtraLight
    /usr/share/fonts/TTF/CascadiaCodePL.ttf: Cascadia Code PL:style=Regular
    /usr/share/fonts/TTF/CascadiaMonoItalic.ttf: Cascadia Mono:style=SemiLight Italic
    /usr/share/fonts/TTF/CascadiaMonoPLItalic.ttf: Cascadia Mono PL
    /usr/share/fonts/TTF/CascadiaMonoNF.ttf: Cascadia Mono NF:style=ExtraLight
    /usr/share/fonts/TTF/CascadiaMono.ttf: Cascadia Mono:style=Bold
    /usr/share/fonts/TTF/CascadiaCodePLItalic.ttf: Cascadia Code PL:style=Italic
    /usr/share/fonts/TTF/CascadiaCodeNFItalic.ttf: Cascadia Code NF:style=SemiLight Italic
    /usr/share/fonts/TTF/CascadiaCodeNF.ttf: Cascadia Code NF:style=Regular
    /usr/share/fonts/TTF/CascadiaCodePLItalic.ttf: Cascadia Code PL:style=SemiBold Italic
    /usr/share/fonts/TTF/CascadiaCodePL.ttf: Cascadia Code PL:style=SemiLight
    /usr/share/fonts/TTF/CascadiaCodeNF.ttf: Cascadia Code NF:style=Light
    /usr/share/fonts/TTF/CascadiaMonoPLItalic.ttf: Cascadia Mono PL:style=Light Italic
    /usr/share/fonts/TTF/CascadiaMonoNF.ttf: Cascadia Mono NF:style=Light
    /usr/share/fonts/TTF/CascadiaCodePL.ttf: Cascadia Code PL:style=SemiBold
    /usr/share/fonts/TTF/CascadiaMonoPL.ttf: Cascadia Mono PL:style=ExtraLight
    /usr/share/fonts/TTF/CascadiaMonoPLItalic.ttf: Cascadia Mono PL:style=SemiLight Italic
    /usr/share/fonts/TTF/CascadiaMonoPLItalic.ttf: Cascadia Mono PL:style=Bold Italic
    /usr/share/fonts/TTF/CascadiaMonoPL.ttf: Cascadia Mono PL:style=SemiLight
    /usr/share/fonts/TTF/CascadiaMonoItalic.ttf: Cascadia Mono:style=Light Italic
    /usr/share/fonts/TTF/CascadiaMonoNFItalic.ttf: Cascadia Mono NF:style=SemiLight Italic
    /usr/share/fonts/TTF/CascadiaCodePL.ttf: Cascadia Code PL:style=Light
    /usr/share/fonts/TTF/CascadiaCodeNF.ttf: Cascadia Code NF:style=SemiBold
    /usr/share/fonts/TTF/CascadiaMono.ttf: Cascadia Mono:style=Light
    /usr/share/fonts/TTF/CascadiaMonoPLItalic.ttf: Cascadia Mono PL:style=ExtraLight Italic
    /usr/share/fonts/TTF/CascadiaCodeNF.ttf: Cascadia Code NF:style=SemiLight
    /usr/share/fonts/TTF/CascadiaMonoPLItalic.ttf: Cascadia Mono PL:style=Italic
    /usr/share/fonts/TTF/CascadiaCode.ttf: Cascadia Code:style=Light
    /usr/share/fonts/TTF/CascadiaMonoNFItalic.ttf: Cascadia Mono NF
    /usr/share/fonts/TTF/CascadiaMono.ttf: Cascadia Mono:style=SemiLight
    /usr/share/fonts/TTF/CascadiaMonoNF.ttf: Cascadia Mono NF:style=SemiLight
    /usr/share/fonts/TTF/CascadiaMonoPL.ttf: Cascadia Mono PL:style=Light
    /usr/share/fonts/TTF/CascadiaCode.ttf: Cascadia Code:style=SemiLight
    /usr/share/fonts/TTF/CascadiaCodeNFItalic.ttf: Cascadia Code NF:style=Bold Italic
    /usr/share/fonts/TTF/CascadiaMonoNF.ttf: Cascadia Mono NF:style=Bold
    /usr/share/fonts/TTF/CascadiaCodeNFItalic.ttf: Cascadia Code NF:style=Light Italic
    /usr/share/fonts/TTF/CascadiaCodePLItalic.ttf: Cascadia Code PL
    /usr/share/fonts/TTF/CascadiaCodePLItalic.ttf: Cascadia Code PL:style=Bold Italic
    /usr/share/fonts/TTF/CascadiaMono.ttf: Cascadia Mono:style=Regular
    /usr/share/fonts/TTF/CascadiaMonoNFItalic.ttf: Cascadia Mono NF:style=Bold Italic
    /usr/share/fonts/TTF/CascadiaMonoPL.ttf: Cascadia Mono PL:style=Bold
    /usr/share/fonts/TTF/CascadiaCodeItalic.ttf: Cascadia Code:style=Bold Italic
    /usr/share/fonts/TTF/CascadiaCodeNF.ttf: Cascadia Code NF:style=ExtraLight
    /usr/share/fonts/TTF/CascadiaMonoPL.ttf: Cascadia Mono PL:style=SemiBold
    /usr/share/fonts/TTF/CascadiaMonoPLItalic.ttf: Cascadia Mono PL:style=SemiBold Italic
    /usr/share/fonts/TTF/CascadiaMonoNF.ttf: Cascadia Mono NF:style=SemiBold
    /usr/share/fonts/TTF/CascadiaCodeItalic.ttf: Cascadia Code:style=Light Italic
    /usr/share/fonts/TTF/CascadiaMonoNFItalic.ttf: Cascadia Mono NF:style=Italic
    /usr/share/fonts/TTF/CascadiaCodePLItalic.ttf: Cascadia Code PL:style=ExtraLight Italic
    /usr/share/fonts/TTF/CascadiaMono.ttf: Cascadia Mono:style=ExtraLight
    /usr/share/fonts/TTF/CascadiaCode.ttf: Cascadia Code:style=Bold
    /usr/share/fonts/TTF/CascadiaMonoItalic.ttf: Cascadia Mono:style=ExtraLight Italic
    /usr/share/fonts/TTF/CascadiaCodeItalic.ttf: Cascadia Code:style=SemiLight Italic
    /usr/share/fonts/TTF/CascadiaCodePL.ttf: Cascadia Code PL:style=ExtraLight
    /usr/share/fonts/TTF/CascadiaCode.ttf: Cascadia Code
    /usr/share/fonts/TTF/CascadiaMonoItalic.ttf: Cascadia Mono:style=Italic
    /usr/share/fonts/TTF/CascadiaMono.ttf: Cascadia Mono
    /usr/share/fonts/TTF/CascadiaCodeNFItalic.ttf: Cascadia Code NF:style=Italic
    /usr/share/fonts/TTF/CascadiaMonoItalic.ttf: Cascadia Mono
    /usr/share/fonts/TTF/CascadiaCodeItalic.ttf: Cascadia Code:style=SemiBold Italic
    /usr/share/fonts/TTF/CascadiaCodeNF.ttf: Cascadia Code NF
    /usr/share/fonts/TTF/CascadiaCode.ttf: Cascadia Code:style=SemiBold
    /usr/share/fonts/TTF/CascadiaMono.ttf: Cascadia Mono:style=SemiBold
    /usr/share/fonts/TTF/CascadiaCodePLItalic.ttf: Cascadia Code PL:style=SemiLight Italic
    /usr/share/fonts/TTF/CascadiaMonoItalic.ttf: Cascadia Mono:style=Bold Italic
    /usr/share/fonts/TTF/CascadiaCodePL.ttf: Cascadia Code PL
    /usr/share/fonts/TTF/CascadiaMonoPL.ttf: Cascadia Mono PL:style=Regular
    /usr/share/fonts/TTF/CascadiaCodePLItalic.ttf: Cascadia Code PL:style=Light Italic
    /usr/share/fonts/TTF/CascadiaMonoPL.ttf: Cascadia Mono PL
    /usr/share/fonts/TTF/CascadiaMonoNF.ttf: Cascadia Mono NF:style=Regular
    /usr/share/fonts/TTF/CascadiaMonoNF.ttf: Cascadia Mono NF
    /usr/share/fonts/TTF/CascadiaCodeNFItalic.ttf: Cascadia Code NF:style=SemiBold Italic
    /usr/share/fonts/TTF/CascadiaCode.ttf: Cascadia Code:style=Regular
    /usr/share/fonts/TTF/CascadiaMonoItalic.ttf: Cascadia Mono:style=SemiBold Italic
    /usr/share/fonts/TTF/CascadiaCodeItalic.ttf: Cascadia Code
    /usr/share/fonts/TTF/CascadiaCodeItalic.ttf: Cascadia Code:style=ExtraLight Italic
    /usr/share/fonts/TTF/CascadiaCodeNFItalic.ttf: Cascadia Code NF:style=ExtraLight Italic
    /usr/share/fonts/TTF/CascadiaMonoNFItalic.ttf: Cascadia Mono NF:style=SemiBold Italic
    /usr/share/fonts/TTF/CascadiaCodeItalic.ttf: Cascadia Code:style=Italic
    /usr/share/fonts/TTF/CascadiaMonoNFItalic.ttf: Cascadia Mono NF:style=ExtraLight Italic
    /usr/share/fonts/TTF/CascadiaCodeNFItalic.ttf: Cascadia Code NF
    ```

---

## ***Recursos Documentacion y Pagina Oficial Para Descargar Los Paquetes***

- *[binutils](https://archlinux.org/packages/core/x86_64/binutils/ "https://archlinux.org/packages/core/x86_64/binutils/")*

- *[ttf-ubuntu-mono-nerd](https://archlinux.org/packages/extra/any/ttf-ubuntu-mono-nerd/ "https://archlinux.org/packages/extra/any/ttf-ubuntu-mono-nerd/")*

- *[ttf-fira-code](https://archlinux.org/packages/extra/any/ttf-fira-code/ "https://archlinux.org/packages/extra/any/ttf-fira-code/")*

- *[ttf-cascadia-code](https://archlinux.org/packages/extra/any/ttf-cascadia-code/ "https://archlinux.org/packages/extra/any/ttf-cascadia-code/")*

- *[ttf-victor-mono-nerd](https://archlinux.org/packages/extra/any/ttf-victor-mono-nerd/ "https://archlinux.org/packages/extra/any/ttf-victor-mono-nerd/")*

- *[ttf-mononoki-nerd](https://archlinux.org/packages/extra/any/ttf-mononoki-nerd/ "https://archlinux.org/packages/extra/any/ttf-mononoki-nerd/")*

- *[ttf-agave-nerd](https://archlinux.org/packages/extra/any/ttf-agave-nerd/ "https://archlinux.org/packages/extra/any/ttf-agave-nerd/")*

- **Binutils** *(GNU Binary Utilities) es una colección de herramientas de desarrollo proporcionadas por el Proyecto GNU para la manipulación de ficheros binarios en sistemas Unix y Unix-like, como Linux. Estas herramientas son esenciales para la compilación, ensamblaje y enlace de programas, y se utilizan comúnmente en el desarrollo de software en entornos de programación de bajo nivel.*

- *[Fonts](https://archlinux.org/groups/x86_64/nerd-fonts/ "https://archlinux.org/groups/x86_64/nerd-fonts/")*

---

### ***¿Qué es Binutils?***

- *Binutils incluye un conjunto de herramientas que permiten trabajar con ficheros binarios y ensambladores. Es una parte fundamental del ecosistema de desarrollo de software en sistemas GNU/Linux y otros sistemas basados en Unix.*

---

### ***Herramientas Principales en Binutils***

1. **`ar` (Archiver):** *Crea, modifica y extrae de ficheros de bibliotecas (libraries).*
2. **`as` (Assembler):** *Ensambla el código fuente en lenguaje ensamblador en ficheros objeto.*
3. **`ld` (Linker):** *Enlaza ficheros objeto y bibliotecas para crear ejecutables.*
4. **`nm` (Name List):** *Lista los símbolos de los ficheros objeto.*
5. **`objcopy`:** *Copia y convierte ficheros objeto.*
6. **`objdump`:** *Muestra información detallada sobre ficheros objeto.*
7. **`ranlib`:** *Genera un índice para ficheros de bibliotecas, mejorando la velocidad de acceso.*
8. **`size`:** *Muestra el tamaño de las secciones y el tamaño total de los ficheros objeto.*
9. **`strings`:** *Extrae y muestra las cadenas de caracteres imprimibles en ficheros binarios.*
10. **`strip`:** *Elimina símbolos innecesarios de los ficheros objeto, reduciendo su tamaño.*

---

### ***Características y Usos***

- **Compilación y Enlace:** *Las herramientas de Binutils son esenciales para la compilación y el enlace de programas, convirtiendo el código fuente en ejecutables.*
- **Análisis de Binarios:** *Permiten analizar y manipular ficheros binarios, facilitando la depuración y el desarrollo.*
- **Optimización de Tamaño:** *Herramientas como `strip` ayudan a reducir el tamaño de los binarios eliminando símbolos no necesarios.*
- **Compatibilidad Multiplataforma:** *Soportan una amplia gama de arquitecturas de hardware y sistemas operativos, siendo una parte integral del ecosistema GNU.*

---

### ***Instalación de Binutils en Arch Linux***

**Para instalar Binutils en Arch Linux, puedes usar el gestor de paquetes `pacman`:**

```bash
sudo pacman -Syu binutils
```

---

### ***Ejemplos de Uso***

1. **Crear una Biblioteca Estática:**
   - *Usa `ar` para crear una biblioteca estática a partir de ficheros objeto:*

     ```bash
     ar rcs libexample.a example1.o example2.o
     ```

2. **Ensamblar y Enlazar un Programa:**
   - *Ensamblar un fichero fuente en lenguaje ensamblador:*

     ```bash
     as -o example.o example.s
     ```

   - **Enlazar el fichero objeto para crear un ejecutable:**

     ```bash
     ld -o example example.o
     ```

3. **Mostrar Información sobre un Fichero Objeto:**
   - *Usa `objdump` para mostrar el contenido y la información del fichero objeto:*

     ```bash
     objdump -d example.o
     ```

4. **Extraer Cadenas de un Binario:**
   - *Usa `strings` para mostrar las cadenas imprimibles en un binario:*

     ```bash
     strings example
     ```

5. **Reducir el Tamaño de un Binario:**

   - *Usa `strip` para eliminar símbolos no necesarios y reducir el tamaño del ejecutable:*

     ```bash
     strip --strip-unneeded example
     ```

---

### ***Conclusión***

- *Binutils es un conjunto esencial de herramientas para cualquier desarrollador que trabaje en sistemas GNU/Linux o similares. Proporciona las funcionalidades básicas necesarias para la creación, manipulación y análisis de ficheros binarios, y es un componente fundamental en el proceso de desarrollo de software de bajo nivel. Su versatilidad y compatibilidad con múltiples plataformas lo hacen indispensable en el ecosistema de desarrollo de software.*
