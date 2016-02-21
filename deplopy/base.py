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

