from recognition import recognize_speech
from model import load_model, generate_response
from utils.tts import text_to_speech  # Módulo auxiliar para convertir texto a voz
from gtts import gTTS
import os

# Inicializar el modelo
model, tokenizer = load_model()

def main():
    print("Iniciando aplicación...")
    while True:
        # Capturar texto hablado
        text = recognize_speech()
        
        if text:
            # Generar respuesta con el modelo
            response = generate_response(text, model, tokenizer)
            print(f"Respuesta de la IA: {response}")
            
            # Convertir respuesta a voz
            text_to_speech(response)
        else:
            print("No se recibió entrada válida. Intentando de nuevo...")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
