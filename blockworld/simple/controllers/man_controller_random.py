import logging
from blockworld.simple.controllers import BaseController
from blockworld.simple.game_objects import Man
import random


class ManRandomController(BaseController):

    """
        Does random actions.
    """

    def __init__(self, pos, sprite="U", val=0.5):
        self.character = Man(pos=pos, sprite=sprite, val=val)
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        self.actions = {1: "NOP",
                        2: "MOVE_N",
                        3: "MOVE_S",
                        4: "MOVE_E",
                        5: "MOVE_W"}

    def play(self, state):
        action = random.randint(1, 5)
        self.character.do(self.actions[action])
