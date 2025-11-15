# Mi Proyecto de Red Neuronal

Este proyecto tiene como objetivo desarrollar una aplicación que utiliza una red neuronal para generar informes específicos en formato PDF a partir de un auidio grabado en la aplicacion. La aplicación clasifica y distingue dimensiones específicas y genera nuevos textos basados en la entrada proporcionada.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
mi-proyecto-red-neuronal
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── neural_network
│   │   └── model.py           # Definición de la red neuronal
│   ├── pdf_generator
│   │   └── generator.py       # Generación de informes en PDF
│   ├── database
│   │   └── db.py              # Manejo de la base de datos
│   ├── interface
│   │   └── ui.py              # Interfaz de usuario
│   └── utils
│       └── helpers.py         # Funciones auxiliares
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación del proyecto
└── .gitignore                 # Archivos a ignorar por Git
```

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/Trivii1457/Neural_Ases.git
   cd Neural_Ases
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:
   ```
   python src/main.py
   ```

2. Ingresa el texto plano en la interfaz de usuario.

3. La aplicación procesará el texto, clasificará las dimensiones y generará un informe en formato PDF.

## Arquitectura

- **Red Neuronal**: Implementada en `src/neural_network/model.py`, esta clase se encarga de entrenar el modelo y realizar predicciones.
- **Generación de PDF**: La clase `PDFGenerator` en `src/pdf_generator/generator.py` se encarga de crear y guardar los informes.
- **Base de Datos**: `src/database/db.py` maneja la conexión y las operaciones de almacenamiento y recuperación de datos.
- **Interfaz de Usuario**: Implementada en `src/interface/ui.py`, permite la interacción con el usuario.
- **Funciones Auxiliares**: `src/utils/helpers.py` contiene funciones que facilitan diversas tareas en el proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.