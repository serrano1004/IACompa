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
- Si no entiende el audio, asegúrate de hablar claro y que el micrófono funcione correctamente. Puedes guardar el audio para verificar:
```python
with open("audio.wav", "wb") as f:
    f.write(audio.get_wav_data())
```

## b.Generación de texto: model.py
Este módulo utiliza el modelo de lenguaje bloomz de Hugging Face para generar respuestas.

###Cómo funciona:
Carga del modelo:
```python
model, tokenizer = load_model()
```
AutoTokenizer convierte el texto de entrada en tensores (valores numéricos).
AutoModelForCausalLM genera texto en base al tensor.
Generación de respuesta:
```python
outputs = model.generate(inputs["input_ids"], max_length=100)
```
Controlas el largo de la respuesta con max_length y puedes ajustar parámetros como:
- temperature: Controla la creatividad (valores entre 0.7-1.5 son útiles).
- top_p: Reduce palabras poco probables (valores cercanos a 0.9).
## Cómo optimizar:
Prueba modelos adicionales de Hugging Face como:
- Davlan/xlm-roberta-large-es-ner (enfocado en español).
- facebook/blenderbot-400M-distill (más general).
- Si tu hardware es limitado, usa versiones más ligeras. Por ejemplo:
```bash
pip3 install transformers[onnxruntime]
```

## c. Integración y síntesis de voz: app.py
Este módulo conecta todo el flujo y convierte las respuestas generadas a voz utilizando gTTS.

### Cómo funciona:
1. Captura texto hablado con recognize_speech() desde recognition.py.
2. Genera una respuesta con generate_response() desde model.py.
3. Convierte el texto de la respuesta a voz con gTTS y lo reproduce.

### Cómo depurar:
Si no se reproduce el archivo de audio, instala mpg321:
```bash
sudo apt install mpg321
```
Si la voz es muy rápida o lenta, ajusta la velocidad en gTTS:
```python
tts = gTTS(text=text, lang='es', slow=True)
```
 
