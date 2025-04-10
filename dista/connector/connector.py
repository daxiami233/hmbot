from abc import ABC, abstractmethod

class Connector(ABC):
    """
    this interface describes a connector (ADB or HDC)
    """
    @abstractmethod
    def __init__(self, device):
        pass

    @abstractmethod
    def run_cmd(self, extra_args):
        """
        Run a command and return the output

        Args:
            extra_args (str): arguments to run in adb or hdc

        Returns:
            str: output of command
        """
        pass

    @abstractmethod
    def shell(self, extra_args):
        """
        Run a shell-command and return the output

        Args:
            extra_args (str): arguments to run in adb or hdc

        Returns:
            str: output of command
        """
        pass

    # @abstractmethod
    # def get_current_ability(self):
    #     pass

    # @abstractmethod
    # def get_resource(self):
    #     pass