import torch
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM

def load_model():
    print("Cargando el modelo...")
    # token = "hugging token if needed"
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    # Necesario para modelos tipo GPT2
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    return model, tokenizer


def generate_response(prompt, model, tokenizer):
    try:
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(model.device)

        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=300,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
          #  top_k=50,
            repetition_penalty=1.3,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
        #outputs = model.generate(
        #    inputs["input_ids"],
        #    max_new_tokens=300,  # Solo cuenta los tokens generados, no el prompt
        #    do_sample=True,  # Sampling en lugar de greedy decoding
        #    temperature=0.7,  # Controla la creatividad
        #    top_p=0.9,        # Top-p sampling (nucleus sampling)
        #    repetition_penalty=1.3,  # Penaliza repeticiones
        #    pad_token_id=tokenizer.eos_token_id,  # Evita warnings
        #    eos_token_id=tokenizer.eos_token_id  # Para cortar de forma natural
        # )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    except Exception as e:
        print(f"Error durante la generación: {e}")
        return "Lo siento, hubo un error procesando tu solicitud."


if __name__ == "__main__":
    print(f"CUDA disponible: {torch.cuda.is_available()}")
    print(f"Dispositivo actual: {'cuda' if torch.cuda.is_available() else 'cpu'}")

    model, tokenizer = load_model()
    if model is None or tokenizer is None:
        print("La carga del modelo falló. Saliendo.")
    else:
        print("Modelo cargado exitosamente.")
        prompt = "¿Cuál es la capital de España?"
        respuesta = generate_response(prompt, model, tokenizer)
        print(f"Respuesta de prueba: {respuesta}")
