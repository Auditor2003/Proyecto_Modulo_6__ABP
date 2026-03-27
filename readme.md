# Proyecto Módulo 6 – Gestor de Proyectos (Django)

## Descripción

Este proyecto corresponde al desarrollo de una aplicación web utilizando Django, cuyo objetivo es gestionar proyectos y tareas, incorporando autenticación de usuarios, control de acceso y visualización diferenciada según el tipo de usuario.

---

## 1. Autenticación (Login / Logout)

Se implementó un sistema de autenticación utilizando las vistas de Django.

* Inicio de sesión personalizado
* Manejo de errores en el login
* Cierre de sesión mediante método POST
* Redirección controlada

---

## 2. Protección de vistas (Decoradores)

Se utilizó el decorador:

@login_required

Para restringir el acceso a vistas protegidas como el dashboard, evitando que usuarios no autenticados accedan a información sensible.

---

## 3. Gestión de usuarios

Se trabajó con dos tipos de usuarios:

* Superusuario

  * Acceso total
  * Visualiza proyectos y tareas

* Usuario normal

  * Acceso limitado
  * No visualiza detalles

Los usuarios son gestionados desde el panel de administración de Django, sin embargo se pueden crear desde Login Web y asignar rol y proyecto.

---

## 4. Control de acceso

Se implementó control de acceso utilizando:

request.user.is_superuser

Esto permite:

* Diferenciar contenido según el tipo de usuario
* Restringir información sensible

Se aplicó tanto en:

* Backend (views)
* Frontend (templates)

---

## 5. Interfaz de usuario

Se desarrolló una interfaz clara y funcional:

* Página de inicio con conteo de datos
* Dashboard con detalle
* Login estilizado con Bootstrap
* Mensajes de error amigables
* Navbar global con botón de cierre de sesión

---

## 6. Arquitectura del proyecto

Se implementó una estructura organizada:

* Uso de plantilla base (base.html)
* Separación de vistas

  * Home → resumen
  * Dashboard → detalle
* Evita duplicación de código
* Mejora mantenibilidad

---

## 7. Gestión de datos (Admin Django)

Los datos se gestionan desde el panel de administración:

* Creación de proyectos
* Creación de tareas
* No se implementa CRUD en frontend (según requerimiento)

---

## Seguridad (CSRF)

Se utilizó protección CSRF en formularios mediante:

{% csrf_token %}

Esto protege contra ataques de tipo Cross-Site Request Forgery.

---

## Conclusión

El sistema implementa correctamente autenticación, control de acceso, protección de vistas y diferenciación de usuarios, cumpliendo con los requisitos solicitados y aplicando buenas prácticas de desarrollo en Django.

---

## Defensa del proyecto

Se implementó autenticación con Django, se protegieron vistas mediante decoradores y se diferenciaron accesos utilizando atributos del usuario como is_superuser, además de estructurar la aplicación con una plantilla base para mantener consistencia visual.

---

## Repositorio

https://github.com/Auditor2003/Proyecto_Modulo_6__ABP
