import requests
# imports the request module to allow API to be used
import random
# Imports the random module which selects random items in the Pokemon API
import time
# Sets a delay using the time module when introducing the user to the Top Trumps Game

def get_random_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/" # API requests pulled from this url
    random_num = random.randrange(1, 151) # Sets a random request between 1 and 151 to be used
    response = requests.get(url + str(random_num))
    pokemon_data = response.json()
    stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
# Once all the requests are pulled - stats are then given to the user to select from against the CPU opponent
    return {
        'name': pokemon_data['name'],
        'id': pokemon_data['id'],
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        'speed': stats.get('speed'),
        'attack': stats.get('attack'),
    }

# This block allows the random stats to be compared between the user (us) and the CPU opponent
def compare_stats(player, opponent, stat):
    if player[stat] > opponent[stat]: # utilising the if/else statements to compare the stats and return different messages
        return 'Player wins!'
    elif player[stat] < opponent[stat]:
        return 'Opponent wins!'# if the opponent stat is a greater number than the user stat
    else:
        return 'It\'s a draw!' # if the randomly generated number is the same, a draw message will be returned

# This block keeps a tally of the score - our game acts in a loop so each game score can be added to the running tally
def run():
    player_score = 0
    opponent_score = 0
# Introduction to the game message and the instructions to generate a card
    print("Hello!")
    print("Welcome to Top Trumps!")
    time.sleep(1) # delays the beginning of the game by 1 second

    while True:
        input("Press enter to generate a card...")
        print("Getting you a random pokemon card")
        print("------------")
        time.sleep(1)

        player_pokemon = get_random_pokemon()
        opponent_pokemon = get_random_pokemon()
# Returns the randomised pokemon pulled from the API url
        print("Your Pokemon is {}\n".format(player_pokemon["name"]))
        print(f'Player Pokemon: {player_pokemon}')
        time.sleep(0.5)
# Gives the user the option to select which stat they want to use against their opponent
        stat = input('Which stat do you want to use (id, height, weight, speed, attack)?')

        print("------------")
        print("Your opponents Pokemon was {}\n".format(opponent_pokemon["name"]))
        print(f'Opponent Pokemon: {opponent_pokemon}')

        result = compare_stats(player_pokemon, opponent_pokemon, stat)
# Adds the score to the running tally after comparing the stats between the user and opponents
        if result == 'Player wins!':
            player_score += 1
        elif result == 'Opponent wins!':
            opponent_score += 1

        print(result)
        time.sleep(0.5)
# Sends the overall score and number of games back to the user at the end
        print("------------")
        print("So far you have won {} games...".format(player_score))
        print("Your opponent has won {} games...".format(opponent_score))
        print(f'Player Score: {player_score}, Opponent Score: {opponent_score}')
# Loop block to allow user to either play again or not. If user selects no, the code breaks and ends.
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

run()
# runs the game