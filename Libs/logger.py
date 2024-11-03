import logging
import os

uno_logger = logging.getLogger('uno')

stream_handler = logging.StreamHandler()



file_handler = logging.FileHandler(os.path.join(os.getcwd(),'Logs','error.log'))

stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

uno_logger.addHandler(stream_handler)
uno_logger.addHandler(file_handler)

