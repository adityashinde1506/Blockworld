import logging


class InvalidObjectError(Error):
    pass


class World:

    """
        Defines the 2d grid world.
    """

    def __init__(self, height=10, width=10):
        self.height = height
        self.width = width

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        self.contents = {}
        self.logger.info("Empty world initialised.")

    def __handle_collisions(self):
        """
            Checks for position clashes for every game object. In case of a collision, both objects are restored to their previous positions.
        """

        for _object in self.contents:
            for other in self.contents:

                if other == _object:
                    continue

                elif _object.pos == other.pos:
                    _object.go_to_lastpos()
                    other.go_to_lastpos()

                    self.logger.debug(f"Collision between {_object} and {other } detected.")
