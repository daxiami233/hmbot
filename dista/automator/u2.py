from .automator import Automator
import uiautomator2

class U2(Automator):
    def __init__(self, device):
        self.device = device

    def click(self, x, y):
        pass

    def drag(self, x1, y1, x2, y2):
        pass