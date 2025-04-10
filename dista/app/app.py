from abc import ABC, abstractmethod
class App(ABC):
    """
    this interface describes a App (Android or Harmony)
    """
    @abstractmethod
    def __init__(self, app_path='', package_name='', entry=''):
        self.app_path = app_path
        self.package_name = package_name
        self.entry = entry
