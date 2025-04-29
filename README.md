# IACompa
Compañero para la tercera edad

## Requisitos para Ubuntu 22 (es como lo hemos hecho, así que "you know" ajo y agua)

### 1. Instalar dependencias
Ejecuta los siguientes comandos para instalar todas las librerías necesarias:
```bash
sudo apt update
sudo apt install python3-pip portaudio19-dev mpg321 -y
pip3 install -r requirements.txt
```

### 2. Pruebas individuales de los módulos
Ejecuta los archivos por separado para probar:
```bash
python3 recognition.py   # Verifica que el micrófono funciona y captura audio.
python3 model.py         # Prueba la generación de texto con el modelo.
python3 app.py           # Conecta todo y verifica la interacción completa.
```

### 3. Estructura del proyecto
```text
IACompa/
├── __pycache__/                    # Caché de Python
│   ├── model.cpython-310.pyc
│   └── recognition.cpython-310.pyc
├── templates/
│   └── index.html                  # Interfaz web HTML
├── utils/
│   ├── __init__.py                 # Inicializa el paquete utils
│   ├── tts.py                      # Síntesis de texto a voz
│   └── web_search.py               # Módulo de búsqueda en la web
├── app_web.py                      # Versión web del integrador
├── app.py                          # Integración completa (CLI o principal)
├── how-it-works.md                 # Explicación técnica o funcional
├── model.py                        # Generación de texto con modelo
├── recognition.py                  # Captura y reconocimiento de voz
├── README.md                       # Documentación del proyecto
├── requirements.txt                # Dependencias del proyecto
└── response.mp3                    # Salida de voz generada (ejemplo)
```