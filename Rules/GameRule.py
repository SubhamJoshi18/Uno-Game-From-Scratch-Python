from typing import List,Any
from Exceptions.index import GameRuleException
import copy

from Rules.GameInstruction import GameMethods


def game_rule_with_cards(players_card:List[List[int]],left_cards) -> Any :
    original_card = []
    try:
        players_count = len(players_card)
        for index , player in enumerate(players_card):
            players_sign = index + 1
            player_num = f'Player - {players_sign}'
            player_card = copy.deepcopy(player)
            print(f'{player_num} : {player_card }')
            original_card.append(players_card)

        match players_count:

            case 2:
                game_instruction_instance = GameMethods()
                game_instruction_instance.handle_game_deck(players_card[0],players_card[1],left_cards)

            case _:
                print('Player Count Does not match')


    except (GameRuleException,Exception) as game_rule_error:
        print(f'Error in game rule exception : {game_rule_error}')