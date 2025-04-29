# 1. Deep Dive into the Project Workflow

## a. Voice Capture: recognition.py
This module uses the `speech_recognition` library to capture the user's audio through the microphone and convert it into text.

### How it works:
1. Uses the microphone as the source.
2. Waits until it detects voice.
3. Transcribes the audio using the Google Speech Recognition API.

```python
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    text = r.recognize_google(audio, language="es-ES")
```

---

## b. Text Generation: model.py
This module receives the user's text and generates a response using a language model (such as those from Hugging Face).

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

### Key Parameters:
- `temperature`: Controls creativity (useful values range between 0.7 and 1.5).
- `top_p`: Avoids improbable words (values close to 0.9 work well).
- `repetition_penalty`: Penalizes unnecessary repetitions.

### How to Optimize:
You can use alternative Hugging Face models based on your needs:
- `Davlan/xlm-roberta-large-es-nER`: Better for Spanish.
- `facebook/blenderbot-400M-distill`: More general.
- If your hardware is limited, install lighter versions:

```bash
pip3 install transformers[onnxruntime]
```

---

## c. Integration and Voice Synthesis: app.py
This module orchestrates the entire workflow and converts the generated responses into voice using gTTS.

### How it works:
1. Captures text with `recognize_speech()` from `recognition.py`. 
2. Generates a response with  `generate_response()` from `model.py`.
3. Converts the text to speech with `gTTS` and plays it.

### How to Debug:
- If the voice is not audible, install mpg321:
```bash
sudo apt install mpg321
```

- If the voice is too fast or slow, adjust the speed:
```python
tts = gTTS(text=text, lang="es", slow=True)
```

---

## d. Web Interface (Optional): app_web.py
Provides an accessible version via a web browser using HTML and Flask.

- Main template: `templates/index.html`
- Run with: `python3 app_web.py`
- Useful for testing the app from mobile or other devices on the local network.

