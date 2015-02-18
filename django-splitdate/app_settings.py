# -*- coding: utf-8 -*-

from . import SPLITDATE_ORDER_DMY
from django.utils.translation import ugettext_lazy

__author__ = 'Tim Schneider <tim.schneider@northbridge-development.de>'
__copyright__ = "Copyright 2015, Northbridge Development Konrad & Schneider GbR"
__credits__ = ["Tim Schneider", ]
__maintainer__ = "Tim Schneider"
__email__ = "mail@northbridge-development.de"
__status__ = "Release"



class classproperty(object):
    def __init__(self, getter):
        self.getter= getter
    def __get__(self, instance, owner):
        return self.getter(owner)


class Settings(object):
    _SPLITDATE_ORDER = None
    _SPLITDATE_FORMAT = None
    _SPLITDATE_PLACEHOLDER_DAY = None
    _SPLITDATE_PLACEHOLDER_MONTH = None
    _SPLITDATE_PLACEHOLDER_YEAR = None

    @classproperty
    def SPLITDATE_ORDER(cls):           # property
        if cls._SPLITDATE_ORDER is None:
            from django.conf import settings
            cls._SPLITDATE_ORDER = getattr(settings, 'SPLITDATE_ORDER', SPLITDATE_ORDER_DMY)
        return cls._SPLITDATE_ORDER

    @classproperty
    def SPLITDATE_FORMAT(cls):           # property
        if cls._SPLITDATE_FORMAT is None:
            order = cls.SPLITDATE_ORDER
            cls._SPLITDATE_FORMAT = '.'.join(['%%%s' % elm for elm in order])
        return cls._SPLITDATE_FORMAT
    
    @classproperty
    def SPLITDATE_PLACEHOLDER_DAY(cls):           # property
        if cls._SPLITDATE_PLACEHOLDER_DAY is None:
            from django.conf import settings
            cls._SPLITDATE_PLACEHOLDER_DAY = getattr(settings, 'SPLITDATE_PLACEHOLDER_DAY', ugettext_lazy('DD'))
        return cls._SPLITDATE_PLACEHOLDER_DAY
    
    @classproperty
    def SPLITDATE_PLACEHOLDER_MONTH(cls):           # property
        if cls._SPLITDATE_PLACEHOLDER_MONTH is None:
            from django.conf import settings
            cls._SPLITDATE_PLACEHOLDER_MONTH = getattr(settings, 'SPLITDATE_PLACEHOLDER_MONTH', ugettext_lazy('MM'))
        return cls._SPLITDATE_PLACEHOLDER_MONTH

    @classproperty
    def SPLITDATE_PLACEHOLDER_YEAR(cls):           # property
        if cls._SPLITDATE_PLACEHOLDER_YEAR is None:
            from django.conf import settings
            cls._SPLITDATE_PLACEHOLDER_YEAR = getattr(settings, 'SPLITDATE_PLACEHOLDER_YEAR', ugettext_lazy('YYYY'))
        return cls._SPLITDATE_PLACEHOLDER_YEAR

