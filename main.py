import requests 

print("PokéTeam iniciado!")
pokemon = input("Choose a Pokémon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

resposta = requests.get(url)

if resposta.status_code == 200: 
    print("We have your pokémon here!")
    dados = resposta.json()
    
    nome = dados["name"]
    altura = int(dados["height"])
    peso = int(dados["weight"])
    tipos = []

    print(f"Nome: {nome}")
    print(f"Altura: {altura / 10} m")
    print(f"Peso: {peso / 10} kg")
    
    for tipo in dados["types"]: 
        tipos.append(tipo["type"]["name"])
    print(f"Seu pokémon tem tipo(s): {", ".join(tipos)}")

else:
    print("Yeah, we don't have it...")
