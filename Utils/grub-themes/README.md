# GRUB Theme Installation (Vimix)

Este repositorio contiene temas de GRUB en formato `.tar.xz` para distintas resoluciones de pantalla.

---

## Requisitos

* Sistema con **GNU GRUB instalado
* Permisos de superusuario (sudo)
* `tar` para descompresión

---

## Archivos disponibles

```bash
Vimix-1080p.tar.xz
Vimix-2k.tar.xz
Vimix-4k.tar.xz
```

Cada archivo corresponde a una resolución distinta.

---

## 1. Determinar resolución de pantalla

Antes de instalar un tema, debes conocer tu resolución.

### Método recomendado

```bash
xrandr | grep '*'
```

Ejemplo de salida:

```bash
1920x1080     60.00*
```

Resolución detectada: `1920x1080`

---

### Alternativa (solo resolución)

```bash
xrandr | awk '/\*/ {print $1}'
```

---

## 2. Elegir tema correcto

| Resolución | Tema        |
| ---------- | ----------- |
| 1920x1080  | Vimix-1080p |
| 2560x1440  | Vimix-2k    |
| 3840x2160  | Vimix-4k    |

---

## 3. Descomprimir el tema

```bash
tar -xvf Vimix-1080p.tar.xz
```

Esto generará un directorio con el contenido del tema.

---

Perfecto, entonces el README debe reflejar que la instalación se hace mediante el script `install.sh`. Te dejo la sección corregida y coherente:

---

## 4. Instalar el tema

Una vez descomprimido el archivo, entra al directorio del tema:

```bash
cd Vimix-1080p
```

Ejecuta el script de instalación con privilegios de superusuario:

```bash
sudo bash ./install.sh
```

---

## 5. Configuración automática

El script `install.sh` normalmente realiza:

* Copia de archivos a `/boot/grub/themes/`
* Configuración del tema en `/etc/default/grub`
* Aplicación de la configuración de GRUB

---

## 6. Configurar resolución de GRUB

GRUB puede usar una resolución distinta a la del sistema.

Para ver las resoluciones soportadas:

### Importante

El comando:

```bash
videoinfo
```

no se ejecuta en Linux, sino dentro de GRUB.

---

### Cómo usar `videoinfo`

1. Reiniciar el sistema
2. En el menú de GRUB, presionar `c` para abrir la consola
3. Ejecutar:

```bash
videoinfo
```

Se mostrará una lista de resoluciones soportadas, por ejemplo:

```bash
1024x768x32
1280x1024x32
1920x1080x32
```

---

### Configurar resolución

Editar:

```bash
sudo nano /etc/default/grub
```

Agregar:

```bash
GRUB_GFXMODE=1920x1080
GRUB_GFXPAYLOAD_LINUX=keep
```

---

## 7. Aplicar cambios

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

---

## 8. Reiniciar

```bash
reboot
```

---

## Verificación

Al reiniciar, el tema debería aplicarse correctamente en el menú de GRUB.

---

## Problemas comunes

### El tema no aparece

* Ruta incorrecta en `GRUB_THEME`
* `theme.txt` no existe en el directorio

Verificar:

```bash
ls /boot/grub/themes/Vimix-1080p
```

---

### Resolución incorrecta

* GRUB no soporta la resolución configurada
* Usar `videoinfo` para verificar compatibilidad

---

## Notas

* GRUB no siempre soporta resoluciones modernas completas
* Es recomendable usar resoluciones estándar como `1920x1080`
* El tema debe coincidir con la resolución para evitar distorsión
