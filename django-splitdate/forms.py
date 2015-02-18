# -*- coding: utf-8 -*-
import logging
import datetime
from django.forms import MultiWidget
from django import forms
from django.utils.translation import ugettext
from app_settings import Settings

__author__ = 'Tim Schneider <tim.schneider@northbridge-development.de>'
__copyright__ = "Copyright 2015, Northbridge Development Konrad & Schneider GbR"
__credits__ = ["Tim Schneider", ]
__maintainer__ = "Tim Schneider"
__email__ = "mail@northbridge-development.de"
__status__ = "Release"

logger = logging.getLogger(__name__)

class SplitDateWidget(MultiWidget):
    """
    A Widget that splits date input into three <input type="text"> boxes.
    """
    supports_microseconds = False

    def __init__(self, *args, **kwargs):
        placeholder_d = kwargs.pop('placeholder_day', Settings.SPLITDATE_PLACEHOLDER_DAY)
        placeholder_m = kwargs.pop('placeholder_month', Settings.SPLITDATE_PLACEHOLDER_MONTH)
        placeholder_y = kwargs.pop('placeholder_year', Settings.SPLITDATE_PLACEHOLDER_YEAR)
        placeholder = []
        for elm in Settings.SPLITDATE_ORDER:
            if elm == 'd':
                placeholder.append(placeholder_d)
            elif elm == 'm':
                placeholder.append(placeholder_m)
            elif elm == 'Y':
                placeholder.append(placeholder_y)
        if len(placeholder) != 3:
            raise ValueError(ugettext('Your SPLITDATE_ORDER setting seems to be invalid. Please user one of the predefined settings defined in django-splitdate.'))
        widgets = (forms.TextInput(attrs={'placeholder': placeholder[0]}),
                   forms.TextInput(attrs={'placeholder': placeholder[1]}),
                   forms.TextInput(attrs={'placeholder': placeholder[2]}),
                   )
        super(SplitDateWidget, self).__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        vals = super(SplitDateWidget, self).value_from_datadict(data, files, name)
        if all(vals):
            return datetime.datetime.strptime(".".join(vals), Settings.SPLITDATE_ORDER).date()
        return None
