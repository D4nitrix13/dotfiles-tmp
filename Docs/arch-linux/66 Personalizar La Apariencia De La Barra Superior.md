<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de Qtile define la disposición de los widgets en la barra superior (`bar.Bar`) de una pantalla (`Screen`)***

- *Este fichero de configuración de Qtile define la disposición de los widgets en la barra superior (`bar.Bar`) de una pantalla (`Screen`). Aquí tienes una explicación detallada de cada sección y parámetro:*

```python
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font Mono',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block', # <- linea agregada ... no he visto su uso
                    urgent_border=["#F07178", "#F07178"], # <- linea agregada ... no he visto su uso
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#353c4a", "#353c4a"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a",],
                    disable_drag=True # <- linea agregada ... no he visto su uso
                ),
                # widget.GroupBox(),
                # widget.Prompt(),
                widget.WindowName(
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=16,
                    font='UbuntuMono Nerd Font Mono',

                ),
                widget.Systray(),

                # Nueva Confirguracion
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#0f101a","#0f101a"]
                ),

                # Nueva Confirguracion
                widget.Image(
                    filename=path.join(path.expanduser("~"), ".config", "qtile", "img", "bar2.png")
                ),
                
                # Nueva Confirguracion
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    foreground=["#0f101a","#0f101a"],
                    background=["#F07178","#F07178"] 
                ),

                # Confirguracion por (Defecto)
                # widget.CurrentLayout(),

                # Nueva Confirguracion
                widget.CurrentLayout(
                    foreground=["#0f101a","#0f101a"],
                    background=["#F07178","#F07178"],
                ),

                # Nueva Confirguracion
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#F07178","#F07178"]
                ),

                # Nueva Confirguracion
                widget.Image(
                    filename=path.join(path.expanduser("~"), ".config", "qtile", "img", "bar1.png")
                ),

                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),

                # Confirguracion por (Defecto)
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                
                # Nueva Confirguracion
                widget.TextBox(background=["#a151d3","#a151d3"], foreground=["#0f101a","#0f101a"],text=""), # nf-fa-clock_o

                # Confirguracion por (Defecto)
                # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),

                # Nueva Confirguracion
                widget.Clock(background=["#a151d3","#a151d3"], foreground=["#0f101a","#0f101a"], padding=5, format='%d/%m/%Y - %H:%M:%S '),

                # widget.QuickExit(),
            ],
            # Nueva Confirguracion 24 -> 26
            26,
            opacity = 0.95
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]
```

---

## ***Screen y Bar***

- **Screen:** *Define una pantalla en Qtile donde se colocará la barra.*
- **top:** *Especifica que la barra estará en la parte superior de la pantalla.*
- **bar.Bar:** *Define la barra con una lista de widgets que la componen y algunos parámetros adicionales.*

---

### ***Widgets***

*Los widgets son componentes individuales dentro de la barra que muestran información o permiten interactuar con el entorno de trabajo.*

1. **widget.GroupBox:**
   - *Muestra los grupos de ventanas y sus estados.*
   - **Parámetros configurados:**
     - **`foreground`:** *`["#f1ffff", "#f1ffff"]` - Colores del texto de primer plano en estado activo e inactivo.*
     - **`background`:** *`["#0f101a", "#0f101a"]` - Colores de fondo en estado activo e inactivo.*
     - **`font`:** *`'UbuntuMono Nerd Font Mono'` - Fuente utilizada para el texto.*
     - **`fontsize`:** *`19` - Tamaño de la fuente.*
     - **`margin_y`:** *`3` - Margen vertical.*
     - **`padding_y`:** *`8` - Relleno vertical.*
     - **`borderwidth`:** *`1` - Ancho del borde.*
     - **`active`:** *`["#f1ffff", "#f1ffff"]` - Colores específicos cuando el grupo está activo.*
     - **`inactive`:** *`["#f1ffff", "#f1ffff"]` - Colores específicos cuando el grupo está inactivo.*
     - **`rounded`:** *`False` - Define si los bordes son redondeados (`True` o `False`).*
     - **`highlight_method`:** *`'block'` - Método de resaltado de ventanas activas.*
     - **`urgent_alert_method`:** *`'block'` - Método de alerta para ventanas urgentes.*

