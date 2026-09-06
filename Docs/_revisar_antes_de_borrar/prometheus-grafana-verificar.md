Aquí tienes **la forma exacta, técnica y verificable** de asegurarte que **Prometheus y Grafana están funcionando correctamente** dentro de tu stack Docker.

---

# ✅ 1. Verificar Prometheus

### **A. Verificar que el contenedor está corriendo**

```bash
docker ps | grep prometheus
```

Debes ver algo como:

```
prometheus   prom/prometheus:latest   ...   Up ...
```

### **B. Probar que la UI responde**

Abre en tu navegador:

```
http://localhost:9090
```

Si carga la interfaz de Prometheus → ✔️ **Prometheus está vivo**.

### **C. Verificar que está scrapendo tus targets**

Dentro de la UI:

1. Entra a: **Status → Targets**
2. Debes ver:

* `laravel-app` → UP (si ya tienes tu endpoint `/metrics`)
* `postgres` → UP

Si alguno dice **DOWN**, el problema es:

* endpoint incorrecto
* service name o puerto mal
* `/metrics` no existe en Laravel

---

# ❗ Cómo probar Prometheus desde CLI

### **1. Hacer curl directo desde tu PC**

```bash
curl http://localhost:9090/-/ready
```

Debe responder:

```
Prometheus Server is Ready.
```

### **2. Hacer curl desde dentro del contenedor (útil para debug de redes)**

```bash
docker exec -it <prometheus_container_id> sh
curl http://app:8000/metrics
curl http://postgres-exporter:9187/metrics
```

Si responde texto de métricas → ✔️ Todo bien.

---

# ✅ 2. Verificar Grafana

### **A. Contenedor running**

```bash
docker ps | grep grafana
```

Debe aparecer:

```
grafana   grafana/grafana:latest   ...   Up ...
```

### **B. Abrir la UI**

Entra al navegador:

```
http://localhost:3000
```

Si ves el login → ✔️ Grafana está funcionando.

---

# ❗ 3. Verificar que Grafana tiene acceso a Prometheus

Una vez dentro:

1. En la izquierda → **Engranaje (Settings)**
2. **Data Sources**
3. Debes ver un datasource llamado **Prometheus**
4. Ábrelo → **Test & Save**

Si sale:

```
Data source is working
```

→ ✔️ Grafana está conectado a Prometheus.

---

# 🟦 Diagnóstico rápido paso por paso

| Componente                    | Check | Comando / URL                                      | Resultado esperado       |
| ----------------------------- | ----- | -------------------------------------------------- | ------------------------ |
| Prometheus está vivo          | ✔️     | `http://localhost:9090`                            | UI abierta               |
| Grafana está viva             | ✔️     | `http://localhost:3000`                            | UI de login abierta      |
| Exporter de Postgres funciona | ✔️     | `http://localhost:9187/metrics` (por curl interno) | Respuesta de métricas    |
| App Laravel expone `/metrics` | ✔️     | `http://localhost:8000/metrics`                    | Texto plano con métricas |
| Prometheus scrapea            | ✔️     | Prometheus → Status → Targets                      | Todos “UP”               |
| Grafana accede a Prometheus   | ✔️     | Grafana → Data Source → Test                       | “Data source is working” |

---

# Si quieres, puedo revisar tu `docker-compose.yml` completo y decirte EXACTAMENTE qué probar y en qué orden según tu configuración actual.

¿Quieres que valide tu stack con tus contenedores reales?
