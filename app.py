from recognition import recognize_speech
from model import load_model, generate_response
from utils.tts import text_to_speech
import time

# Inicializar el modelo (solo una vez)
model, tokenizer = load_model()

def main():
    print("Iniciando aplicación...")
    text_to_speech("Hola, estoy aquí para conversar. ¿De qué te gustaría hablar hoy?")  # Saludo general
    while True:
        text = recognize_speech()

        if text:
            # Generación de la respuesta con el modelo (sin lógica específica):
            prompt = f"Eres un experto en trabajo social y psicólogo. Además experto en personas de la tercera edad. Vas a conversar con una persona mayor:\nUsuario: {text}\nAsistente:"
            response = generate_response(prompt, model, tokenizer)

            print(f"Respuesta de la IA: {response}")
            text_to_speech(response)
        elif text == "": # Si no detecta audio
            print("No se detecta audio. Intentando de nuevo...")
            time.sleep(1)
        elif text is None:
            print("Error en el reconocimiento de voz.")
            time.sleep(1)
        else:
            print("No se recibió entrada válida. Intentando de nuevo...")
            time.sleep(1)

    if __name__ == "__main__":
        main()