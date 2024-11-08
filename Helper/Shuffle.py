import math
from abc import ABC,abstractmethod
import random
from Exceptions.index import UnoShuffleException
from Libs.logger import uno_logger
from Constant.index import max_uno_card
from Utils.utils import random_90_card, count_players
from Helper.Game import GameUno
from queue import Queue

game_finished_queue = Queue()



class UnoAbs(ABC):
    @abstractmethod
    def shuffle_card(self):
        pass

class Uno(UnoAbs,ABC):
    no_of_player = None
    def __init__(self,no_of_player):
        self.no_of_player = no_of_player
        self.shuffle_card()


    def start_game(self):
        pass

    def shuffle_card(self):
        try:
            if str(self.no_of_player).startswith('0') or self.no_of_player < 2:
                raise UnoShuffleException('No of Player is not enough to start the game')
            distribute_card ,card_evenly  = self.__calculate_deck()
            print('This is the random {} card in the Deck'.format(distribute_card))
            count_player = count_players(card_evenly)
            randomized_cards = random_90_card(num_range=distribute_card)


        except (UnoShuffleException,Exception) as shuffle_error:
            uno_logger.error(f'Error while Shuffling An : {shuffle_error}')

        else:
            game_uno_instance = GameUno()
            game_uno_instance.pursue_game(no_of_player=count_player,left_card=randomized_cards,distribute_card_with_player=card_evenly)

        finally:
            while not game_finished_queue.empty():
                print('Game is Going on.....')
            else:
                print('Game is Finished')

    def __distribute_evenly_card(self,no_of_player):
        colors = ['Blue','Yellow','Green','Red']
        player_list = {}
        for index in range(no_of_player):
            cards = [[random.randint(0,10), random.choice(colors)] for _ in range(9)]
            player_list[f'Player {index + 1}'] = [cards]

        return player_list

    def __calculate_deck(self):
        distribute_card = math.ceil(math.fabs(max_uno_card - 9 * int(self.no_of_player)))
        card_evenly = self.__distribute_evenly_card(no_of_player=self.no_of_player)
        print(f'Distributed Card For {self.no_of_player} and remaining card in the deck is {distribute_card}')
        return distribute_card , card_evenly
