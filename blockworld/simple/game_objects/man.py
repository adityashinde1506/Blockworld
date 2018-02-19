import logging
from blockworld.simple.game_objects import BaseObject


class Man(BaseObject):

    def __init__(self, pos, sprite="U", val=0.5):

        assert len(sprite) == 1, "Sprite should be single character."

        BaseObject.__init__(self, pos, sprite, val=val)
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.debug(f"Initialised Man.{self.obj_id}")

    def do(self, action):
        self.logger.debug(f"Man.{self.obj_id} does {action}: POS {self.pos} TTL {self.ttl}")
        self._do(action)

    def kill(self):
        self.logger.debug(f"{self.__class__.__name__}.{self.obj_id} dies.")
