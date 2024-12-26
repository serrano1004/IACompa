from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "bigscience/bloomz"  # Modelo enfocado en español

import torch

def load_model():
    print("Cargando el modelo...")
    model_name = "distilgpt2"  # O el nombre de tu modelo
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name).to('cuda' if torch.cuda.is_available() else 'cpu')
    return model, tokenizer

def generate_response(prompt, model, tokenizer):
    try:
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(model.device)
        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_length=200,  # Aumentar aún más la longitud máxima
            num_return_sequences=1,
            pad_token_id=tokenizer.pad_token_id,
            do_sample=True,
            top_p=0.85,  # Reducir top_p para mayor coherencia
            top_k=30,  # Reducir top_k para mayor coherencia
            temperature=0.6,  # Reducir temperature para mayor coherencia
            repetition_penalty=1.3,  # Aumentar la penalización por repetición
            early_stopping=True # Detener la generación cuando se alcanza el EOS token
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        print(f"Error durante la generación: {e}")
        return "Lo siento, hubo un error procesando tu solicitud."

# Solo para pruebas locales
if __name__ == "__main__":
    model, tokenizer = load_model()
    prompt = "Hola, ¿cómo estás hoy? Estoy aquí para ayudarte."
    response = generate_response(prompt, model, tokenizer)
    #response = generate_response(text, model, tokenizer)

