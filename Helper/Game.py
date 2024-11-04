from abc import ABC,abstractmethod
from Exceptions.index import PursueGameException
from Libs.logger import uno_logger
from Rules.GameRule import game_rule_with_cards


class GameUnoAbs(ABC):

    @abstractmethod
    def pursue_game(self,no_of_player,left_card,distribute_card_with_player):
        pass



class GameUno(GameUnoAbs,ABC):

    def __init__(self):
        pass



    def pursue_game(self,no_of_player,left_card,distribute_card_with_player):
        try:
            players = []
            print('This is a no of player',no_of_player)
            for  player , player_card in distribute_card_with_player.items():
                if iter(player_card) and isinstance(player_card,list):
                    players.append(player_card)

            game_rule_with_cards(players_card=[item for sublist in players for item in sublist],left_cards=left_card)

        except (PursueGameException,Exception) as pursue_game:
            uno_logger.error(f'Error in Pursuing game  : {pursue_game}')

