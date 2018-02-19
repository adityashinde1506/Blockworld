import logging
from blockworld.simple.handlers import CollisionHandler


class InvalidObjectError(Exception):
    pass


class World:

    """
        Defines the 2d grid world.
    """

    def __init__(self, height=10, width=10):
        self.height = height
        self.width = width

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        self._contents = []
        self.collision_handler = CollisionHandler()
        self.logger.info("Empty world initialised.")

    def handle_collisions(self):
        """
            Checks for position clashes for every game object. In case of a collision, both objects are restored to their previous positions.
        """
        detection_flag = 0

        for _object in self.contents:

            r, c = _object.pos

            if (r < 0 or r >= self.height) or (c < 0 or c >= self.width):
                self.logger.debug(f"{_object.__class__.__name__}.{_object.obj_id} went out of bounds!")
                _object.undo_pos()

                detection_flag = 1

            for other in self.contents:

                if other == _object:
                    continue

                elif _object.pos == other.pos:
                    self.logger.debug(f"Collision between {_object.obj_id} and {other.obj_id} detected.")

                    self.collision_handler.handle_collision(_object, other)
                    detection_flag = 1

        return detection_flag

    @property
    def contents(self):
        return self._contents

    def register_object(self, _object):
        self._contents.append(_object)

    def delete(self, _object):
        self._contents.remove(_object)
        print(self.contents)
