# -*- coding: utf-8 -*-
import logging
from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, UnknownHostException, ConnectionErrorException
import pssh.utils


logger = logging.getLogger(__name__)
stream = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(filename)s:%(lineno)d - %(message)s')

logger.setLevel(logging.DEBUG)
logger.addHandler(stream)
stream.setFormatter(formatter)


# BASE CLASSES #
class BaseSourceArchiver(object):
    def __call__(self, *args, **kwargs):
        print '*'*10

class BasePreArchiver(object):
    def __call__(self, *args, **kwargs):
        print '#'*10

class BaseArchiver(object):
    pass

class BaseTransporter(object):
    '''The more important class, this is like the core of the fabric clone:
    it allows to open a tunnel  from the (usually) local computer to a certain
    numbers of remote endpoints.

    This class should implement the functions needed to act upon the remote system,
    as filesystem-like commands (cd, mkdir, rm)

        >>> transporter = Transporter(hosts=hosts)
        >>> with transporter.cd('/var/www/'):
        >>>    transporter.mkdir(web_root_dir)
    '''
    def __init__(self, hosts=None):
        if not hosts:
            raise Exception('hosts parameter must be defined')

        self.hosts = hosts

        self.client = ParallelSSHClient(hosts)

        logger.info(self._exec_command('uname -a'))

    def cd(self, path):
        # handle absolute or relative paths
        # make clear where the action is done
        # TODO: context manager
        pass

    def mkdir(self, path):
        pass

    def rm(self, path):
        pass

    def cp(self, src, dst):
        # src can be local
        # dst must be remote
        pass

    def _exec_command(self, cmd):
        try:
            return self.client.run_command(cmd)
        except (AuthenticationException, UnknownHostException, ConnectionErrorException) as e:
            logger.exception(e)


class BaseRemotePreExtractor(object):
    pass

class BaseRemoteExtractor(object):
    pass

class BaseRemotePostExtractor(object):
    pass

