<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Información del Paquete `openssh`***

- **Página de Instalación de Arch Linux:** *[Arch Linux - openssh](https://archlinux.org/packages/core/x86_64/openssh/ "https://archlinux.org/packages/core/x86_64/openssh/")*
- **Repositorio de GitHub:** *[OpenSSH GitHub](https://github.com/openssh/openssh-portable "https://github.com/openssh/openssh-portable")*
- **Página Oficial del Paquete:** *[OpenSSH](https://www.openssh.com/ "https://www.openssh.com/")*

---

## ***Instalación***

```bash
sudo pacman -Syu --noconfirm openssh
```

---

### ***Funcionamiento a Bajo Nivel***

**OpenSSH** *(Open Secure Shell) es un conjunto de herramientas para proporcionar sesiones remotas seguras a través del protocolo SSH (Secure Shell). A continuación se detalla cómo funciona a bajo nivel:*

1. **Autenticación:**
   - **Claves Públicas/Privadas:** *El cliente y el servidor usan pares de claves para autenticarse mutuamente. La clave pública se comparte, mientras que la clave privada se mantiene segura y privada.*
   - **Contraseñas:** *Alternativamente, el servidor puede solicitar una contraseña para autenticar al usuario.*

2. **Encriptación:**
   - **Cifrado de Sesión:** *Una vez autenticado, el tráfico entre el cliente y el servidor se cifra usando algoritmos como AES, 3DES, etc. Esto asegura que los datos transferidos no puedan ser leídos por terceros.*

3. **Integridad de Datos:**
   - **HMAC (Hash-based Message Authentication Code):** *Se utiliza para asegurar que los datos no hayan sido alterados durante la transmisión. Esto se logra aplicando un hash criptográfico a los datos y comparándolo en ambos extremos.*

4. **Compresión:**
   - **Compresión de Datos:** *OpenSSH puede opcionalmente comprimir los datos antes de la transmisión para aumentar la velocidad de transferencia en conexiones lentas.*

5. **Túneles Seguros:**
   - **Port Forwarding:** *OpenSSH permite tunelizar otros protocolos y conexiones a través de la conexión SSH segura. Esto incluye el reenvío de puertos locales y remotos.*

6. **Configuración del Sistema:**
   - **Ficheros de Configuración:** *Los ficheros de configuración como `sshd_config` (para el servidor) y `ssh_config` (para el cliente) permiten personalizar aspectos del comportamiento de SSH, como puertos de escucha, métodos de autenticación permitidos, etc.*
   - **Demonio sshd:** *En el servidor, el demonio `sshd` se ejecuta en segundo plano, esperando conexiones entrantes. Al recibir una solicitud de conexión, autentica al usuario y establece una sesión segura.*

7. **Integración con el Sistema:**
   - **Servicios y Demonios:** *En Arch Linux, el servicio `sshd` puede gestionarse utilizando `systemd`. Comandos como `systemctl start sshd`, `systemctl enable sshd`, y `systemctl status sshd` se usan para iniciar, habilitar y verificar el estado del servicio SSH.*
   - **Ficheros de Registro:** *Los eventos y errores de OpenSSH se registran en ficheros de registro como `/var/log/auth.log` o `/var/log/secure` dependiendo de la configuración del sistema.*

---

### ***Resumen***

> [!NOTE]
> **OpenSSH** *proporciona una forma segura de comunicarse entre sistemas, protegiendo los datos en tránsito mediante cifrado y asegurando la integridad de la comunicación. Su implementación a bajo nivel involucra una serie de pasos y protocolos que aseguran que tanto la autenticación como la transferencia de datos se realicen de manera segura y confiable.*
