<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicación de los Layouts en Qtile***

- *En Qtile, los layouts determinan cómo se organizan las ventanas en la pantalla. Aquí se explica cada uno de los layouts mencionados en el fichero de configuración, incluyendo aquellos que están comentados.*

```python
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
```

---

## ***Layouts Activos***

1. **`layout.Columns`:**
   - **Descripción:** *Este layout organiza las ventanas en columnas.*
   - **Opciones:**
     - `border_focus_stack`: *Color del borde de las ventanas en foco.*
     - `border_width`: *Ancho del borde de las ventanas.*
   - **Uso:** *Ideal para mantener varias ventanas visibles y organizadas en columnas, permitiendo un fácil acceso y comparación.*

2. **`layout.Max`:**
   - **Descripción:** *Este layout maximiza una ventana a la vez.*
   - **Uso:** *Similar al modo de pantalla completa, útil cuando se desea enfocar completamente en una sola ventana sin distracciones.*

3. **`layout.MonadTall`:**
   - **Descripción:** *Organiza una ventana principal en un lado y las ventanas adicionales en el otro lado, apiladas verticalmente.*
   - **Uso:** *Excelente para configuraciones de pantalla ancha donde una ventana principal requiere más espacio.*

4. **`layout.MonadWide`:**
   - **Descripción:** *Similar a `MonadTall`, pero organiza las ventanas adicionales en pilas horizontales.*
   - **Uso:** *Adecuado para monitores más altos o configuraciones de múltiples monitores.*

---

### ***Layouts Comentados***

*Estos layouts están comentados en el fichero de configuración y pueden activarse removiendo el símbolo de comentario (`#`). Aquí se explica su propósito y uso potencial:*

1. **`layout.Stack(num_stacks=2)`:**
   - **Descripción:** *Organiza las ventanas en pilas. Se pueden tener múltiples pilas de ventanas.*
   - **Uso:** *Permite una mayor flexibilidad en la organización de ventanas, ideal para usuarios que necesitan dividir el espacio de trabajo en múltiples grupos de ventanas.*

2. **`layout.Bsp()`:**
   - **Descripción:** *Utiliza un árbol binario para organizar las ventanas.*
   - **Uso:** *Proporciona una organización dinámica y flexible de ventanas, ideal para usuarios avanzados que prefieren una gestión de ventanas más personalizada.*

3. **`layout.Matrix()`:**
   - **Descripción:** *Organiza las ventanas en una cuadrícula de filas y columnas.*
   - **Uso:** *Útil para configuraciones de múltiples ventanas pequeñas, manteniendo todo visible y organizado en una cuadrícula.*

4. **`layout.RatioTile()`:**
   - **Descripción:** *Organiza las ventanas en una proporción específica.*
   - **Uso:** *Permite mantener una proporción constante entre ventanas, útil para tareas que requieren una comparación constante de contenido entre ventanas.*

5. **`layout.Tile()`:**
   - **Descripción:** *Organiza las ventanas en un patrón de baldosas.*
   - **Uso:** *Similar a `Columns`, pero con un enfoque más rígido en la organización de ventanas en un patrón de baldosas.*

6. **`layout.TreeTab()`:**
   - **Descripción:** *Organiza las ventanas en una estructura de árbol.*
   - **Uso:** *Ideal para usuarios que prefieren una vista jerárquica de sus ventanas, permitiendo una navegación rápida y estructurada entre ellas.*

7. **`layout.VerticalTile()`:**
   - **Descripción:** *Organiza las ventanas en pilas verticales.*
   - **Uso:** *Similar a `MonadTall`, pero con un enfoque en mantener las ventanas en pilas estrictamente verticales.*

8. **`layout.Zoomy()`:**
   - **Descripción:** *Proporciona un enfoque visual de zoom en las ventanas.*
   - **Uso:** *Útil para presentaciones o para enfocarse en una ventana específica mientras se mantiene la vista de las otras ventanas en segundo plano.*
