import requests 

def search_pokemon(pokemon): 
    print(f"Searching {pokemon}...")

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    result = requests.get(url)

    if result.status_code == 200: 
        print("We have your pokémon here!")
        data = result.json()
        
        name = data["name"]
        height = int(data["height"])
        weight = int(data["weight"])
        types = []

        print(f"Name: {name}")
        print(f"Height: {height / 10} m")
        print(f"Weight: {weight / 10} kg")
        
        for atype in data["types"]: 
            types.append(atype["type"]["name"])
        print(f"Your Pokémon type(s) is/are: {", ".join(types)}")

    else:
        print("Yeah, we don't have it...")

print("PokéTeam Started!")
pokemon = input("Choose a Pokémon: ")
search_pokemon(pokemon)




