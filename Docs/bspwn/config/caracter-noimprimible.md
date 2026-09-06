Para obtener un espacio que **no muestre ningún carácter visible** pero **ocupe anchura real**, debes usar un Unicode que sea clasificado como espacio, no un carácter de ancho cero. Aquí tienes varios que puedes usar:

---

### 📐 Espacios invisibles con anchura

| Nombre (U+####)            | Descripción                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------- |
| U+2002 (EN SPACE)          | Equivale a la mitad de la "M" del tipo de letra ([jkorpela.fi][1], [Wikipedia][2]) |
| U+2003 (EM SPACE)          | Equivale a la "M" completa del tipo de letra                                       |
| U+2004 (THREE‑PER‑EM)      | Un tercio de la "M"                                                                |
| U+2005 (FOUR‑PER‑EM)       | Un cuarto de la "M"                                                                |
| U+2006 (SIX‑PER‑EM)        | Un sexto de la "M"                                                                 |
| U+2007 (FIGURE SPACE)      | Igual de ancho que una cifra tipográfica                                           |
| U+2008 (PUNCTUATION SPACE) | Ancho como el símbolo de punto “.”                                                 |
| U+2009 (THIN SPACE)        | Aproximadamente una quinta parte de la "M"                                         |
| U+200A (HAIR SPACE)        | Muy fino, más delgado que el anterior                                              |

---

### 🧪 ¿Cómo insertarlos en tu configuración?

Para Polybar, reemplaza el contenido del módulo con uno de estos espacios:

```ini
[module/sysmenu]
type = custom/text
content = %{T2}   ; U+2002 EN SPACE
```

Para escribirlo en tu archivo, puedes:

**Usar el código con Bash + portapapeles:**

```bash
printf '\u2002' | xclip -selection clipboard
```

o con Wayland:

```bash
printf '\u2002' | wl-copy
```

Luego pégalo directamente en tu `.ini`.

---

### 🎯 ¿Cuál usar?

* Para un espacio **amplio**: `U+2003 EM SPACE`
* Para un espacio **moderado**: `U+2002 EN SPACE` o `U+2009 THIN SPACE`
* Para un espacio **muy estrecho**: `U+200A HAIR SPACE`

---

### ✅ Ejemplo final

```ini
[module/sysmenu]
type = custom/text
label = %{T2}   ; aquí hay un U+2002 (en‑space)
click-left = ~/.config/polybar/scripts/powermenu_alt
```

* `T2` usa tu fuente de íconos.
* ` ` ocupa espacio pero sin mostrar nada.

---

¿Quieres que te sugiera un script pequeño para probar y copiar cualquiera de estos espacios invisibles al portapapeles fácilmente?

[1]: https://jkorpela.fi/chars/spaces.html?utm_source=chatgpt.com "Unicode spaces - Jukka Korpela"
[2]: https://en.wikipedia.org/wiki/General_Punctuation?utm_source=chatgpt.com "General Punctuation"
