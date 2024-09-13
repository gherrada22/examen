# Proyecto de Inventario en Django

Este proyecto es una aplicación web de inventario desarrollada en Django. Permite listar productos, registrar nuevos productos y realizar ventas de pedidos. La interfaz de usuario es responsive gracias a Bootstrap.

## Características

- Listado de productos con búsqueda avanzada.
- Registro de nuevos productos.
- Venta de pedidos con detalles.
- Interfaz de usuario responsive.

## Requisitos

- Python 3.8 o superior
- Django 3.2 o superior
- Bootstrap 4 o superior

### 2. Crear y activar un entorno virtual

#### En Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

#### En macOS y Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django bootstrap4
```
### 4. Configurar la base de datos

Django usa SQLite por defecto, por lo que no es necesario realizar configuraciones adicionales para la base de datos.

### 5. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario
Para acceder al panel de administración de Django, necesitas crear un superusuario.

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

## Uso

### Acceder a la aplicación

- Lista de productos: `http://127.0.0.1:8000/inventory/productos/`
- Registrar producto: `http://127.0.0.1:8000/inventory/productos/registrar/`
- Venta de pedido: `http://127.0.0.1:8000/inventory/venta/`

### Acceder al panel de administración

- URL: `http://127.0.0.1:8000/admin/`
- Usa las credenciales del superusuario que creaste anteriormente.

## Estructura del Proyecto

- `myproject/`: Directorio principal del proyecto.
  - `settings.py`: Configuración del proyecto.
  - `urls.py`: Configuración de las URLs del proyecto.
- `inventory/`: Aplicación de inventario.
  - `models.py`: Definición de los modelos de datos.
  - `views.py`: Definición de las vistas.
  - `forms.py`: Definición de los formularios.
  - `urls.py`: Configuración de las URLs de la aplicación.
  - `templates/inventory/`: Plantillas HTML de la aplicación.
    - `base.html`: Plantilla base con Bootstrap.
    - `lista_productos.html`: Plantilla para listar productos.
    - `registrar_producto.html`: Plantilla para registrar productos.
    - `venta_pedido.html`: Plantilla para registrar ventas de pedidos.

## Dependencias

Las dependencias del proyecto están listadas en el archivo `requirements.txt`. Asegúrate de instalar todas las dependencias antes de ejecutar el proyecto.

```bash
pip install -r requirements.txt
```
## Notas

- Asegúrate de tener una conexión a internet para cargar los archivos de Bootstrap desde el CDN.
- Puedes personalizar las plantillas y estilos según tus necesidades.

# para el panel de administracion
usuario: gherrada22
password: 2001

# Accede a la página de inicio de sesión:
URL: http://127.0.0.1:8000
que lo va a redirigir a la pagina de login
http://127.0.0.1:8000/accounts/login/

# Inicia sesión con las credenciales del superusuario que creaste.
Después de iniciar sesión, deberías ser redirigido a la lista de productos:

URL: http://127.0.0.1:8000/inventory/productos/