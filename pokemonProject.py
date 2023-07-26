import requests

while True:
    pokemon = input("Find your favorite Pokemon: ")
    pokemon = pokemon.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    req = requests.get(url)

    if req.status_code == 200:
        data = req.json()
        print(f"Name is: {data['name']}")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found")


