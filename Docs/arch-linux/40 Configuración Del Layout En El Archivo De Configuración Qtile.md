<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración del Layout en el Fichero de Configuración***

*Para activar un layout comentado, simplemente remueve el símbolo de comentario (`#`). Por ejemplo, para activar `layout.Stack`:*

```python
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.Stack(num_stacks=2),
    layout.MonadTall(),
    layout.MonadWide(),
]
```

*Esta configuración añadirá el layout `Stack` a tu lista de layouts disponibles en Qtile.*
