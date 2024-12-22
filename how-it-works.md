# 1. Profundización en el flujo del proyecto
## a. Captura de voz: recognition.py
Este módulo utiliza speech_recognition para capturar el audio del usuario desde el micrófono y convertirlo a texto. Aquí algunos puntos importantes:
### Cómo funciona:
1. Inicialización del reconocedor:
sr.Recognizer() es la clase que maneja el procesamiento del audio.
2. Uso del micrófono:
sr.Microphone() gestiona la entrada de audio. El bloque with asegura que el recurso (el micrófono) se libera automáticamente cuando termina su uso.
3. Reconocimiento del texto:
recognizer.recognize_google(audio, language="es-ES") utiliza la API de Google Speech para transcribir el audio a texto en español.
### Como depurar esta parte:
- Si no detecta el micrófono:
```bash
sudo apt install portaudio19-dev
pip3 install pyaudio
```
- Verifica los dispositivos de audio con:
```bash
arecord -l
```
Si no entiende el audio, asegúrate de hablar claro y que el micrófono funcione correctamente. Puedes guardar el audio para verificar:
```python
with open("audio.wav", "wb") as f:
    f.write(audio.get_wav_data())
```
