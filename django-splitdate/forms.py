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
        self.ordering = unicode(kwargs.pop('field_ordering', Settings.SPLITDATE_ORDER)).lower()
        placeholder = []
        format = []
        if len(self.ordering) != 3 or 'd' not in self.ordering or 'm' not in self.ordering or 'y' not in self.ordering:
            raise ValueError(ugettext('Your SPLITDATE_ORDER setting or \'field_ordering\' attribute is '
                                      'invalid. It needs to be a string that is excactly 3 characters long and contains'
                                      ' the characters \'d\', \'m\' and \'y\' excactly once.'))
        for elm in self.ordering:
            if elm == 'd':
                placeholder.append(placeholder_d)
                format.append('%d')
            elif elm == 'm':
                placeholder.append(placeholder_m)
                format.append('%m')
            elif elm == 'y':
                placeholder.append(placeholder_y)
                format.append('%Y')
        self.date_format = '.'.join(format)
        widgets = (forms.TextInput(attrs={'placeholder': placeholder[0]}),
                   forms.TextInput(attrs={'placeholder': placeholder[1]}),
                   forms.TextInput(attrs={'placeholder': placeholder[2]}),
        )
        super(SplitDateWidget, self).__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            ret = []
            for order in self.ordering:
                if order == 'd':
                    ret.append(value.day)
                elif order == 'm':
                    ret.append(value.month)
                elif order == 'y':
                    ret.append(value.year)
            return ret
        return [None, None]

    def value_from_datadict(self, data, files, name):
        vals = super(SplitDateWidget, self).value_from_datadict(data, files, name)
        if all(vals):
            return datetime.datetime.strptime(".".join(vals), self.date_format).date()
        return None
