from .connector import Connector

class ADB(Connector):
    def __init__(self, device):
        self.device = device
        self.cmd_prefix = ['adb', "-s", device.serial]