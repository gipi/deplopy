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


# https://parallel-ssh.readthedocs.org/en/latest/pssh_client.html
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
        self._initial_connection()

    def _parse_output(self, output):
        '''This parse for our usage the output of the execution'''

    def _log_channel_output(self, output, prefix=None):
        for host in output:
            for stdout in output[host]['stdout']:
                logger.info('%s%s' % (prefix, stdout))
            for stderr in output[host]['stderr']:
                logger.warn('%s%s' % (prefix, stderr))

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

    def _initial_connection(self):
        '''The ratio of this method is that we need to connect immediately to the remote endpoints
        in order to be sure that hosts are accessible.

        AuthenticationException, UnknownHostException and ConnectionErrorException are possible only
        at the first attempt (TODO: check, I'm not sure for ConnectionErrorException, if the server
        lost connection?).
        '''
        try:
            self._log_channel_output(self.client.run_command('uname -a'), prefix=' --- start connection: ')
        except (AuthenticationException, UnknownHostException, ConnectionErrorException) as e:
            logger.exception(e)
            raise e

    def _exec_command(self, cmd):
        return self.client.run_command(cmd)

    def run(self, cmd):
        return self._exec_command(cmd)


class BaseRemotePreExtractor(object):
    pass

class BaseRemoteExtractor(object):
    pass

class BaseRemotePostExtractor(object):
    pass

