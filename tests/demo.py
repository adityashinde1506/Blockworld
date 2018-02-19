import sys
import logging
import time
import os

sys.path.append("/home/adityas/Projects/BlockWorld")
logging.basicConfig(level=logging.DEBUG)

from blockworld.simple.game import Game
from blockworld.simple.controllers import ManRandomController

game = Game()
game.add_controller(ManRandomController(pos=(2, 2), val=0.2))
game.add_controller(ManRandomController(pos=(8, 8), val=0.2))
game.add_controller(ManRandomController(pos=(5, 5), val=0.2))
game.init_game()

while 1:

    time.sleep(0.5)
    os.system("clear")
    game.loop(view=1)
