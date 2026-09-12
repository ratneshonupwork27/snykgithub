import requests

# ❌ INSECURE: The secret token is hardcoded and exposed to anyone reading the code
API_TOKEN = "sk_live_51NzABC123XYZSecretKeyThatIsExposed" 

def fetch_user_data(user_id):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(f"https://example.com{user_id}", headers=headers)
    return response.json()
