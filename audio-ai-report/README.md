# Audio AI Report Project

Este proyecto tiene como objetivo desarrollar una aplicación que permita recibir audio como entrada, procesarlo utilizando inteligencia artificial y generar un informe en formato PDF. La aplicación está dividida en dos partes principales: el backend y el frontend.

## Estructura del Proyecto

### Backend
- **app.py**: Punto de entrada de la aplicación Flask, configura las rutas y la aplicación.
- **api/**: Contiene las rutas de la API para manejar las solicitudes relacionadas con la generación de informes.
- **core/**: Incluye la configuración y el sistema de logging de la aplicación.
- **services/**: Contiene la lógica para la ingesta de audio, preprocesamiento, transcripción, generación de embeddings, procesamiento de lenguaje natural y generación de informes en PDF.
- **models/**: Define los modelos de datos utilizados en la aplicación.
- **database/**: Maneja la conexión a la base de datos y las migraciones.
- **utils/**: Incluye funciones utilitarias como validadores y manejo de almacenamiento de archivos.
- **tests/**: Contiene pruebas para asegurar la funcionalidad del backend.
- **requirements.txt**: Lista las dependencias necesarias para el backend.

### Frontend
- **package.json**: Configuración de npm que lista las dependencias y scripts del frontend.
- **vite.config.js**: Configuración para Vite, el bundler utilizado en el frontend.
- **index.html**: Página principal de la aplicación frontend.
- **src/**: Contiene los componentes de Vue, la lógica de la aplicación y los estilos.
  - **main.js**: Punto de entrada de la aplicación Vue.
  - **App.vue**: Componente raíz de la aplicación.
  - **api/**: Maneja las solicitudes HTTP al backend.
  - **components/**: Incluye componentes como grabador de audio, panel de subida, vista previa del informe y botón de descarga.
  - **store/**: Maneja el estado global de la aplicación utilizando Vuex.
  - **styles/**: Contiene los estilos globales de la aplicación.

### Machine Learning
- **model_loader.py**: Carga el modelo de machine learning.
- **inference.py**: Maneja la inferencia utilizando el modelo cargado.
- **training/**: Contiene la lógica para entrenar el modelo y manejar los datos de entrenamiento.

### Scripts
- **run_dev.sh**: Script para iniciar el entorno de desarrollo.
- **init_db.py**: Inicializa la base de datos.
- **export_sample_report.py**: Genera un informe de muestra.

### Configuración
- **.env.example**: Ejemplo de archivo de configuración de variables de entorno.
- **settings.yaml**: Configuraciones adicionales en formato YAML.

### Docker
- **backend.Dockerfile**: Define la imagen Docker para el backend.
- **frontend.Dockerfile**: Define la imagen Docker para el frontend.
- **docker-compose.yml**: Orquesta la ejecución de múltiples contenedores Docker.

## Instalación

1. Clona el repositorio.
2. Navega al directorio del backend y ejecuta `pip install -r requirements.txt` para instalar las dependencias.
3. Configura las variables de entorno en un archivo `.env`.
4. Inicializa la base de datos ejecutando `python scripts/init_db.py`.
5. Inicia el servidor backend ejecutando `python backend/app.py`.
6. Navega al directorio del frontend y ejecuta `npm install` para instalar las dependencias.
7. Inicia el servidor frontend ejecutando `npm run dev`.

## Uso

- Graba o sube un archivo de audio a través de la interfaz gráfica.
- El sistema procesará el audio y generará un informe en formato PDF que podrás descargar.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cambios o mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT.