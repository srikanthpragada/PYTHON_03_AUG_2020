import requests

resp = requests.get(f"https://restcountries.eu/rest/v2/all")
countries = resp.json()  # Convert array of JSON to  list of dict

countries = filter(lambda c: c['area'] is not None, countries)

for c in sorted(countries, key=lambda c: c['area'], reverse=True)[:10]:
    print(f"{c['name']:50}  {c['population']:10} {c['area']:10} {c['region']}")
