# Audio AI Report Backend

Este proyecto es una aplicación backend que permite la generación de informes a partir de archivos de audio utilizando inteligencia artificial. A continuación se describen los componentes principales del backend.

## Estructura del Proyecto

- **app.py**: Punto de entrada de la aplicación Flask. Configura la aplicación y las rutas necesarias.
- **api/**: Contiene la lógica de la API, incluyendo las rutas para manejar las solicitudes relacionadas con la generación de informes.
- **core/**: Contiene la configuración y el sistema de logging de la aplicación.
- **services/**: Implementa la lógica de negocio, incluyendo la ingesta de audio, preprocesamiento, transcripción, generación de embeddings, y construcción de informes.
- **models/**: Define los modelos de datos utilizados en la aplicación.
- **database/**: Maneja la conexión y las operaciones de la base de datos, incluyendo migraciones y datos iniciales.
- **utils/**: Contiene funciones utilitarias, como validadores y manejo de archivos.
- **tests/**: Incluye pruebas para asegurar el correcto funcionamiento de la aplicación.
- **requirements.txt**: Lista las dependencias necesarias para el backend.

## Requisitos

Para instalar las dependencias del proyecto, ejecute:

```
pip install -r requirements.txt
```

## Ejecución

Para iniciar la aplicación, ejecute:

```
python app.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si desea contribuir, por favor abra un issue o un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.