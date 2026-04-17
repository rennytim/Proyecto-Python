# Proyecto Python - Chat con Llama 3.3 usando Groq

Este repositorio contiene un asistente de chat en consola construido en Python que se conecta a la API de Groq para interactuar con el modelo `llama-3.3-70b-versatile`.

## Descripción

`Proyecto.py` implementa una aplicación REPL (Read-Eval-Print Loop) donde el usuario ingresa mensajes en la terminal y recibe respuestas generadas por el modelo de lenguaje.

El programa está pensado como proyecto universitario para la asignatura de Análisis de Sistemas en la Universidad Centroccidental Lisandro Alvarado.

## Requisitos

- Python 3.10 o superior
- Paquete `groq`
- Clave de API de Groq

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:

```bash
pip install groq
```

3. Configura tu variable de entorno con la clave de Groq:

En Windows PowerShell:

```powershell
$env:GROQ_API_KEY = "TU_API_KEY_AQUI"
```

En Windows CMD:

```cmd
set GROQ_API_KEY=TU_API_KEY_AQUI
```

## Uso

Ejecuta el script principal:

```bash
python Proyecto.py
```

Durante la ejecución podrás ingresar tus mensajes. Escribe `salir`, `exit` o `quit` para cerrar la aplicación.

## Estructura del repositorio

- `Proyecto.py` - Script principal del chat con el modelo Groq.
- `recursos/` - Carpeta para archivos adicionales o de apoyo.

## Notas

- Asegúrate de no subir tu clave de API a repositorios públicos.
- Si la variable `GROQ_API_KEY` no está configurada, el programa mostrará una advertencia y no intentará ejecutar la consulta.
