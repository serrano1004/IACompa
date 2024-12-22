# IACompa
Compañero para la tercera edad
## Requisitos para Ubuntu 22 (es como lo hemos hecho, así que "you know" ajo y agua)
### 1. Instalar dependencias
Ejecuta los siguientes comandos para instalar todas las librerías necesarias:
```bash
sudo apt update
sudo apt install python3-pip portaudio19-dev mpg321 -y
pip3 install speechrecognition gtts torch transformers
```
### 2. Pruebas individuales de los módulos
Ejecuta los archivos por separado para probar:
```bash
python3 recognition.py: Verifica que el micrófono funciona y captura audio.
python3 model.py: Prueba la generación de texto con el modelo.
python3 app.py: Conecta todo y verifica la interacción completa.
```
### 3. Estructura del proyecto
```text
IACompa/
├── recognition.py   # Captura de voz
├── model.py         # Generación de texto
├── app.py           # Integración completa
├── requirements.txt # (Opcional) Dependencias del proyecto
```
