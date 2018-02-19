import logging
import pprint
from blockworld.simple.controllers import WorldController


class Display:

    def __init__(self):
        pass

    def pprint(self, game):

        for row in game:
            for element in row:
                print(element, end="")
            print()


class Game:

    """
        Runs game loops.
    """

    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        self.world_controller = WorldController()
        self.controllers = []
        #self.display = pprint.PrettyPrinter(indent=1)
        self.display = Display()
        self.state = None

    def init_game(self):
        for controller in self.controllers:
            _object = controller.get_object()
            self.world_controller.register_object(_object)
        self.state = self.world_controller.get_state()

    def add_controller(self, controller):
        self.controllers.append(controller)

    def loop(self, view=0):
        for controller in self.controllers:
            controller.play(self.state)

        self.world_controller.play(self.state)
        self.state = self.world_controller.get_state()

        if view:
            self.display.pprint(self.world_controller.get_display())
