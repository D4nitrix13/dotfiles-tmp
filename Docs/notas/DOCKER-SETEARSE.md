¡Muy buena pregunta! 🚀
En `docker-compose.yml` puedes usar **expansión de variables de entorno con valores por defecto**. Esto sirve justo para lo que mencionas: buscar una variable y, si no existe, usar otra.

---

# 🔑 Sintaxis

```yaml
variable: ${NOMBRE_VAR:-valor_por_defecto}
```

- `${NOMBRE_VAR}` → busca la variable de entorno en tu host.
- `:-valor` → si no existe (o está vacía), usa el valor por defecto.

También existe:

- `${NOMBRE_VAR-default}` → usa `default` solo si no está definida (pero **sí** acepta vacío).
- `${NOMBRE_VAR:-default}` → usa `default` si no está definida **o está vacía** (más común).

---

# 🐘 Ejemplo con PostgreSQL

```yaml
version: "3.8"

services:
  db:
    image: postgres:15
    container_name: store-db
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-storeuser}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-secret123}
      POSTGRES_DB: ${POSTGRES_DB:-storedb}
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
```

### Explicación:

- Si tienes `POSTGRES_USER` en tu `.env`, lo usará.
- Si no existe, será `storeuser`.
- Lo mismo aplica para password, DB y puerto.

---

# 📂 Estructura típica

```bash
store-app/
├─ docker-compose.yml
├─ .env
├─ certs/
├─ scripts/
└─ ...
```

### `.env` ejemplo

```env
POSTGRES_USER=zeus
POSTGRES_PASSWORD=supersecure
# POSTGRES_DB se omitió, así que tomará el valor por defecto "storedb"
```

---

# 🔍 Cómo comprobar qué valor se usó

Puedes levantar con:

```bash
docker compose config
```

Eso renderiza el `docker-compose.yml` con las variables ya sustituidas, y verás qué defaults aplicaron.

---

👉 ¿Quieres que te prepare un ejemplo **doble** (uno para Postgres y otro para tu servicio FTPS) mostrando cómo en cada caso puedes fallbackear (`:-default`) para que todo quede uniforme en tu stack `store`?
