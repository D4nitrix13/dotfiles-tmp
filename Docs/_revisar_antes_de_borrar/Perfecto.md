Perfecto.
Ahora que **borraste la app**, **borraste el fly.toml**, **borraste el workflow**, y quieres empezar desde cero *pero importando TODO tu `.env` en un solo comando*, aquí tienes el **flujo perfecto y limpio**.

---

# ✔️ PASO 1 — Crear la app de nuevo con `fly launch`

En tu proyecto:

```bash
fly launch
```

Cuando pregunte por:

```
? Do you want to tweak these settings?
```

Pon:

```
No
```

Esto generará una nueva app con un nuevo `fly.toml`.

---

# ✔️ PASO 2 — Importar **todas** las variables del `.env` con un solo comando

Fly.io permite importar un `.env` completo de un solo golpe:

```bash
fly secrets import < .env
```

⚠️ **IMPORTANTE:**
El `.env` debe tener el formato:

```
db_username=loquesea
db_password=loquesea
db_hostname=loquesea
db_port=50013
db_name=loquesea
JWT_SECRET=loquesea
```

**Sin espacios**, **sin comillas**, **sin valores faltantes**.

---

# ✔️ PASO 3 — Revisar que los secrets sí llegaron

```bash
fly secrets list
```

Debe mostrar tus variables (sin valores).

---

# ✔️ PASO 4 — Deploy limpio

```bash
fly deploy
```

---

# ✔️ PASO 5 — Confirmar que la app levantó

```bash
fly logs
```

Debe mostrar:

```
PostgreSQL is ready.
Applying Alembic migrations...
Starting FastAPI server...
Uvicorn running on http://0.0.0.0:8000
```

---

# ✔️ NOTA IMPORTANTE PARA EVITAR EL ERROR ANTERIOR

Tu `.env` debe especificar:

```
db_port=50013
```

porque Clever Cloud NO usa `5432`.

Si ese valor está mal en tu `.env`, Fly importará el incorrecto.

---

# ✔️ Flujo completo resumido (copia/pega)

```bash
fly launch
fly secrets import < .env
fly deploy
fly logs
```

---

Si quieres, mándame tu `.env` **sin contraseñas** y te confirmo que el formato está perfecto para Fly.io.
