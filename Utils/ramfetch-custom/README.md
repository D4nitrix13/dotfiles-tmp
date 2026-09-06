# Ramfetch

Ramfetch es una herramienta ligera escrita en Bash que muestra información del sistema de forma rápida en la terminal. Está diseñada como una alternativa simple a herramientas como neofetch, enfocándose en bajo consumo y facilidad de uso.

---

## Características

* Implementación en Bash sin dependencias complejas
* Ejecución rápida
* Instalación mediante Makefile
* Integración directa en el sistema

---

## Requisitos

* bash disponible en /bin/bash
* make
* Permisos de escritura en el directorio de instalación

---

## Instalación

### Instalación global (requiere privilegios)

Instala el ejecutable en /usr/local/bin:

```bash
make install
sudo make install
```

Luego puedes ejecutar:

```bash
ramfetch
```

---

### Instalación local (recomendada)

Instala sin necesidad de sudo en el directorio del usuario:

```bash
make install PREFIX="$HOME/.local"
```

Asegúrate de que el PATH incluya:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Luego ejecuta:

```bash
ramfetch
```

---

## Verificación

Para comprobar la instalación:

```bash
which ramfetch
```

Salida esperada:

```bash
/usr/local/bin/ramfetch
```

o

```bash
/home/user/.local/bin/ramfetch
```

---

## Desinstalación

```bash
sudo make uninstall
```

o si fue instalación local:

```bash
make uninstall PREFIX="$HOME/.local"
```

---

## Reinstalación

```bash
sudo make reinstall
```

---

## Estructura del proyecto

```bash
.
├── Makefile
└── ramfetch
```

---

## Notas técnicas

El Makefile utiliza:

```bash
install -Dm755
```

Esto permite:

* Crear directorios automáticamente si no existen
* Asignar permisos de ejecución (755)

El script original:

```bash
ramfetch
```

se instala como:

```bash
ramfetch
```

---

## Uso

Ejecuta:

```bash
ramfetch
```

---

## Autor

Daniel Benjamin Perez Morales
GitHub: D4nitrix13
