from .connector import Connector

class HDC(Connector):
    def __init__(self, device):
        self.device = device