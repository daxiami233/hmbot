import sys
from typing import Union
from loguru import logger
from .connector.adb import ADB
from .connector.hdc import HDC
from .automator.u2 import U2
from .automator.h2 import H2
from .exception import*
from .proto import OperatingSystem, SwipeDirection

system_mapping = {
    OperatingSystem.ANDROID: (ADB, U2),
    OperatingSystem.HARMONY: (HDC, H2)
}

class Device(object):
    """
    The class describes a connected device
    """

    def __init__(self, device_serial, operating_system):
        """
        Initialize a device connection
        Args:
            device_serial (str): The serial of device.
            operating_system (str): The operating system of device.
        """
        self.serial = device_serial
        self.operating_system = operating_system
        try:
            connector_cls, automator_cls = system_mapping[self.operating_system]
            self.connector = connector_cls(self)
            self.automator = automator_cls(self)
        except OSKeyError:
            logger.error("%s is not supported" % operating_system)
            sys.exit(-1)
    
    def click(self, x, y):
        return self.automator.click(x, y)

    def click(self, node):
        (x, y) = node.attrib['center']
        return self.automator.click(x, y)

    def long_click(self, x, y):
        return self.automator.long_click(x, y)

    def long_click(self, node):
        (x, y) = node.attrib['center']
        return self.automator.long_click(x, y)

    def drag(self, x1, y1, x2, y2, speed=2000):
        return self.automator.drag(x1, y1, x2, y2, speed)

    def swipe(self, direction: Union[SwipeDirection, str], scale: float = 0.3):
        return self.automator.swipe(direction, scale)

    def dump_hierarchy(self):
        return self.automator.dump_hierarchy()

    def screenshot(self, path=''):
        return self.automator.screenshot(path)

    def display_size(self):
        return self.automator.display_size()

    def display_rotation(self):
        return self.automator.display_rotation()
    
    def home(self):
        self.automator.home()

    def back(self):
        self.automator.back()

    def recent(self):
        self.automator.recent()