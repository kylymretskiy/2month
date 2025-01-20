from decouple import config
from logic import  game

cash = int(config('FISHKI'))
first_number = int(config('FIRST_NUMBER'))
last_number = int(config('LAST_NUMBER'))
attempts = int(config('POPYTKI'))

game(cash,first_number,last_number,attempts)

