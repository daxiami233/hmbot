from .automator import Automator
from loguru import logger
from hmdriver2.driver import Driver
from hmdriver2.proto import KeyCode
from ..vht import VHTParser
from ..proto import SwipeDirection

class H2(Automator):
    def __init__(self, device):
        self.serial = device.serial
        self._driver = Driver(self.serial)
        logger.debug("hm_driver2 is connected to device:%s" %(self.serial))
    
    def click(self, x, y):
        return self._driver.click(x, y)

    def drag(self, x1, y1, x2, y2, speed=2000):
        return self._driver.swipe(x1, y1, x2, y2, speed)

    def swipe(self, direction, scale):
        if direction == SwipeDirection.RIGHT :
            self._driver.swipe(0.5, 0.5, 0.5-scale, 0.5, 500)
        elif direction == SwipeDirection.LEFT :
            self._driver.swipe(0.5, 0.5, 0.5+scale, 0.5, 500)

    def dump_hierarchy(self):
        return VHTParser.parse(self._driver.dump_hierarchy())

    def screenshot(self, path=''):
        return self._driver.screenshot(path)
    
    def display_size(self):
        return self._driver.display_size

    def display_rotation(self):
        return self._driver.display_rotation
    
    def home(self):
        self._driver.go_home()

    def back(self):
        self._driver.go_back()

    def recent(self):
        self._driver.swipe(0.5, 2710/2720, 0.5, 2400/2720, 500)