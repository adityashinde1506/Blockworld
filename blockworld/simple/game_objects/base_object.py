
class UnderfinedActionError(Exception):
    pass


def id_generator():
    i = 0
    while 1:
        yield i
        i += 1


id_gen = id_generator()


class BaseObject:

    """
        Base class for all world objects.
    """

    def __init__(self, pos, sprite="?", val=0.01):
        self._id = next(id_gen)
        self._pos = pos
        self._health = 100.0
        self._strength = 1.0
        self._last_pos = None
        self._ttl = 100
        self._sprite = sprite
        self._val = val

    @property
    def health(self):
        return self._health

    @property
    def strength(self):
        return self._strength

    @property
    def pos(self):
        return self._pos

    @property
    def ttl(self):
        return self._ttl

    @property
    def obj_id(self):
        return self._id

    @property
    def sprite(self):
        return self._sprite

    @property
    def val(self):
        return self._val

    def _tick(self):
        self._ttl -= 1

    def undo_pos(self):
        temp_pos = self._pos
        self._pos = self._last_pos
        self._last_pos = temp_pos

    def _do(self, action):
        self._tick()
        self._last_pos = self._pos

        if action == "NOP":
            pass

        elif action == "MOVE_N":
            r, c = self.pos
            self._pos = (r - 1, c)

        elif action == "MOVE_S":
            r, c = self.pos
            self._pos = (r + 1, c)

        elif action == "MOVE_E":
            r, c = self.pos
            self._pos = (r, c - 1)

        elif action == "MOVE_W":
            r, c = self.pos
            self._pos = (r, c + 1)

        else:
            raise UnderfinedActionError

    def kill(self):
        raise NotImplementedError
