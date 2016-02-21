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

