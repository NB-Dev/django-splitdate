# -*- coding: utf-8 -*-
import logging
from datetime import datetime, time, date
from django.forms import MultiWidget
from django import forms
from django.utils import formats
from django.utils.dateparse import parse_date
from django.utils.encoding import force_str
from django.utils.formats import get_format
from django.utils.translation import ugettext
from app_settings import Settings
from django_splitdate import _strptime

__author__ = 'Tim Schneider <tim.schneider@northbridge-development.de>'
__copyright__ = "Copyright 2015, Northbridge Development Konrad & Schneider GbR"
__credits__ = ["Tim Schneider", ]
__maintainer__ = "Tim Schneider"
__email__ = "mail@northbridge-development.de"
__status__ = "Release"

logger = logging.getLogger(__name__)

class _LazyPlaceholder(object):
        def __init__(self, pos, ordering, placeholder):
            self.pos = pos
            self.ordering = ordering
            self.placeholder = placeholder
        def __unicode__(self):
            ordering = unicode(self.ordering).lower()
            if len(ordering) != 3 or 'd' not in ordering or 'm' not in ordering or 'y' not in ordering:
                raise ValueError(ugettext('Your SPLITDATE_ORDER setting or \'field_ordering\' attribute is '
                                          'invalid. It needs to be a string that is excactly 3 characters long and contains'
                                          ' the characters \'d\', \'m\' and \'y\' excactly once. Current value: %s') % ordering)
            return unicode(self.placeholder[ordering[self.pos]])

class SplitDateWidget(MultiWidget):

    """
    A Widget that splits date input into three <input type="text"> boxes.
    """
    input_formats = formats.get_format_lazy('DATE_INPUT_FORMATS')

    def __init__(self, *args, **kwargs):
        placeholder_d = kwargs.pop('placeholder_day', Settings.SPLITDATE_PLACEHOLDER_DAY)
        placeholder_m = kwargs.pop('placeholder_month', Settings.SPLITDATE_PLACEHOLDER_MONTH)
        placeholder_y = kwargs.pop('placeholder_year', Settings.SPLITDATE_PLACEHOLDER_YEAR)
        self.ordering = kwargs.pop('field_ordering', Settings.SPLITDATE_ORDER)

        placeholder = {
            'd': placeholder_d,
            'm': placeholder_m,
            'y': placeholder_y,
        }
        widgets = (forms.TextInput(attrs={'placeholder': _LazyPlaceholder(0, self.ordering, placeholder)}),
                   forms.TextInput(attrs={'placeholder': _LazyPlaceholder(1, self.ordering, placeholder)}),
                   forms.TextInput(attrs={'placeholder': _LazyPlaceholder(2, self.ordering, placeholder)}),
        )
        super(SplitDateWidget, self).__init__(widgets, *args, **kwargs)

    def get_ordering(self):
        ordering = unicode(self.ordering).lower()
        if len(ordering) != 3 or 'd' not in ordering or 'm' not in ordering or 'y' not in ordering:
            raise ValueError(ugettext('Your SPLITDATE_ORDER setting or \'field_ordering\' attribute is '
                                      'invalid. It needs to be a string that is excactly 3 characters long and contains'
                                      ' the characters \'d\', \'m\' and \'y\' excactly once. Current value: %s') % ordering)
        return ordering

    def decompress(self, value):
        values = [None, None, None]
        if value:
            date = None
            for format in self.input_formats:
                try:
                    date = _strptime(force_str(value), format)
                except (ValueError, TypeError):
                    continue
            if date:
                ordering = self.get_ordering()
                for i in xrange(len(ordering)):
                    if ordering[i] == 'd':
                        values[i] = date[2]
                    elif ordering[i] == 'm':
                        values[i] = date[1]
                    elif ordering[i] == 'y':
                        values[i] = date[0]
        return values

    def value_from_datadict(self, data, files, name):
        vals = super(SplitDateWidget, self).value_from_datadict(data, files, name)
        if all(vals):
            time_format = get_format('SHORT_DATE_FORMAT')
            ordering = self.get_ordering()
            for i in xrange(len(vals)):
                if ordering[i] == 'd':
                    time_format = time_format.replace('d', unicode(vals[i]))
                elif ordering[i] == 'm':
                    time_format = time_format.replace('m', unicode(vals[i]))
                elif ordering[i] == 'y':
                    time_format = time_format.replace('Y', unicode(vals[i]))
                    time_format = time_format.replace('y', unicode(vals[i])[:2])
            return time_format
        return None


