# -*- coding: utf-8 -*-
import logging

from .base import (
    BaseSourceArchiver,
    BasePreArchiver,
    BaseArchiver,
    BaseTransporter,
    BaseRemotePreExtractor,
    BaseRemoteExtractor,
    BaseRemotePostExtractor,
)


logger = logging.getLogger(__name__)

stream = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(filename)s:%(lineno)d - %(message)s')

logger.setLevel(logging.DEBUG)
logger.addHandler(stream)
stream.setFormatter(formatter)


# IMPLEMENTATIONS #
class GitSourceArchiver(BaseSourceArchiver):
    pass

class PreArchiver(BasePreArchiver):
    pass

class TarArchiver(BaseArchiver):
    pass


class SSHTransporter(BaseTransporter):
    pass

class RemotePreExtractor(BaseRemotePreExtractor):
    pass

class RemoteTarExtractor(BaseRemoteExtractor):
    pass

class RemotePostExtractor(BaseRemotePostExtractor):
    pass

class DeployBase(object):
    source_archiver = GitSourceArchiver()
    pre_archiver    = PreArchiver()
    archiver        = TarArchiver()
    transporter     = SSHTransporter
    pre_extractor   = RemotePreExtractor()
    extractor       = RemoteTarExtractor()
    post_extractor  = RemotePostExtractor()

    def run(self, *args, **kwargs):
        self.archiver()

if __name__ == '__main__':
    import sys
    import pssh.utils

    pssh.utils.enable_host_logger()

    if len(sys.argv) < 3: # at least one command and one hosts
        print 'usage: %s cmd host1 [host2 [ host3 ] ...' % sys.argv[0]
        sys.exit(1)

    cmd = sys.argv[1]
    hosts = sys.argv[2:]

    transporter = SSHTransporter(hosts=hosts)

    output = transporter.run(cmd)

    for host in output:
        for stdout in output[host]['stdout']:
            print stdout
