import requests

user = "srikanthpragada"

resp = requests.get(f"https://api.github.com/users/{user}")
details = resp.json()  # Convert JSON to Dict
for name,value in details.items():
    print(f"{name:20} {value}")


