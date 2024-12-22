from transformers import AutoModelForCausalLM, AutoTokenizer

# Cargar el modelo preentrenado en español
def load_model():
    print("Cargando el modelo...")
    model_name = "bigscience/bloomz"  # Modelo enfocado en español
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_response(prompt, model, tokenizer):
    # Codificar el texto de entrada
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generar respuesta
    outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
    
    # Decodificar y devolver
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Solo para pruebas locales
if __name__ == "__main__":
    model, tokenizer = load_model()
    prompt = "Hola, ¿cómo estás hoy? Estoy aquí para ayudarte."
    response = generate_response(prompt, model, tokenizer)
    print(f"Respuesta del modelo: {response}")
