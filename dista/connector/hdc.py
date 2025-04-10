from .connector import Connector
from ..exception import DeviceError, HDCError
from loguru import logger
import subprocess, re

class HDC(Connector):
    def __init__(self, device = None):
        from ..device import Device
        if isinstance(device, Device):
            self.serial = device.serial
        else:
            raise DeviceError
        self.cmd_prefix = ['hdc', "-t", device.serial]
    
    def run_cmd(self, extra_args):
        if isinstance(extra_args, str):
            extra_args = extra_args.split()
        if not isinstance(extra_args, list):
            msg = "invalid arguments: %s\nshould be str, %s given" % (extra_args, type(extra_args))
            logger.warning(msg)
            raise HDCError(msg)

        args = [] + self.cmd_prefix
        args += extra_args

        logger.debug('command:')
        logger.debug(args)
        r = subprocess.check_output(args).strip()
        if not isinstance(r, str):
            r = r.decode()
        logger.debug('return:')
        logger.debug(r)
        return r

    def shell(self, extra_args):
        if isinstance(extra_args, str):
            extra_args = extra_args.split()
        if not isinstance(extra_args, list):
            msg = "invalid arguments: %s\nshould be str, %s given" % (extra_args, type(extra_args))
            logger.warning(msg)
            raise HDCError(msg)
        extra_args = ['shell'] + extra_args
        return self.run_cmd(extra_args)
    
    def _hidumper(self, ability, extra_args):
        if isinstance(extra_args, str):
            extra_args = [extra_args]
        else:
            msg = "invalid arguments: %s\nshould be str, %s given" % (extra_args, type(extra_args))
            logger.warning(msg)
            raise HDCError(msg)
        extra_args = ['hidumper', '-s', ability, '-a'] + extra_args
        return self.shell(extra_args)

    def get_current_ability(self):
        missions = self._hidumper(ability='AbilityManagerService', extra_args='-l')
        current_mission_re = re.compile('.*current mission lists:{(.*?)}.*', flags=re.DOTALL)
        infos_re = re.compile('.*app name \[(.*)\].*main name \[(.*)\].*bundle name \[(.*)\].*ability type.*', flags=re.DOTALL)
        match = current_mission_re.match(missions)
        if match:
            return infos_re.match(match.group(1)).groups()