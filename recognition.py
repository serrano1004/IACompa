import speech_recognition as sr

def recognize_speech():
    # Inicializar el reconocimiento
    recognizer = sr.Recognizer()
    
    # Usar el micrófono como fuente
    with sr.Microphone() as source:
        print("Por favor, habla ahora...")
        
        try:
            # Escuchar el audio del usuario
            audio = recognizer.listen(source)
            
            # Reconocer el texto (configurado para español de España)
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {text}")
            return text

        except sr.UnknownValueError:
            print("No se pudo entender lo que dijiste.")
            return None
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de reconocimiento: {e}")
            return None

# Solo para pruebas locales
if __name__ == "__main__":
    recognize_speech()
