import requests

def search_google(query):
    api_key = 'api-key'  # Reemplaza con tu API key real
    search_engine_id = 'tu_search_engine_id'  # Reemplaza con tu ID de motor de búsqueda
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza una excepción para códigos de estado HTTP erróneos (4xx o 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la búsqueda de Google: {e}")
        return None  # Devuelve None en caso de error