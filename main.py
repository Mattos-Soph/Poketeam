import requests 

print("PokéTeam iniciado!")
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

resposta = requests.get(url)

dados = resposta.json()

nome = dados["name"]
altura = int(dados["height"])
peso = int(dados["weight"])

print(f"Nome: {nome}")
print(f"Altura: {altura / 10} m")
print(f"Peso: {peso / 10} kg")

print(f"Seu pokémon é do tipo: {dados["types"][0]["type"]["name"]}")