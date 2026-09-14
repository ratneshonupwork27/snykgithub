import requests

# ❌ EXPOSED SECRETS: Anyone with access to the file can see these
API_TOKEN = "sk_live_51Nx92KLmZ091873jHkdalqi8912301823"
DB_PASSWORD = "super_secret_db_password_2026"

def fetch_user_data():
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    # Vulnerable implementation tracking plain text credentials
    response = requests.get("https://example.com", headers=headers)
    return response.json()
