# WARNING: Insecure implementation
import requests

def fetch_user_data():
    # EXPOSED SECRET: The private API key is hardcoded directly into the file
    API_KEY = "sk_live_51NzM82LkWm91JqQz98u76543210vBnzXy" 
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get("https://example.com", headers=headers)
    return response.json()

if __name__ == "__main__":
    print(fetch_user_data())