2. **widget.WindowName:**
   - *Muestra el nombre de la ventana activa.*
   - **Parámetros:**
     - **`foreground`:** *`["#a151d3", "#a151d3"]` - Color del texto.*
     - **`background`:** *`["#0f101a", "#0f101a"]` - Color de fondo.*
     - **`fontsize`:** *`16` - Tamaño de la fuente.*
     - **`font`:** *`'UbuntuMono Nerd Font Mono'` - Fuente utilizada.*

3. **widget.Systray:**
   - *Muestra el área de notificación del sistema.*

4. **widget.Sep:**
   - *Un separador visual entre widgets.*
   - **Parámetros:**
     - **`linewidth`:** *`0` - Grosor de la línea.*
     - **`padding`:** *`5` - Espacio de relleno.*
     - **`background`:** *`["#0f101a", "#0f101a"]` - Color de fondo.*

5. **widget.Image:**
   - *Muestra una imagen en la barra.*
   - **Parámetro:**
     - **`filename`:** *`path.join(path.expanduser("~"), ".config", "qtile", "img", "bar2.png")` - Ruta de la imagen a mostrar.*

6. **widget.CurrentLayoutIcon:**
   - *Muestra un icono que representa el diseño actual del gestor de ventanas.*
   - **Parámetros:**
     - **`scale`:** *`0.65` - Escala del icono.*
     - **`foreground`:** *`["#0f101a", "#0f101a"]` - Color del icono.*
     - **`background`:** *`["#F07178", "#F07178"]` - Color de fondo del icono.*

7. **widget.CurrentLayout:**
   - *Muestra el nombre del diseño actual del gestor de ventanas.*
   - **Parámetros:**
     - **`foreground`:** *`["#0f101a", "#0f101a"]` - Color del texto.*
     - **`background`:** *`["#F07178", "#F07178"]` - Color de fondo.*

8. **widget.Chord:**
   - *Permite definir combinaciones de teclas para acciones específicas.*
   - **Parámetros:**
     - **`chords_colors`:** *`{"launch": ("#ff0000", "#ffffff")}` - Colores de las combinaciones de teclas.*
     - **`name_transform`:** *`lambda name: name.upper()` - Transformación opcional de nombres.*

9. **widget.TextBox:**
   - *Muestra texto estático en la barra.*
   - **Parámetros:**
     - **`background`:** *`["#a151d3", "#a151d3"]` - Color de fondo del widget.*
     - **`foreground`:** *`["#0f101a", "#0f101a"]` - Color del texto.*
     - **`text`:** *`""` - Texto a mostrar.*

10. **widget.Clock:**
    - *Muestra la fecha y hora actuales.*
    - **Parámetros:**
      - **`background`:** *`["#a151d3", "#a151d3"]` - Color de fondo del widget.*
      - **`foreground`:** *`["#0f101a", "#0f101a"]` - Color del texto.*
      - **`padding`:** *`5` - Espacio de relleno.*
      - **`format`:** *`'%d/%m/%Y - %H:%M:%S '` - Formato de la fecha y hora mostrada.*

---

### ***Otros Parámetros***

- **26:** `Número máximo de widgets que se mostrarán en la barra.`
- **opacity:** *`0.95` - Opacidad de la barra.*

---

### ***Comentarios adicionales***

- *Se han agregado líneas comentadas que muestran configuraciones por defecto o alternativas que se pueden activar dependiendo de las necesidades del usuario o del entorno (como la compatibilidad con Wayland y la tasa de sondas de arrastre en X11).*

- *Este fichero de configuración muestra cómo personalizar la apariencia y el comportamiento de Qtile mediante la configuración detallada de cada widget y la barra en general.*
