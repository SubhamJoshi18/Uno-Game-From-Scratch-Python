import random
from Helper.helper import Uno
from Libs.logger import uno_logger


if __name__ == "__main__":
    try:
        player_input = int(input('Enter the Player you want to play UNO: '))
        uno_instance = Uno(no_of_player=player_input)
    except Exception as error:
        uno_logger.error(f'Error in starting the game : {error}')



