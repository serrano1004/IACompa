from transformers import T5ForConditionalGeneration, AutoModelForCausalLM, AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def load_model():
    try:
        print("Cargando el modelo...")
        model_name = "google/flan-t5-base" # o tu modelo
        print(f"Intentando cargar el modelo: {model_name}")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        print("Tokenizer cargado.")
        model = T5ForConditionalGeneration.from_pretrained(model_name).to('cuda' if torch.cuda.is_available() else 'cpu')
        print("Modelo cargado en:", model.device)
        return model, tokenizer
    except OSError as e:
        print(f"Error al cargar el modelo (OSError): {e}")
        return None, None
    except Exception as e:
        print(f"Error inesperado al cargar el modelo: {e}")
        return None, None

if __name__ == "__main__":
    print(f"CUDA disponible: {torch.cuda.is_available()}")
    print(f"Dispositivo actual: {'cuda' if torch.cuda.is_available() else 'cpu'}")
    model, tokenizer = load_model()
    if model is None or tokenizer is None:
        print("La carga del modelo falló. Saliendo.")
    else:
        print("Modelo cargado exitosamente.")
        prompt = "Traduce esto al inglés: Hola, ¿cómo estás?"
        input_ids = tokenizer(prompt, return_tensors="pt").to(model.device)
        try:
            outputs = model.generate(input_ids)
            decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"Respuesta de prueba: {decoded}")
        except Exception as e:
            print(f"Error durante la generación: {e}")


def load_model():
    print("Cargando el modelo...")
    # Modelo especializado (CRUCIAL):
    # model_name = "facebook/bart-large-cnn" # Un modelo más potente para tareas conversacionales y de resumen.
    model_name = "google/flan-t5-base" # Ligero y con buen rendimiento para pruebas
    # model_name = "flax-community/t5-base-cnn-dm" # Otra opción muy potente.
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    # model = AutoModelForCausalLM.from_pretrained(model_name).to('cuda' if torch.cuda.is_available() else 'cpu')
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to('cuda' if torch.cuda.is_available() else 'cpu')
    model = T5ForConditionalGeneration.from_pretrained(model_name).to('cuda' if torch.cuda.is_available() else 'cpu')
    return model, tokenizer


def generate_response(prompt, model, tokenizer):
    try:
        # Preparar entrada y mover al mismo dispositivo que el modelo
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(model.device)

        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=300,  # Solo cuenta los tokens generados
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            top_k=40,  # Limita a las 40 opciones más probables antes de aplicar top_p
            repetition_penalty=1.2,
            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            early_stopping=True
        )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    except Exception as e:
        print(f"Error durante la generación: {e}")
        return "Lo siento, hubo un error procesando tu solicitud."
