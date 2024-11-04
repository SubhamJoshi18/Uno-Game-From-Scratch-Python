import random
from typing import List
from Constant.index import random_deck



def randomize_nine_card(deck:List[int]) -> List[int]:
     if len(deck) < 9 :
        print('Card is not sufficient')
        return []
     return random.choices(deck,k=9)




def random_90_card(num_range):
    colors = ['Red','Yellow','Blue','Green']
    cards = [[random.randint(0,14),random.choice(colors)] for _ in range(num_range)]
    return cards

def count_players(player_list:dict) -> int :
    players = []
    for item in player_list.keys():
        players.append(item)
    return len(players)