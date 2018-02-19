
class BaseController:

    def __init__(self, character):
        self.character = character

    def play(self, state):
        raise NotImplementedError

    def get_object(self):
        return self.character
