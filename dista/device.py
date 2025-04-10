import sys
from typing import Union
from loguru import logger
from .app.app import App
from .exception import*
from .proto import SwipeDirection
from .rfl.system_rfl import system_rfl
from .window import Window

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
            connector_cls, automator_cls = system_rfl[self.operating_system]
            self.connector = connector_cls(self)
            self.automator = automator_cls(self)
        except OSKeyError:
            logger.error("%s is not supported" % operating_system)
            sys.exit(-1)

    def install_app(self, app):
        self.automator.install_app(app)

    def uninstall_app(self, app):
        self.automator.uninstall_app(app)

    def start_app(self, app):
        self.automator.start_app(app)

    def stop_app(self, app):
        self.automator.stop_app(app)

    def restart_app(self, app):
        self.automator.restart_app(app)
    
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

    # def display_size(self):
    #     return self.automator.display_size()

    # def display_rotation(self):
    #     return self.automator.display_rotation()
    
    def home(self):
        self.automator.home()

    def back(self):
        self.automator.back()

    def recent(self):
        self.automator.recent()
    
    def dump_window(self):
        vht = self.dump_hierarchy()
        screen = self.screenshot()
        window = Window(vht=vht, screen=screen)
        return window

    def current_ability(self):
        return self.connector.current_ability()