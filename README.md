# Proyecto Coder - Tienda de Ropa Urbana

Este proyecto fue desarrollado como parte de la **Entrega Final** del curso de Python.  
Consiste en una **tienda básica de ropa** donde los usuarios pueden registrarse, iniciar sesión y gestionar prendas (crear, ver, actualizar y eliminar).


## Funcionalidades principales

### Autenticación
- Registro de usuarios
- Inicio de sesión
- Cierre de sesión
- Acceso restringido para crear/editar/eliminar prendas (solo usuarios logueados)

### Gestión de prendas
Modelo **Prenda**:
- Marca  
- Categoría (distintos tipos de prendas que existan)  
- Talla  
- Imagen  

Vistas disponibles:
- **Inicio**: página principal
- **Acerca de mí**: información de la autora y del proyecto
- **Crear prenda**: solo para usuarios autenticados
- **Listado de prendas**: muestra todas las prendas creadas
- **Detalle de prenda**: vista "Ver"
- **Actualizar prenda**
- **Eliminar prenda**
- **Buscador de prendas por categoría**


## Manejo de imágenes
El proyecto permite:
- Subir una imagen al crear una prenda
- Mantener la imagen actual al actualizar (no es obligatorio cambiarla)

## Tecnologías utilizadas
- **Python**
- **Django**
- **HTML**
- **Git y GitHub**


## Cómo ejecutar el proyecto
1. Activar el entorno virtual:
   ```bash
   source .venv/Scripts/activate

2. Instalar dependencias

3. Iniciar servidor: python manage.py runserver

4. Entrar al proyecto

## Video demostración

Demo: https://drive.google.com/drive/folders/11MbQOlBrG6tpmhDKr7xeAEoyVY2CExrf?usp=sharing 

## Proyecto creado por

Javiera Poblete