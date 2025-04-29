# 1. Profundización en el flujo del proyecto

## a. Captura de voz: recognition.py
Este módulo utiliza la biblioteca `speech_recognition` para captar el audio del usuario a través del micrófono y convertirlo en texto.

### Cómo funciona:
1. Usa el micrófono como fuente.
2. Espera hasta detectar voz.
3. Transcribe el audio usando la API de Google Speech Recognition.

```python
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    text = r.recognize_google(audio, language="es-ES")
```

---

## b. Generación de texto: model.py
Este módulo recibe el texto del usuario y genera una respuesta con un modelo de lenguaje (como los de Hugging Face).

```python
outputs = model.generate(
    inputs["input_ids"],
    max_new_tokens=300,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.3,
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id
)
```

### Parámetros importantes:
- `temperature`: Controla la creatividad (valores útiles entre 0.7 y 1.5).
- `top_p`: Evita palabras improbables (valores cercanos a 0.9 suelen ir bien).
- `repetition_penalty`: Penaliza repeticiones innecesarias.

### Cómo optimizar:
Puedes usar modelos alternativos de Hugging Face según tus necesidades:
- `Davlan/xlm-roberta-large-es-nER`: Mejor en español.
- `facebook/blenderbot-400M-distill`: Más general.
- Si tu equipo es limitado, instala versiones más ligeras:

```bash
pip3 install transformers[onnxruntime]
```

---

## c. Integración y síntesis de voz: app.py
Este módulo orquesta todo el flujo y convierte las respuestas generadas en voz usando gTTS.

### Cómo funciona:
1. Captura texto con `recognize_speech()` desde `recognition.py`.
2. Genera respuesta con `generate_response()` desde `model.py`.
3. Convierte el texto a voz con `gTTS` y lo reproduce.

### Cómo depurar:
- Si no se escucha la voz, instala mpg321:
```bash
sudo apt install mpg321
```

- Si la voz es muy rápida o lenta, ajusta la velocidad:
```python
tts = gTTS(text=text, lang="es", slow=True)
```

---

## d. Interfaz web (opcional): app_web.py
Ofrece una versión accesible vía navegador con HTML y Flask.

- Plantilla principal: `templates/index.html`
- Ejecuta con: `python3 app_web.py`
- Útil para probar la app desde el móvil u otros dispositivos en red local.

