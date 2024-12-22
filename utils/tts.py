from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='es', slow=False)  # Ajusta la velocidad según lo necesario
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # Reproduce el archivo de audio
