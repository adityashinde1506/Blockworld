import logging
from blockworld.simple.controllers import BaseController
from blockworld.simple.game_objects import World


class WorldController(BaseController):

    """
        Handles world events.
    """

    def __init__(self):
        self.character = World()
        BaseController.__init__(self, self.character)

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def register_object(self, _object):
        self.logger.debug(f"Adding {_object} to world.")
        self.character.register_object(_object)

    def get_state(self):
        values = {}

        for _object in self.character.contents:
            values[_object.pos] = _object.val

        state = [[0.0 for i in range(self.character.width)] for j in range(self.character.height)]

        for pos in values.keys():

            r, c = pos
            state[r][c] = values[pos]

        return state

    def get_display(self):
        sprites = {}

        for _object in self.character.contents:
            sprites[_object.pos] = _object.sprite

        state = [[" . " for i in range(self.character.width)] for j in range(self.character.height)]

        for pos in sprites.keys():

            r, c = pos
            state[r][c] = f" {sprites[pos]} "

        return state

    def play(self, state):

        while 1:
            redo = self.character.handle_collisions()

            if not redo:
                break
        print(self.character.contents)
        for _obj in self.character.contents:
            if _obj.ttl < 0:
                _obj.kill()
                self.character.delete(_obj)
