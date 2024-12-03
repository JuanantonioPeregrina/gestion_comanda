# 🥘 MCNOLO - Gestor de Comandas para Restaurantes 🍽️

MCNOLO es una solución eficiente para gestionar las comandas en restaurantes, permitiendo a los clientes enviar pedidos directamente a la cocina desde una aplicación web. Su objetivo es optimizar el flujo de trabajo, reducir errores humanos y ofrecer una experiencia más rápida y fluida tanto para el cliente como para el personal del restaurante.

---

## 👨‍🍳 Desarrolladores 👩‍🍳

Este proyecto ha sido desarrollado por el equipo:

1. **Juan Antonio Peregrina**🍔
2. **Anthony Caju**🍕
3. **Jorge VF**🍟
4. **Miguel G7**🍣
5. **Iván Martínez Floro**🌮
6. **Robert CV** 🍩

Gracias a su dedicación y esfuerzo, este proyecto se ha convertido en una herramienta poderosa para la gestión de restaurantes. 🎉

---

## 🚀 Características principales 🍽️

- **Gestión de usuarios**: Inicio de sesión y registro con roles diferenciados: **Clientes**, **Invitados** y **Admins**.
- **Gestión de pedidos**: Creación, cancelación y seguimiento de pedidos. 📝
- **Procesos de pago integrados**: Soporte para pagos mediante Stripe. 💳
- **Gestión de menús**: Administración y visualización de la carta del restaurante. 📜
- **Notificaciones en tiempo real**: Integración con WebSockets para actualizaciones instantáneas. 📡
- **Recuperación de cuentas**: Función para recuperación de contraseñas olvidadas. 🔑
- **Historial de facturación**: Almacenamiento y descarga de facturas en formato HTML. 📂

---

## 🛠️ Despliegue inicial para desarrolladores

### Instalación de dependencias
Asegúrate de tener Python instalado en tu sistema. Luego, instala las dependencias necesarias ejecutando los siguientes comandos:

```bash
pip install django
pip install stripe
pip install channels_redis
(quizás falte por determinar alguno más)
```

### Activar entorno virtual
Activa tu entorno virtual para gestionar las dependencias:

```bash
.\env\Scripts\activate
```

### Migraciones de base de datos
Realiza las migraciones necesarias para inicializar la base de datos:

```bash
cd .\gestion_comanda\
python .\mcnolo\manage.py makemigrations
python .\mcnolo\manage.py migrate
```

### Ejecutar el servidor de desarrollo
Inicia el servidor de desarrollo para probar la aplicación localmente:

```bash
python .\mcnolo\manage.py runserver
```

Accede a la aplicación en tu navegador en [http://localhost:8000](http://localhost:8000). 🖥️

---

## 🌐 Configuración adicional para PHP (opcional) 🍝

Algunas funcionalidades pueden requerir soporte para archivos PHP. Para configurar esto, sigue los pasos a continuación:

1. Descarga e instala **XAMPP** desde [aquí](https://sourceforge.net/projects/xampp/).
2. Copia los siguientes archivos en la carpeta deseada dentro de la instalación de XAMPP:
   - `InicioSesion2.html`
   - `index.html`
   - `login.php`
   - `PaginaPrincipal.html`
   - `usuarios.json`
3. Guarda estos archivos en la ruta: `C:\xampp\htdocs\carpetaqueprefieras`.
4. Inicia el panel de control de XAMPP y activa el módulo **Apache**.
5. Abre tu navegador y accede a [http://localhost/ISO/index.html](http://localhost/ISO/index.html) para usar estas funcionalidades.

---

## 📂 Estructura del proyecto 🍳

El proyecto se organiza de la siguiente manera:

```
gestion_comanda/
│
├── mcnolo/
│   ├── app/               # Aplicación principal
│   │   ├── migrations/    # Migraciones de base de datos
│   │   ├── templates/     # Archivos HTML para vistas
│   │   ├── static/        # Archivos estáticos (CSS, JS, imágenes)
│   │   ├── models.py      # Modelos de datos
│   │   ├── views.py       # Lógica de vistas
│   │   ├── urls.py        # Enrutamiento
│   │   └── tests.py       # Pruebas unitarias
│   ├── media/             # Almacenamiento de archivos cargados
│   ├── asgi.py            # Configuración para WebSockets
│   ├── settings.py        # Configuración global del proyecto
│   └── wsgi.py            # Configuración para despliegue en servidor
└── env/                   # Entorno virtual
```

---

## ⚙️ Tecnologías utilizadas 🍤

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de datos**: SQLite (por defecto)
- **Pagos**: Integración con Stripe
- **WebSockets**: Django Channels
- **Servidor local**: XAMPP (opcional)

---

## 🤝 Contacto

Si tienes dudas, problemas o sugerencias, por favor abre un **issue** en este repositorio. Estaremos encantados de ayudarte. 🍴


