7. Reflexión de Aprendizaje

Durante el desarrollo del proyecto se aplicaron de forma integrada conocimientos de sistemas operativos, redes, virtualización y desarrollo web. En particular, se reforzaron habilidades en administración de procesos y servicios en Linux (arranque, parada y monitoreo con systemd), manejo de permisos y propietarios sobre el sistema de archivos (modelo usuario/grupo/otros), y operación segura de un servidor web y un motor de base de datos en un entorno controlado. La práctica constante con Ubuntu dentro de una máquina virtual permitió comprender la relación entre hardware virtual, kernel y servicios de usuario, así como la importancia de definir recursos adecuados (CPU, RAM, disco, adaptadores de red) según los objetivos del sistema.

El mayor reto técnico fue la conexión estable y segura entre PHP y PostgreSQL. Inicialmente surgieron incidencias relacionadas con controladores, extensiones de PHP no habilitadas y políticas de acceso en PostgreSQL. Este problema se solucionó instalando y habilitando la extensión php-pgsql, verificando su carga en el entorno de Apache, y ajustando la configuración de pg_hba.conf y postgresql.conf para permitir conexiones locales autenticadas de manera correcta. Además, se revisaron parámetros de php.ini (upload_max_filesize, post_max_size, memory_limit) y cabeceras de Apache para garantizar cargas de archivos confiables sin comprometer la seguridad.

A nivel metodológico, el trabajo en un esquema incremental evidenció los beneficios de iterar por etapas: primero levantar el entorno (VirtualBox + Ubuntu), después el servidor LAMP, posteriormente la base de datos y la interfaz web, y finalmente las pruebas de concurrencia, permisos y respaldo. Este orden permitió detectar tempranamente inconsistencias (por ejemplo, permisos del directorio de subida o rutas relativas en el servidor web), y corregirlas antes de avanzar a la siguiente fase.

Desde la perspectiva de seguridad y buenas prácticas, se interiorizó la necesidad de validar entradas (tanto en cliente como en servidor), restringir tipos de archivo por MIME real, separar el almacenamiento de ficheros de la raíz pública del sitio, y proteger formularios con tokens contra CSRF. También se aprendió a registrar eventos clave (inicio de sesión, carga/descarga, eliminación) para auditoría y a aplicar cuotas y límites de tamaño como mecanismo preventivo ante abusos involuntarios.

Finalmente, la experiencia permitió comprender, en un entorno realista, cómo el sistema operativo coordina procesos concurrentes, gestiona memoria y archivos, y expone servicios de red que son consumidos por el navegador del usuario. Trabajar con instantáneas de la máquina virtual (snapshots), copias de respaldo y restauraciones rápidas fortaleció la capacidad para responder a fallos y reducir tiempos de recuperación. En conjunto, el proyecto consolidó competencias técnicas y criterios de ingeniería necesarios para diseñar, desplegar y mantener servicios web locales con niveles aceptables de rendimiento, seguridad y mantenibilidad.

---

Tabla de comandos y archivos de configuración (para copiar y consultar)

+------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Propósito | Comando / Archivo | Nota |
+------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Actualizar repositorios | sudo apt update | Preparación del entorno Ubuntu |
| Instalar Apache | sudo apt install apache2 | Servidor web |
| Instalar PHP | sudo apt install php libapache2-mod-php | Módulo PHP para Apache |
| Extensión PHP–PostgreSQL | sudo apt install php-pgsql | Habilita conexión PHP ↔ PostgreSQL |
| Extensiones útiles PHP | sudo apt install php-zip php-xml php-mbstring php-gd | Manejo de ZIP, XML, UTF-8, imágenes |
| Instalar PostgreSQL | sudo apt install postgresql postgresql-contrib | Motor de base de datos |
| Estado de servicios | systemctl status apache2 | Verifica Apache |
| | systemctl status postgresql | Verifica PostgreSQL |
| Iniciar/detener servicio | sudo systemctl start|stop|restart apache2 | Control de Apache |
| | sudo systemctl start|stop|restart postgresql | Control de PostgreSQL |
| Habilitar al arranque | sudo systemctl enable apache2 postgresql | Servicios persistentes |
| Ver módulos PHP cargados | php -m | Confirmar php-pgsql |
| Comprobar versión PHP | php -v | Diagnóstico |
| Crear rol en PostgreSQL | sudo -u postgres psql -c "CREATE ROLE localdrive WITH LOGIN PASSWORD 'TuClaveSegura';" | Usuario de BD para la app |
| Crear base de datos | sudo -u postgres psql -c "CREATE DATABASE localdrive OWNER localdrive;" | BD de la aplicación |
| Acceder a psql | sudo -u postgres psql | Consola interactiva |
| Listar DB/roles | \l (en psql) / \du | Inspección |
| Archivo pg*hba.conf | /etc/postgresql/*/main/pg*hba.conf | Políticas de acceso |
| Archivo postgresql.conf | /etc/postgresql/*/main/postgresql.conf | Puertos, memoria, etc. |
| Recargar PostgreSQL | sudo systemctl reload postgresql | Aplicar cambios |
| Raíz de sitio (ejemplo) | /var/www/localdrive/ | Carpeta del proyecto |
| VirtualHost de Apache | /etc/apache2/sites-available/localdrive.conf | Host virtual para el sitio |
| Habilitar sitio | sudo a2ensite localdrive.conf && sudo systemctl reload apache2 | Activar host virtual |
| Deshabilitar default | sudo a2dissite 000-default.conf && sudo systemctl reload apache2 | Opcional |
| Habilitar módulos Apache | sudo a2enmod rewrite headers ssl | Reescritura, cabeceras, TLS |
| Archivo apache2.conf | /etc/apache2/apache2.conf | Configuración general |
| Archivo php.ini (Apache) | /etc/php/\*/apache2/php.ini | Límites de subida, memoria, zona horaria |
| Parámetros PHP típicos | upload_max_filesize = 32M | Ajustar según necesidades |
| | post_max_size = 32M | |
| | memory_limit = 256M | |
| | date.timezone = America/Managua | Hora local |
| Permisos de la app | sudo chown -R www-data:www-data /var/www/localdrive | Propietario para Apache |
| | find /var/www/localdrive -type d -exec chmod 755 {} ; | Permisos carpetas |
| | find /var/www/localdrive -type f -exec chmod 644 {} ; | Permisos archivos |
| Comprobación de sintaxis | sudo apachectl configtest | Validación de Apache |
| Recarga de Apache | sudo systemctl reload apache2 | Aplicar cambios |
| Hosts locales (opcional) | /etc/hosts | Mapear dominio local (p. ej. localdrive.test) |
| Firewall UFW (opcional) | sudo ufw allow "Apache Full" | Abrir HTTP/HTTPS |
| Snapshot de VM | VBoxManage snapshot "NombreVM" take "pre-cambio" | Punto de restauración |
| Exportar VM | VBoxManage export "NombreVM" -o localdrive.ova | Portabilidad |
| Respaldo de BD | pg_dump -U localdrive -d localdrive > backup.sql | Copia lógica |
| Restaurar BD | psql -U localdrive -d localdrive -f backup.sql | Recuperación |
+------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Nota: en las rutas que incluyen “\*/” (comodín), el asterisco representa la versión instalada (por ejemplo, /etc/php/8.3/apache2/php.ini o /etc/postgresql/16/main/pg_hba.conf). Ajustar según la versión disponible en Ubuntu 25.10.
