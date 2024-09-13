# Proyecto de Inventario en Django

Este proyecto es una aplicación web de inventario desarrollada en Django. Permite listar productos, registrar nuevos productos y realizar ventas de pedidos. La interfaz de usuario es responsive gracias a Bootstrap.
# Propuesta del examen
CASO: Se necesita que se desarrolle una pagina web donde un usuario con password y contraseña pueda ingresar y registrar un producto para ello se necesitara que se tenga los siguientes formularios.

   - Formulario de listado de productos, grupo y subgrupos. (Grupo->SubGRupo-> Producto), El contenido del producto debe ser (Nombre, id, precio de venta)
   - Formulario de mantenimiento o modal de mantenimiento (Se deja libre de desarrollar)
   - Formulario de venta de pedidos (Cabecerta solo id de orden, y detalle de venta -> Producto,cantidad y precio de venta)
   - Un reporte donde muestre la información según cruzando, productos, grupos, subgrupos y ordenes generados (Opcional con filtros).


## Capturas de pantalla

![240913_07h03m20s_screenshot](https://github.com/user-attachments/assets/a0be84c3-73db-4eaf-aa98-376d3414f325)

![240913_06h26m15s_screenshot](https://github.com/user-attachments/assets/4c78d457-fbcc-4514-9de7-c9033d350a96)

![240913_06h27m45s_screenshot](https://github.com/user-attachments/assets/996a75fd-e4ac-488d-9d2b-491c8bbd3e71)

![240913_06h27m58s_screenshot](https://github.com/user-attachments/assets/f2108194-0514-49d0-a045-9b50483e0ff6)

![240913_06h28m07s_screenshot](https://github.com/user-attachments/assets/1f14a637-3284-4cda-afc2-3a113ec1b064)

![240913_06h28m26s_screenshot](https://github.com/user-attachments/assets/b371d576-2536-47bf-b59e-35c07b7cd025)

![240913_06h28m35s_screenshot](https://github.com/user-attachments/assets/a7c10b84-0848-4e24-ba82-8755f36c304a)

![240913_06h28m44s_screenshot](https://github.com/user-attachments/assets/f81edf59-db8f-4cd0-b2d9-558f01441a67)


## Características

- Listado de productos con búsqueda avanzada(en proceso)
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
- Inicio de sesión: `http://127.0.0.1:8000`
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

# para el panel de administracion e inicio de sesión
```bash
usuario: gherrada22
contraseña: 2001
```

- Aún sigue en mejoras :)

&nbsp;

<p align="center">
  <img src="https://user-images.githubusercontent.com/104341274/210186277-0d434bb0-80c0-43a9-b6b0-2e42e18c31a9.png" width="400" />
</p>

<p align="center">Copyright &copy; <a href="https://github.com/gherrada22" target="_blank">George Herrada Farfán</a>
</p>
