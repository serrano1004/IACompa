from gtts import gTTS
from io import BytesIO  # Importar BytesIO
from playsound import playsound
import os

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='es', slow=False)
        # Usar BytesIO para evitar guardar archivos innecesariamente (opcional)
        #fp = BytesIO()
        #tts.write(fp)
        #fp.seek(0)
        tts.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3") # Eliminar el archivo después de reproducirlo (opcional)
    except Exception as e:
        print(f"Error en text_to_speech: {e}")
        return