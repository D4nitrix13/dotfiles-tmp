Sí, puedes hacer que tu sistema Linux se bloquee automáticamente cuando no haya actividad del mouse o teclado durante un cierto tiempo, usando herramientas como `xautolock`, `xidle`, `xss-lock` o directamente configurando `systemd` y `i3lock`/`i3lock-color`.

### Opción recomendada: `xautolock` + `i3lock` o `i3lock-color`

#### 1. **Instala las herramientas necesarias**

```bash
yay -S xautolock
```

#### 2. **Agrega este comando a tu archivo de inicio** (por ejemplo en `.xinitrc`, `.xprofile`, o en tu script de inicio de Openbox, BSPWM, etc.)

```bash
xautolock -time 5 -locker "i3lock-color --blur=5 --clock --indicator" -detectsleep &
```

* `-time 5`: bloquea la pantalla tras 5 minutos de inactividad.
* `-locker`: comando para bloquear la pantalla (puede ser `i3lock`, `i3lock-color`, `betterlockscreen`, etc.).
* `-detectsleep`: evita que se bloquee inmediatamente al volver de suspensión.

#### 3. **Si quieres que no se bloquee mientras estás viendo un video**, puedes usar

```bash
xautolock -time 5 -locker "i3lock" -notifier "notify-send 'Screen will lock in 10 seconds'" -killtime 10 -killer "xset dpms force off" &
```

---

### Alternativa: usando `xss-lock` (más moderno, funciona con `xsecurelock`, `i3lock`, etc.)

```bash
xss-lock -- i3lock --color=000000 &
```

Pero este requiere que el servidor X respete `XScreenSaver` internamente, y que esté habilitado.

---

### Verifica el tiempo de inactividad (útil para debugging)

```bash
xprintidle
```

Este comando muestra los milisegundos desde la última actividad.

---

¿Quieres que prepare un script de ejemplo para Openbox o BSPWM?
