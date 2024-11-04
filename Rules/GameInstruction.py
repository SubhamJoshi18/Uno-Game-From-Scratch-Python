import copy
import random

class GameMethods:
    def handle_game_deck(self, player1_card, player2_card, randomized_cards):
        # Validate the format of initial cards for debugging
        print("Initial Player 1 Deck:", player1_card)
        print("Initial Player 2 Deck:", player2_card)
        print("Randomized Cards Deck:", randomized_cards)

        player_1 = copy.deepcopy(player1_card)
        player_2 = copy.deepcopy(player2_card)

        # Ensure decks are formatted correctly before proceeding
        for i, card in enumerate(player_1):
            if not (isinstance(card, (list, tuple)) and len(card) == 2):
                print(f"Error in Player 1's deck at position {i}: {card}")
                return
        for i, card in enumerate(player_2):
            if not (isinstance(card, (list, tuple)) and len(card) == 2):
                print(f"Error in Player 2's deck at position {i}: {card}")
                return

        while player_1 and player_2:
            card1 = player_1[0]
            card2 = player_2[0]

            card1_number, card1_color = card1
            card2_number, card2_color = card2

            if self.check_card_condition(card1_number, card1_color, card2_number, card2_color):
                print(f"Match! {card1} (Player 1) matches {card2} (Player 2)")
                player_1.pop(0)
                player_2.pop(0)
            else:
                print(f"No Match: {card1} (Player 1) vs {card2} (Player 2)")

                if randomized_cards:
                    new_card1 = randomized_cards.pop(0)
                    new_card2 = randomized_cards.pop(0)
                    print(f"Player 1 draws {new_card1}, Player 2 draws {new_card2}")
                    player_1.pop(0)
                    player_2.pop(0)
                    player_1.append(new_card1)
                    player_2.append(new_card2)
                else:
                    print("Draw deck is empty, game ends in a draw.")
                    return

        if not player_1:
            print("Player 1 has no cards left! Player 2 wins!")
        elif not player_2:
            print("Player 2 has no cards left! Player 1 wins!")

    @staticmethod
    def check_card_condition(card1_number, card1_color, card2_number, card2_color):
        return card1_color == card2_color or card1_number == card2_number

def random_90_card(num_range):
    colors = ['Red', 'Blue', 'Green', 'Yellow']
    cards = [[random.randint(0, 14), random.choice(colors)] for _ in range(num_range)]
    print("Generated Cards:", cards)  # Debug: check generated cards format
    return cards
