# IACompa
A companion for the elderly

## Requirements for Ubuntu 22 (that's how we did it, so... you know, tough luck!)

### 1. Install dependencies
Run the following commands to install all required libraries:
```bash
sudo apt update
sudo apt install python3-pip portaudio19-dev mpg321 -y
pip3 install -r requirements.txt
```

### 2. Individual module testing
Run each script individually to test:
```bash
python3 recognition.py   # Checks if the microphone works and captures audio.
python3 model.py         # Tests text generation with the model.
python3 app.py           # Connects everything and verifies full interaction.
```

### 3. Project structure
```text
IACompa/
├── __pycache__/                    # Python bytecode cache
│   ├── model.cpython-310.pyc
│   └── recognition.cpython-310.pyc
├── templates/
│   └── index.html                  # Web interface HTML
├── utils/
│   ├── __init__.py                 # Initializes the utils package
│   ├── tts.py                      # Text-to-speech synthesis
│   └── web_search.py               # Web search module
├── app_web.py                      # Web version of the integrator
├── app.py                          # Main integration script (CLI or main)
├── how-it-works.md                 # Technical or functional explanation
├── model.py                        # Text generation with model
├── recognition.py                  # Voice capture and recognition
├── README.md                       # Project documentation
├── requirements.txt                # Project dependencies
└── response.mp3                    # Example of generated voice output
```

