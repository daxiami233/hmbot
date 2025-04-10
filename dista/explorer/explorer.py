from abc import ABC, abstractmethod
from ..proto import ExploreMission
from ..ptg import PTG

class Explorer(ABC):
    """
    this interface describes a explorer
    """
    def __init__(self, device=None, app=None):
        self.device = device
        self.app = app

    @abstractmethod
    def explore(self, ptg=PTG(), **termination):
        """
        Explore the app.
        """
        pass
