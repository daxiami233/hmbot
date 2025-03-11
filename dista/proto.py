from enum import Enum

class OperatingSystem(str, Enum):
    HARMONY = 'harmony'
    ANDROID = 'android'

class SwipeDirection(str, Enum):
    LEFT = 'left'
    RIGHT = "right"
    UP = "up"
    DOWN = "down"