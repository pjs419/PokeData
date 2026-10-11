'''Pokemon data project using PokeAPI

  This project will fetch and display data about various Pokemon from the PokeAPI.
'''

import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(pokemon_name):
  url = f"{base_url}pokemon/{pokemon_name.lower()}" # Construct the URL for the API request
  response = requests.get(url, timeout=10) # Make the GET request to the PokeAPI with a timeout of 10 seconds

  if response.status_code == 200:
    return response.json()
  return None

def display_pokemon_data(pokemon_data):
  if pokemon_data:
    # Display the Pokemon's data
    name = pokemon_data['name']
    height = pokemon_data['height']
    weight = pokemon_data['weight']
    types = [t['type']['name'] for t in pokemon_data['types']]
    
    print(f"Name: {name.capitalize()}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Types: {', '.join(types)}")
  else:
    print("No data to display.")

def main():
  print("Welcome to the Pokemon lookup!")

  while True:
    pokemon_name = input("\nEnter the name of the Pokemon, or type 'quit' to exit: ").strip()

    if pokemon_name.lower() in {"quit", "q"}:
      print("Goodbye!")
      break

    if not pokemon_name:
      print("Please enter a Pokemon name.")
      continue

    # Fetch and display Pokemon data
    pokemon_data = get_pokemon_data(pokemon_name)

    if pokemon_data: # If data is found, display it
      display_pokemon_data(pokemon_data)
    else:
      print(f"No Pokemon found named '{pokemon_name}'.")
      choice = input("Would you like to search again or quit? (again/quit): ").strip().lower()

      if choice in {"quit", "q"}:
        break

  print("Goodbye!")

# Run the main function if this script is executed directly
if __name__ == "__main__":
  main()
