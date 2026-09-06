<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de Layouts en Qtile***

- **El fichero de configuración también define los layouts disponibles. Aquí se explica para qué sirve cada uno:**

```python
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.MonadTall(),
    layout.MonadWide(),
]
```

---

## ***Layouts definidos***

- **`layout.Columns`:** *Este layout organiza las ventanas en columnas. Las ventanas pueden apilarse verticalmente dentro de cada columna. Los parámetros `border_focus_stack` y `border_width` definen el color del borde y el grosor del borde, respectivamente.*

- **`layout.Max`:** *Este layout maximiza una ventana a la vez. Es similar al comportamiento de una ventana de pantalla completa.*

- **`layout.MonadTall`:** *Este layout coloca una ventana principal en un lado de la pantalla y las ventanas adicionales en el otro lado, apiladas verticalmente. Es ideal para configuraciones de pantalla ancha.*

- **`layout.MonadWide`:** *Similar a `MonadTall`, pero las ventanas adicionales se apilan horizontalmente.*
