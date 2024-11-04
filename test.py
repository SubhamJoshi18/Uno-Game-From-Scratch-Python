import random

def __distribute_evenly_card(no_of_player):
    colors = ['Blue', 'Yellow', 'Green', 'Red']
    player_list = {}
    for index in range(no_of_player):
        # Generate 9 random numbers with an assigned color as a pair
        cards = [[random.randint(0, 10), random.choice(colors)] for _ in range(9)]

        player_list[f'Player {index + 1}'] = [cards, 0]  # Initialize score as 0

    return player_list

result = __distribute_evenly_card(2)
print(result)
