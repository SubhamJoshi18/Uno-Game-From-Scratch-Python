import copy
import random
from Utils.utils import random_90_card

class GameMethods:

    def handle_game_deck(self, player1_card, player2_card, randomized_cards):
        print("Initial Player 1 Deck:", player1_card)
        print("Initial Player 2 Deck:", player2_card)
        print("Randomized Cards Deck:", randomized_cards)


        player_1 = copy.deepcopy(player1_card)
        player_2 = copy.deepcopy(player2_card)

        if isinstance(player_1, list) and player_1:
            print(f'Player 1 Deck Size: {len(player_1)} is valid')
        if isinstance(player_2, list) and player_2:
            print(f'Player 2 Deck Size: {len(player_2)} is valid')


        while player_1 and player_2:
            card1 = player_1[0]
            card2 = player_2[0]
            card1_number, card1_color = card1
            card2_number, card2_color = card2

            if self.__match_color_condition(card1_color, card1_number, card2_number, card2_color):
                removed_card_player_1 = player_1.pop(0)
                removed_card_player_2 = player_2.pop(0)
                print('Player 1 removed card:', removed_card_player_1)
                print('Player 2 removed card:', removed_card_player_2)
            else:

                if not randomized_cards:
                    print('Randomized Card Deck is empty. Replenishing...')
                    randomized_cards = random_90_card(90)

                new_card_for_player_1 = randomized_cards.pop()
                new_card_for_player_2 = randomized_cards.pop()
                print('New card for Player 1:', new_card_for_player_1)
                print('New card for Player 2:', new_card_for_player_2)

                player_1.append(new_card_for_player_1)
                player_2.append(new_card_for_player_2)


            if not player_1 or not player_2:
                print("Game over!")
                winner = "Player 1" if player_1 else "Player 2"
                print(f"{winner} wins!")
                break

    def __match_color_condition(self, card1_color, card1_number, card2_number, card2_color):
        # Compare if the colors match between both cards
        if card1_color == card2_color:
            print(f'Player 1 Card {card1_number} matches with Player 2 Card {card2_number} by color')
            return True
        return False
