

class GameMethods:


    @staticmethod
    def check_card_condition(card1_number,card1_color,card2_number,card2_color):
        if str(card1_color).__contains__(str(card2_color)) or str(card2_color).lower().startswith(str(card1_color)):
            print(f'Both Color Matches For {card1_number} and {card2_number} ')
            return True