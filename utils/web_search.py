import requests

def search_google(query):
    api_key = 'tu_api_key'  # Necesitarás una API key de Google Custom Search
    search_engine_id = 'tu_search_engine_id'
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    response = requests.get(url)
    return response.json()
