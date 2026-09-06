En **VirtualBox**, para entrar a la "BIOS" (en realidad, el **menú UEFI/firmware de la máquina virtual**), sigue estos pasos:

---

## ✅ OPCIÓN 1: Habilitar el menú UEFI

1. **Apaga la máquina virtual** completamente.
2. Ve a la **configuración de la VM** en VirtualBox.
3. En la pestaña **Sistema > Placa base**:

   * Activa ✅ **"Habilitar EFI (especial para SOs EFI)"**
4. Guarda los cambios.

---

## ✅ OPCIÓN 2: Forzar entrada al firmware UEFI

Puedes decirle a VirtualBox que **entre directamente al menú UEFI (BIOS)**:

### 🔧 Desde terminal (Linux):

```bash
VBoxManage modifyvm "NOMBRE_DE_TU_VM" --firmware efi
VBoxManage startvm "NOMBRE_DE_TU_VM" --bioslogodisplaytime 5000 --biosbootmenu menu
```

> Cambia `"NOMBRE_DE_TU_VM"` por el nombre real de tu VM.

---

## ✅ OPCIÓN 3: Pulsar tecla para entrar

Cuando arrancas la VM (EFI habilitado), presiona repetidamente una de estas teclas:

* **ESC** o **F2**
* También puedes probar **DEL** o **F12**
  (Solo funcionan si EFI está activado)

---

## Resultado

Entrarás al **menú UEFI de VirtualBox**, donde puedes:

* Cambiar el orden de arranque (boot)
* Ver discos
* Configurar opciones de EFI

---

¿Quieres usar BIOS clásica en vez de EFI? ¿O necesitas configurar algo especial como booteo desde USB o ISO?
