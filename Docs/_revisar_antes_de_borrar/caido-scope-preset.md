En Caido, cuando configuras un preset de *scope*, básicamente estás filtrando dominios/hosts para definir lo que es **in scope** (dentro del alcance) y **out of scope** (fuera del alcance). Así funciona:

---

## 🎯 ¿Qué significa cada uno?

* **In Scope**: son los hosts o dominios que Caido va a monitorear o mostrar en pestañas como Sitemap, Intercept, HTTP/WS History y Search. Por ejemplo, si marcas `*.miweb.com` como "in scope", todas las peticiones a ese dominio se incluirán ([docs.caido.io][1]).

* **Out of Scope**: son hosts excluidos, es decir, aunque Caido pueda detectarlos, no los mostrará en las vistas activas. Útil si un subdominio no es relevante y deseas ocultarlo, por ejemplo, `*.docs.miweb.com` .

---

## ¿Para qué sirve?

* **Eficiencia**: te concentras solo en lo que realmente te interesa.
* **Limpieza**: reduces el ruido en las herramientas de revisión.
* **Control**: evitas analizar accidentalmente dominios fuera del alcance.

---

## Ejemplo práctico

Imaginemos que estás auditando toda la web de `miweb.com` excepto su subdominio de documentación:

| Tipo             | Host             | Ejemplo de tráfico mostrado?                |
| ---------------- | ---------------- | ------------------------------------------- |
| **In Scope**     | `*.miweb.com`    | Se mostrará (e.g. `app.miweb.com`)          |
| **Out of Scope** | `docs.miweb.com` | Se ocultará aunque coincida con el wildcard |

Esto garantiza que todo `*.miweb.com` se filtre, excepto `docs.miweb.com`, que será ignorado ([kb.intigriti.com][2], [docs.caido.io][1]).

---

## ¿Cómo definirlo en Caido?

1. Ve a la pestaña **Scopes**.
2. Crea un nuevo preset y pon los hosts separados.
3. Paramétralos como **in** o **out** de scope.
4. Guarda y selecciona el preset en las pestañas de análisis correspondientes ([docs.caido.io][1]).

---

## 🛠️ En resumen

* **In Scope** = lo que quieres que Caido incluya.
* **Out of Scope** = lo que quieres que Caido ignore.

Esto ayuda a mantener el foco en el alcance real de tu análisis y a evitar ruido de tráfico no relevante. ¿Querés que te muestre cómo configurarlo paso a paso o ejemplos más complejos?

[1]: https://docs.caido.io/guides/scope?utm_source=chatgpt.com "Scopes - Caido | Documentation"
[2]: https://kb.intigriti.com/en/articles/5379096-in-scope-or-out-of-scope?utm_source=chatgpt.com "In-scope or out-of-scope? - Intigriti Help Center"

---

En Caido, cuando utilizás *Scope Presets*, tenés dos cosas claves:

* **In Scope** → Dominios que querés **permitir y capturar**.
* **Out of Scope** → Dominios que querés **excluir explícitamente**, aunque coincidan con alguna regla "in scope" (deny list).

---

### 🔍 ¿Qué pasa si el *Out of Scope* queda vacío?

Depende de si definiste un *preset* o dejás el scope "unset":

#### 1. En un *preset* específico:

* Si sólo agregás dominios en **In Scope** y dejás **Out of Scope** vacío:

  * Sólo los dominios especificados en "In Scope" serán considerados.
  * Todo lo demás quedará **excluido por defecto**, *aunque no esté específicamente en Out of Scope*.

Esto ocurre porque Caido interpreta que sólo querés monitorear lo que definiste como "permitido".

#### 2. Si elegís **“Unset Scope”** (sin preset activo):

* No se aplica **ningún filtro**.
* Caido mostrará **todo el tráfico proxy**, sin distinguir entre in o out.

---

### ✅ Resumen de flujo

| Configuración     | In Scope definido | Out Scope vacío | Tráfico mostrado               |
| ----------------- | ----------------- | --------------- | ------------------------------ |
| **Preset activo** | Sí                | Sí              | **Solo** tráfico de “In Scope” |
| **Unset Scope**   | N/A               | N/A             | **Todo** el tráfico proxy      |

---

### ✍️ Para ilustrar:

* Supongamos que pones `*.miweb.com` en In Scope, y no defines nada en Out.
* Con ese preset activo, **solo el tráfico hacia `*.miweb.com` será visible**.
* Todos los demás dominios, como `otrodominio.com`, **no aparecerán aunque sean solicitados**.

Si quisieras incluir todo excepto algo específico, deberías:

1. Marcar `*` como In Scope.
2. Poner en Out de Scope lo que querés excluir (e.j. `docs.miweb.com`).

---

¿Querés que te muestre cómo configurar un preset con wildcard y exclusiones, o cómo alternar entre presets con “unset scope”?
