from abc import ABC, abstractmethod
from ..proto import ExploreMission
from ..ptg import PTG
from ..device import Device
from ..app.app import App
from ..event import Event

class Explorer(ABC):
    """
    this interface describes a explorer
    """
    def __init__(self, device=None, app=None):
        if isinstance(device, Device):
            self.device = device
        if isinstance(app, App):
            self.app = app

    def explore(self, **termination):
        page = self.device.dump_page(self.app)
        ptg = PTG(page)
        while (not self.should_terminate(termination)):
            if page is None:
                self.move_on()
            node = self.best(page.all('clickable'), page.img)
            self.device.click(node)
            new_page = self.device.dump_page(self.app)
            ptg.add_edge(page, new_page, Event(node))
            page = new_page
    
    def move_on(self):
        pass
    
    
    # def back_to(self, ptg, pre_page):
    #     pass

    @abstractmethod
    def best(self, nodes, img):
        pass

    def should_terminate(self, **termination):
        return True

