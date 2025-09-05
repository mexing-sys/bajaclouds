#  BajaClouds

BajaClouds es una aplicación web desarrollada con **Django** que busca emprender en los servicios en la nube.  (En Desarrollo)

---

## 🚀 Características principales
- Backend en *Django + Gunicorn*.
- Gestión de configuración segura (SSL,ENV,etc) 
- Base de datos **SQLite (local)** y soporte para **PostgreSQL/MySQL** en producción.
- Panel de administración personalizado.
- Archivos estáticos y media configurados.
- Despliegue sobre  **Ubuntu Server + Nginx**.
- Cloude Hosting  Proxmox 9.0.5 + CloudFlare Tunnel
---

## 🛠️ Tecnologías utilizadas
- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Gunicorn](https://gunicorn.org/)
- [Nginx](https://nginx.org/)
- [SQLite / PostgreSQL](https://www.postgresql.org/)
- [TailwindCSS](https://tailwindcss.com/) 

---

## 📂 Estructura del proyecto
BajaClouds/
  bajaclouds/ # Aplicación principal
  home/ # Pagina Inicio
  static/ # Archivos estáticos (CSS, JS, imágenes)
  media/ # Archivos subidos por usuarios
  templates/ # Plantillas HTML
  manage.py # Script de gestión de Django
  requirements.txt # Dependencias del proyecto
  .env # Variables de entorno 
