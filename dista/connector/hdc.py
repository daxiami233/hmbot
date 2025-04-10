from .connector import Connector
from ..exception import DeviceError, HDCError
from loguru import logger
import subprocess, re

class HDC(Connector):
    def __init__(self, device = None):
        if device is None and len(HDC.devices()) > 0:
            self.serial = HDC.devices()[0]
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

        logger.debug('command: %s'%args)
        r = subprocess.check_output(args).strip()
        if not isinstance(r, str):
            r = r.decode()
        logger.debug('return: %s'%r)
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

    def shell_grep(self, extra_args, grep_args):
        pass

    def current_ability(self):
        missions = self._hidumper(ability='AbilityManagerService', extra_args='-l')
        missions = missions.split('}')
        infos_re = re.compile('.*app name \[(.*)\].*main name \[(.*)\].*bundle name \[(.*)\].*ability type.*', flags=re.DOTALL)
        for mission in missions:
            if 'state #FOREGROUND  start time' in mission and 'app state #FOREGROUND' in mission:
                match = infos_re.match(mission)
                if match:
                    return {'app': match.groups()[0],
                            'ability': match.groups()[1],
                            'bundle': match.groups()[2]}
    
    def devices(cls):
        args = ['hdc', 'list', 'targets']
        logger.debug('command: %s'%args)
        r = subprocess.check_output(args).strip()
        if not isinstance(r, str):
            r = r.decode()
        logger.debug('return: %s'%r)
        return r.splitlines()
