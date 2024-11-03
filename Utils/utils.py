import random
from typing import List
from Constant.index import random_deck



def randomize_nine_card(deck:List[int]) -> List[int]:
     if len(deck) < 9 :
        print('Card is not sufficient')
        return []
     return random.choices(deck,k=9)




def random_90_card(num_range):
    result = []
    for x in range(num_range):
        if x > 14:
            new_num = random.randint(0,14)
            result.append(new_num)
        else:
            result.append(x)
    return result