from recognition import recognize_speech
from model import load_model, generate_response
from gtts import gTTS
import os

# Inicializar el modelo
model, tokenizer = load_model()

def text_to_speech(text):
    # Convertir texto a voz con Google TTS
    tts = gTTS(text=text, lang='es')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # Reproducir el archivo de audio

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
