# -*- coding: utf-8 -*-
import logging

__author__ = 'Tim Schneider <tim.schneider@northbridge-development.de>'
__copyright__ = "Copyright 2015, Northbridge Development Konrad & Schneider GbR"
__credits__ = ["Tim Schneider", ]
__maintainer__ = "Tim Schneider"
__email__ = "mail@northbridge-development.de"
__status__ = "Development"

logger = logging.getLogger(__name__)

SPLITDATE_ORDER_DMY = ('d','m','Y')
SPLITDATE_ORDER_DYM = ('d','Y','m')
SPLITDATE_ORDER_MDY = ('m','d','Y')
SPLITDATE_ORDER_MYD = ('m','Y','d')
SPLITDATE_ORDER_YDM = ('Y','d','m')
SPLITDATE_ORDER_YMD = ('Y','m','d')