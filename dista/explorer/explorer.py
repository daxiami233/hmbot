from abc import ABC, abstractmethod
from ..proto import ExploreMission
from ..ptg import PTG
from ..device import Device
from ..app.app import App

class Explorer(ABC):
    """
    this interface describes a explorer
    """
    def __init__(self, device=None, app=None):
        if isinstance(device, Device):
            self.device = device
        if isinstance(app, App):
            self.app = app

    def explore(self, ptg=PTG(), **termination):
        while (not self.should_terminate(termination)):
            window = self.device.dump_window()
            page = window.current_page(self.app)
            node = self.best(page.all('clickable'), page.img)
            self.device.click(node)
            if page:
                pass
            else:
                pass

    @abstractmethod
    def best(self, nodes, img):
        pass

    def should_terminate(self, **termination):
        return True

