<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración del Fichero Autostart y Configuración de Qtile***

---

## ***Creación del Fichero Autostart***

---

### ***Hooks en Qtile***

- *Los hooks en Qtile son puntos de enganche que permiten ejecutar código en momentos específicos durante la ejecución de Qtile. Estos hooks pueden utilizarse para realizar acciones automáticas o personalizadas en respuesta a eventos o situaciones específicas.*

- *Los hooks pueden suscribirse a varios eventos, como el inicio de Qtile (`startup_once`), la creación de una nueva ventana (`client_new`), o cuando se cambia de grupo (`group_window_add`).*

- *Al suscribirse a un hook específico, se puede proporcionar una función que se ejecutará cuando se produzca ese evento particular.*

- *Los hooks se utilizan comúnmente para realizar tareas de inicialización, configuración de aplicaciones al inicio, o para realizar acciones específicas en respuesta a eventos dentro del administrador de ventanas.*

- *La documentación oficial de Qtile proporciona una lista completa de los hooks disponibles, así como ejemplos de cómo utilizarlos en la configuración de Qtile.*

- *Los hooks en Qtile son una herramienta poderosa que permite la personalización y automatización del comportamiento del administrador de ventanas, lo que permite a los usuarios adaptar Qtile a sus necesidades específicas y automatizar tareas comunes.*

- *[hooks](https://docs.qtile.org/en/latest/manual/config/hooks.html "https://docs.qtile.org/en/latest/manual/config/hooks.html")*

- *Se crea un fichero `autostart.sh` en la carpeta de configuración de Qtile y se le otorgan permisos de ejecución.*

```bash
touch ~/.config/qtile/autostart.sh
chmod u+x ~/.config/qtile/autostart.sh
```

---

#### ***Contenido del Fichero Autostart (`autostart.sh`)***

- *El fichero `autostart.sh` se utiliza para iniciar aplicaciones automáticamente al iniciar Qtile. En este caso, se inicia `volumeicon` para mostrar el icono de volumen en la bandeja del sistema.*

```bash
#!/bin/sh

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me 

# Iniciar el icono de volumen en la bandeja del sistema
# systray volume
volumeicon &
```

---

##### ***Integración en el Fichero de Configuración de Qtile***

- *Se agrega un hook de inicio (`startup_once`) en el fichero de configuración de Qtile para ejecutar el script `autostart.sh` al iniciar Qtile.*

```python
from libqtile import bar, layout, qtile, widget, hook
from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser(path="~"), ".config", "qtile", "autostart.sh")])
```

- *Este hook se ejecutará una vez al iniciar Qtile y llamará al script `autostart.sh` para iniciar las aplicaciones especificadas.*

---

##### ***Verificación de Configuración***

- *Se verifica la configuración de Qtile mediante la inspección del fichero de registro de Qtile (`qtile.log`).*

```bash
bat ~/.local/share/qtile/qtile.log -l log
```

- *Estos pasos detallan cómo crear el fichero `autostart.sh`, configurarlo para iniciar `volumeicon` automáticamente, integrarlo en el fichero de configuración de Qtile y verificar que la configuración se haya aplicado correctamente mediante el fichero de registro de Qtile.*
