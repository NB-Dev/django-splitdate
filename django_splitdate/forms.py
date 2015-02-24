# -*- coding: utf-8 -*-
import logging
from datetime import date
from django.forms import MultiWidget, DateField
from django import forms
from django.utils import six
from django.utils.functional import lazy
from django.utils.translation import ugettext, get_language
from app_settings import Settings

__author__ = 'Tim Schneider <tim.schneider@northbridge-development.de>'
__copyright__ = "Copyright 2015, Northbridge Development Konrad & Schneider GbR"
__credits__ = ["Tim Schneider", ]
__maintainer__ = "Tim Schneider"
__email__ = "mail@northbridge-development.de"
__status__ = "Release"

logger = logging.getLogger(__name__)

def _get_ordering(ordering):
    if isinstance(ordering, dict):
        ordering = _get_ordering_string_by_language(ordering)
    ordering = unicode(ordering).lower()
    if len(ordering) != 3 or 'd' not in ordering or 'm' not in ordering or 'y' not in ordering:
        raise ValueError(ugettext('Your SPLITDATE_ORDER setting or \'field_ordering\' attribute is '
                                  'invalid. It needs to be a string that is excactly 3 characters long and contains'
                                  ' the characters \'d\', \'m\' and \'y\' excactly once. Current value: %s') % ordering)
    return ordering

def _get_ordering_string_by_language(ordering):
    lang = get_language()
    # first see if exact language is available in ordering
    if lang in ordering:
        return ordering[lang]

    fallback = None
    # Then see if a the language starts with another defined language
    for key, value in ordering.iteritems():
        if lang.startswith(key):
            return value
        if not fallback:
            fallback = value

    # use the first value or 'dmy' as fallback
    return fallback or 'dmy'

def get_placeholder(pos, ordering, placeholder):
    ordering = _get_ordering(ordering)
    return unicode(placeholder[ordering[pos]])

get_placeholder_lazy = lazy(get_placeholder, six.text_type)

class SplitDateWidget(MultiWidget):

    """
    A Widget that splits date input into three <input type="text"> boxes.
    """

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
        widgets = (forms.TextInput(attrs={'placeholder': get_placeholder_lazy(0, self.ordering, placeholder)}),
                   forms.TextInput(attrs={'placeholder': get_placeholder_lazy(1, self.ordering, placeholder)}),
                   forms.TextInput(attrs={'placeholder': get_placeholder_lazy(2, self.ordering, placeholder)}),
        )
        super(SplitDateWidget, self).__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if isinstance(value, date):
            value = value.strftime('%d.%m.%Y')
        values = [None, None, None]
        if value:
            parts = value.split('.')
            if len(parts) != 3:
                raise ValueError(ugettext('The Value needs to be in the format DD.MM.YYYY.'))
            ordering = _get_ordering(self.ordering)
            for i in xrange(len(parts)):
                if ordering[i] == 'd':
                    values[i] = parts[0]
                elif ordering[i] == 'm':
                    values[i] = parts[1]
                elif ordering[i] == 'y':
                    values[i] = parts[2]
        return values

    def value_from_datadict(self, data, files, name):
        vals = super(SplitDateWidget, self).value_from_datadict(data, files, name)
        if all(vals):
            values = [None, None, None]
            ordering = _get_ordering(self.ordering)
            for i in xrange(len(vals)):
                if ordering[i] == 'd':
                    values[0] = vals[i]
                elif ordering[i] == 'm':
                    values[1] = vals[i]
                elif ordering[i] == 'y':
                    values[2] = vals[i]
            return '.'.join(values)
        return None

class SplitDateField(DateField):
    widget = SplitDateWidget
    input_formats = ['%d.%m.%Y',]
