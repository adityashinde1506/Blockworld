import logging


class UndefinedCollisionError(Exception):
    pass


class CollisionHandler:

    """
        Implements physics/ collison response.
    """

    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.debug("Collision Handler initialised.")

    def handle_collision(self, object1, object2):
        """
            Handles collisions between object1 and object2 according to programmed rules.
        """

        if object1.__class__.__name__ == "Man" and object2.__class__.__name__ == "Man":
            object1.undo_pos()
            object2.undo_pos()

        else:
            raise UndefinedCollisionError
