# Audio AI Report Frontend

Este proyecto es una interfaz gráfica para el sistema de generación de informes a partir de audio utilizando inteligencia artificial. A continuación se detallan los componentes y su funcionalidad.

## Estructura del Proyecto

- **src/**: Contiene el código fuente de la aplicación.
  - **main.js**: Punto de entrada de la aplicación Vue.
  - **App.vue**: Componente raíz de la aplicación.
  - **api/**: Módulo para manejar las solicitudes HTTP al backend.
    - **client.js**: Configuración del cliente HTTP.
  - **components/**: Componentes reutilizables de la interfaz.
    - **AudioRecorder.vue**: Componente para grabar audio.
    - **UploadPanel.vue**: Componente para subir archivos de audio.
    - **ReportPreview.vue**: Componente para mostrar una vista previa del informe generado.
    - **DownloadButton.vue**: Componente para descargar el informe en PDF.
  - **store/**: Manejo del estado global de la aplicación.
    - **index.js**: Configuración de Vuex.
  - **styles/**: Contiene los estilos globales de la aplicación.
    - **main.css**: Estilos principales.

## Instalación

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd frontend
   ```

2. Instala las dependencias:
   ```
   npm install
   ```

## Ejecución

Para iniciar la aplicación en modo de desarrollo, ejecuta:
```
npm run dev
```

La aplicación estará disponible en `http://localhost:3000`.

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.