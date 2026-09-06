iSon **parecidos en concepto**, pero **no son lo mismo**.
GitHub Actions y GitLab CI/CD cumplen funciones similares (automatizar build, test, deploy), pero su arquitectura, sintaxis y funcionamiento interno **son diferentes**.

A continuación te lo explico de forma clara y técnica:

---

# 1. Concepto general

| Plataforma                 | ¿Qué es?                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| **GitHub Actions (CI/CD)** | Sistema de automatización nativo de GitHub. Usa archivos YAML en `.github/workflows`.       |
| **GitLab CI/CD**           | Sistema de integración continua nativo de GitLab. Usa `.gitlab-ci.yml` en la raíz del repo. |

Ambos permiten:

- Pipelines automatizados
- CI (testing)
- CD (deployment)
- Ejecutar jobs en runners
- Triggers con push, tags, merge requests, schedules, etc.

Pero tienen **implementación y sintaxis distintas**.

---

# 2. Diferencias principales

## A. Archivo de configuración

GitHub:

```
.github/workflows/cd.yml
```

GitLab:

```
.gitlab-ci.yml
```

GitHub permite varios workflows separados.
GitLab maneja un único pipeline compuesto de stages.

---

## B. Sintaxis

GitHub usa YAML con `jobs:`:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
```

GitLab usa YAML con `stages:`:

```yaml
stages:
  - build
  - test

build:
  stage: build
  script:
    - npm install
```

No son compatibles entre sí.

---

## C. Ejecución

| Plataforma         | Cómo corre                                                                      |
| ------------------ | ------------------------------------------------------------------------------- |
| **GitHub Actions** | Usa runners propios de GitHub y también self-hosted runners. Jobs por workflow. |
| **GitLab CI/CD**   | Usa GitLab Runners (propios o auto-instalados). Pipelines por stages.           |

---

## D. Marketplace de acciones

GitHub tiene **GitHub Actions Marketplace**, con miles de acciones ya hechas:

- docker/build-push-action
- setup-python
- setup-go
- login-actions
- etc.

GitLab no usa acciones externas así; usa scripts dentro de jobs.

---

## E. Triggers

GitHub:

```yaml
on:
  push:
  pull_request:
  schedule:
  workflow_dispatch:
```

GitLab:

```yaml
only:
  - pushes
  - tags
  - schedules
```

---

## F. Acceso a variables

GitHub:

```
${{ github.ref }}
${{ secrets.MY_SECRET }}
```

GitLab:

```
$CI_COMMIT_REF_NAME
$CI_JOB_TOKEN
$MY_SECRET
```

---

# 3. ¿Qué es más parecido?

GitHub Actions está inspirado en:

- Azure Pipelines
- GitLab CI/CD
- CircleCI
- Jenkins declarativo

Pero GitLab CI/CD es más tradicional y estructurado en **stages → jobs → scripts**.

---

# 4. Resumen claro

### Igual en concepto:

- Automatizar CI/CD.
- Desplegar en Docker, Kubernetes, servidores.
- Correr scripts.
- Activarse con tags (como tu `v1.0.5`).
- Usar variables y secretos.

### Diferente en:

- Sintaxis YAML.
- Ubicación del archivo.
- Cómo se organizan los jobs.
- Cómo se usan acciones/plugins.
- Cómo gestionan runners.

---

# Si quieres, puedo hacerte:

- Una **comparación lado a lado** GitHub/CD vs GitLab-CD.
- Un **equivalente del workflow que hiciste para GitLab**.
- Una **plantilla optimizada para FastAPI + Docker + GHCR** tanto en GitHub como GitLab.
- Cómo desplegar en Kubernetes desde ambos (CD real).
