from flask import Flask, render_template, request
import model, transformers 
from utils.tts import text_to_speech

app = Flask(__name__)
model, tokenizer = model.load_model()
assert model is not None, "El modelo no se ha cargado correctamente."
assert tokenizer is not None, "El tokenizer no se ha cargado correctamente."

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if not isinstance(model, transformers.T5ForConditionalGeneration):
        raise Exception("Loaded model is not T5ForConditionalGeneration")
    if request.method == "POST":
        text = request.form["user_input"]
        response = model.generate_response(text, model, tokenizer)
        text_to_speech(response) # Reproducir el audio
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

