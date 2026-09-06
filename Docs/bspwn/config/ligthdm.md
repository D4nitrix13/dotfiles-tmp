Para añadir una tarea que se ejecute **antes de que se inicie el entorno gráfico con LightDM** (es decir, *antes de que se cargue la pantalla de login*), tenés varias formas seguras de hacerlo en Linux. Aquí van las opciones recomendadas:

---

## ✅ OPCIÓN 1: Usar un **servicio de systemd**

Este es el método más robusto y limpio. Podés crear un servicio que se ejecute **antes** de que arranque `lightdm.service`.

### 🔧 Paso a paso:

1. Crea el archivo de servicio:

```bash
sudo nano /etc/systemd/system/mi-tarea.service
```

2. Ejemplo de contenido:

```ini
[Unit]
Description=Mi tarea personalizada antes de LightDM
Before=lightdm.service

[Service]
Type=oneshot
ExecStart=/ruta/a/mi/script.sh
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
```

> 📌 Asegúrate de que `/ruta/a/mi/script.sh` sea ejecutable:
>
> ```bash
> chmod +x /ruta/a/mi/script.sh
> ```

3. Habilita el servicio:

```bash
sudo systemctl enable mi-tarea.service
```

Ahora se ejecutará **en cada inicio**, **antes** de que se cargue LightDM.

---

## ✅ OPCIÓN 2: Modificar el servicio `lightdm.service`

Si querés insertar el script directamente **antes** de que se ejecute LightDM, podés usar un "drop-in" de systemd:

```bash
sudo systemctl edit lightdm.service
```

Agregá:

```ini
[Service]
ExecStartPre=/ruta/a/mi/script.sh
```

Este script se ejecutará **justo antes** del arranque de LightDM.

---

## ⚠️ NO RECOMENDADO

Evitá usar `.bashrc`, `.xinitrc`, o `/etc/profile`, ya que estos se ejecutan **después** del login o sólo cuando hay sesión gráfica iniciada, no antes de LightDM.

---

## ✅ Resumen

| Método                    | Cuándo se ejecuta               | Recomendado |
| ------------------------- | ------------------------------- | ----------- |
| systemd `Before=lightdm`  | Antes del arranque de LightDM   | ✅ Sí        |
| `ExecStartPre` en LightDM | Justo antes de ejecutar LightDM | ✅ Sí        |
| `.bashrc`, `.xprofile`    | Después del login gráfico       | ❌ No        |

---

¿Querés que te arme un ejemplo con un script real (como montar algo, tocar permisos o crear un log)?
