import random

# Dictionary containing Generation 1 Pokemon information
gen1_pokemon_info = {
    "Bulbasaur": {"Type": ["Grass", "Poison"], "Habitat": "Grassland", "Colors": ["Green"], "Evolution Stage": "Basic", "Height": "0.7 m", "Weight": "6.9 kg"},
    "Ivysaur": {"Type": ["Grass", "Poison"], "Habitat": "Grassland", "Colors": ["Green"], "Evolution Stage": "Stage 1", "Height": "1.0 m", "Weight": "13.0 kg"},
    "Venusaur": {"Type": ["Grass", "Poison"], "Habitat": "Grassland", "Colors": ["Green"], "Evolution Stage": "Stage 2", "Height": "2.0 m", "Weight": "100.0 kg"},
}

def play_game():
    pokemon_name = random.choice(list(gen1_pokemon_info.keys()))
    pokemon_info = gen1_pokemon_info[pokemon_name]
    guessed = False
    attempts = 0

    print("Welcome to the Gen 1 Pokemon guessing game!")
    print("I've chosen a Pokemon, can you guess which one it is?")

    while not guessed:
        print("\nHere are some clues:")
        print("1. This Pokemon has types:", ', '.join(pokemon_info["Type"]))
        print("2. This Pokemon lives in:", pokemon_info["Habitat"])
        print("3. This Pokemon comes in the color(s):", ', '.join(pokemon_info["Colors"]))
        print("4. This Pokemon is in the", pokemon_info["Evolution Stage"])
        print("5. This Pokemon's height is:", pokemon_info["Height"])
        print("6. This Pokemon's weight is:", pokemon_info["Weight"])

        guess = input("\nEnter your guess: ").strip().capitalize()

        if guess == pokemon_name:
            print("Congratulations! You've guessed the Pokemon correctly!")
            print("It took you {} attempts.".format(attempts))
            guessed = True
        else:
            print("Incorrect! Try again.")
            attempts += 1

if __name__ == "__main__":
    play_game()
