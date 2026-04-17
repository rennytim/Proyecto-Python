
import os
from groq import Groq

def iniciar_chat():
    """Inicia el chat en consola usando la API de Groq y el modelo llama-3.3-70b-versatile."""

    # 1) Cargar la clave de la API desde la variable de entorno.
    # Si no existe, usa un valor predeterminado codificado (no es buena práctica para producción).
    api_key = os.environ.get("GROQ_API_KEY", "TU_API_KEY_AQUI")
    
    # 2) Validar si el usuario dejó un marcador de posición de clave.
    if api_key == "TU_API_KEY_AQUI":
        print("Advertencia: No has configurado tu API Key.")
        print("Por favor, reemplaza 'TU_API_KEY_AQUI' en el código con tu clave de Groq.\n")
        return

    # 3) Crear el cliente para conectar con la API de Groq.
    try:
        # Inicializar el cliente Groq con la clave de API proporcionada.
        cliente = Groq(api_key=api_key)
    except Exception as e:
        # Si ocurre cualquier error durante la inicialización del cliente, capturarlo y mostrar un mensaje de error amigable.
        print(f"Error al inicializar el cliente: {e}")
        return
    
    # 4) Imprimir el encabezado de presentación del programa en la consola.
    print("")
    print("------------- ANALISIS DE SISTEMAS (UCLA) ------------")
    print("      PROYECTO LENGUAJES DE PROGRAMACION (C7)         ")
    print("-" * 54)
    print("Bienvenido al asistente de consulta basado en LLM.")
    print("Este programa te permitirá interactuar con el modelo")
    print("llama-3.3-70b-versatile para obtener respuestas a tus")
    print("preguntas.\n")
    print("== Conexión establecida con llama-3.3-70b-versatile ==\n")

    while True:
        # 5) Leer el mensaje ingresado por el usuario.
        print("Escribe tu pregunta o mensaje para el modelo:")
        print("Escribe 'salir' para terminar el programa.")
        prompt_usuario = input("Tu mensaje: ")
        
        # 6) Cerrar la aplicación si el usuario escribe un comando de salida.
        if prompt_usuario.lower() in ['salir', 'exit', 'quit']:
            print("Cerrando la conexión. ¡Hasta luego!")
            break
            
        # 7) Validar que el mensaje no esté vacío ni contenga solo espacios.
        if not prompt_usuario.strip():
            print("Por favor, ingresa un mensaje válido.\n")
            continue

        try:
            # 8) Enviar el prompt al modelo y esperar su respuesta.
            respuesta_llm = cliente.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt_usuario,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )

            # 9) Extraer el texto de la primera respuesta devuelta por el modelo.
            contenido_respuesta = respuesta_llm.choices[0].message.content

            # 11) Imprimir la respuesta del modelo en la consola.
            print(f"\n[Llama 3.3 70B]:\n{contenido_respuesta}\n")
            print("-" * 50)

        # 12) si ocurre cualquier error durante la comunicación con la API, capturarlo y mostrar un mensaje de error amigable.
        except Exception as e:
            print(f"\n[Error de comunicación]: Ocurrió un problema al procesar la solicitud: {e}\n")

if __name__ == "__main__":
    # Ejecutar la función iniciar_chat solo cuando este archivo se ejecute directamente.
    # Si el archivo se importa desde otro módulo, no se inicia el chat automáticamente.
    iniciar_chat()