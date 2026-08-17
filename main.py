import requests 

def search_pokemon(pokemon): 
    pokemon = pokemon.strip().lower()
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
    
def show_deck(deck, title="Your Deck"):
    print(f"\n=== {title} ===")

    for position, pokemon in enumerate(deck, start=1):
        print(
            f"{position}. {pokemon['name'].capitalize()} — "
            f"{', '.join(pokemon['types'])}"
        )

print("PokéTeam Started!")
deck = []


while len(deck) < 6:
    pokemon = input("Choose a Pokémon: ")
    chosen_pokemon = search_pokemon(pokemon)

    confirm = ""

    already_in_deck = False 

    if chosen_pokemon is not None:
        for pokemon_in_deck in deck:
            if chosen_pokemon["name"] == pokemon_in_deck["name"]:
               already_in_deck = True
               print("This Pokémon is already in your deck. Please choose another one.")
               break

        if not already_in_deck:
            while confirm not in ["y", "n"]:
                confirm = input("Add this Pokémon to your deck? (y/n): ").lower()
                if confirm == "y":
                    deck.append(chosen_pokemon)
                    print(deck)
                elif confirm == "n":
                    print("Pokémon not added to your deck.")
                else: 
                    print("Invalid answer. Please type 'y' or 'n'.")

show_deck(deck)


deck_confirmed = False

while not deck_confirmed:
    choice = input("\n1 - Confirm deck\n2 - Replace a Pokémon\nChoose an option: ")

    if choice == "1":
        print("Deck confirmed!")
        deck_confirmed = True

    elif choice == "2":
        print("Let's replace a Pokémon.")

        try:
            replace_position = int(
                input("Choose the number of the Pokémon you want to replace: ")
            )

        except ValueError:
            print("Invalid option. Please type a number from 1 to 6.")
            continue 

        if replace_position < 1 or replace_position > 6:
            print("Invalid option. Please choose a number from 1 to 6.")
            continue

        index = replace_position - 1

        pokemon_to_replace = deck[index]

        print(
            f"You chose to replace {pokemon_to_replace['name'].capitalize()}."
        )
        new_pokemon_name = input("Choose the new Pokémon: ")

        new_pokemon = search_pokemon(new_pokemon_name)

        if new_pokemon is None:
            print("Replacement cancelled. Your deck was not changed.")
        else:
            already_in_deck = False

            for pokemon_in_deck in deck:
                if new_pokemon["name"] == pokemon_in_deck["name"]:
                    already_in_deck = True
                    break

            if already_in_deck:
                print("This Pokémon is already in your deck. Replacement cancelled.")
            else:
                deck[index] = new_pokemon
                print(
                    f"{pokemon_to_replace['name'].capitalize()} was replaced by "
                    f"{new_pokemon['name'].capitalize()}."
                )

                show_deck(deck, "Updated Deck")

    else:
        print("Invalid option.")

