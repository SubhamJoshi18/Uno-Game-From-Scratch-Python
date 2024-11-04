import copy
from abc import ABC,abstractmethod

class GameInstructionAbs(ABC):

    @abstractmethod
    def handle_game_deck(self,player1_card,player2_card):
        pass



class GameInstruction(GameInstructionAbs,ABC):


    def __init__(self):
        pass


    def handle_game_deck(self,player1_card,player2_card):
        player_1 = copy.deepcopy(player1_card)
        player_2 = copy.deepcopy(player2_card)

        for card1,card2 in zip(player_1,player_2):
            print(f'Player1 Turn, Card Left for Player  {len(player_1)}')
            print(card1)
            print(f'Player2 Turn, Card Left for Player  {len(player_2)}')
            print(card2)

