# -*- coding: utf-8 -*-
import logging


logger = logging.getLogger(__name__)

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
    pass

class BaseRemotePreExtractor(object):
    pass

class BaseRemoteExtractor(object):
    pass

class BaseRemotePostExtractor(object):
    pass

# IMPLEMENTATIONS #
class GitSourceArchiver(BaseSourceArchiver):
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
    pre_archiver    = BasePreArchiver()
    archiver        = TarArchiver()
    transporter     = SSHTransporter()
    pre_extractor   = RemotePreExtractor()
    extractor       = RemoteTarExtractor()
    post_extractor  = RemotePostExtractor()

    def run(self, *args, **kwargs):
        self.archiver()
