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

        pokemon_data = {
            "name": name,
            "types": types,
        }

        return pokemon_data

    else:
        print("Yeah, we don't have it...")
        return None

print("PokéTeam Started!")
deck = []

while len(deck) < 6:
    pokemon = input("Choose a Pokémon: ")
    chosen_pokemon = search_pokemon(pokemon)

    if chosen_pokemon is not None:
        confirm = input("Add this Pokémon to your deck? (y/n): ")
        if confirm.lower() == "y":
            deck.append(chosen_pokemon)
            print(deck)
        elif confirm.lower() == "n":
            print("Pokémon not added to your deck.")
        else: 
            print("Invalid answer. Please type 'y' or 'n'.")

    break



