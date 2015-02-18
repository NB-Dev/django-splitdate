# -*- coding: utf-8 -*-
from datetime import date
import logging
from django.test import TestCase, override_settings
from ..forms import SplitDateWidget
from ..app_settings import Settings
__author__ = 'Tim Schneider <tim.schneider@northbridge-development.de>'
__copyright__ = "Copyright 2015, Northbridge Development Konrad & Schneider GbR"
__credits__ = ["Tim Schneider", ]
__maintainer__ = "Tim Schneider"
__email__ = "mail@northbridge-development.de"
__status__ = "Development"

logger = logging.getLogger(__name__)

class SplitDateWidgetTestCase(TestCase):

    def setUp(self):
        Settings._SPLITDATE_ORDER = None
        Settings._SPLITDATE_PLACEHOLDER_DAY = None
        Settings._SPLITDATE_PLACEHOLDER_MONTH = None
        Settings._SPLITDATE_PLACEHOLDER_YEAR = None
    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='dmy',
    )
    def test___init___global_config(self):
        widget = SplitDateWidget()
        self.assertEqual(widget.date_format, '%d.%m.%Y')
        self.assertEqual(len(widget.widgets), 3)
        self.assertEqual(widget.widgets[0].attrs['placeholder'], 'DAY')
        self.assertEqual(widget.widgets[1].attrs['placeholder'], 'MONTH')
        self.assertEqual(widget.widgets[2].attrs['placeholder'], 'YEAR')

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='dmy',
    )
    def test___init___local_config(self):
        widget = SplitDateWidget(
            field_ordering='ymd',
            placeholder_day='day',
            placeholder_month='month',
            placeholder_year='year',
        )
        self.assertEqual(widget.date_format, '%Y.%m.%d')
        self.assertEqual(len(widget.widgets), 3)
        self.assertEqual(widget.widgets[0].attrs['placeholder'], 'year')
        self.assertEqual(widget.widgets[1].attrs['placeholder'], 'month')
        self.assertEqual(widget.widgets[2].attrs['placeholder'], 'day')

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='DMY',
    )
    def test___init___to_order_lowercase(self):
        widget = SplitDateWidget()
        self.assertEqual(widget.date_format, '%d.%m.%Y')

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='dmyy',
    )
    def test___init___ordererror_length(self):
        self.assertRaises(ValueError, SplitDateWidget)

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='mmy',
    )
    def test___init___ordererror_day_missing(self):
        self.assertRaises(ValueError, SplitDateWidget)

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='ddy',
    )
    def test___init___ordererror_month_missing(self):
        self.assertRaises(ValueError, SplitDateWidget)

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='dmm',
    )
    def test___init___ordererror_year_missing(self):
        self.assertRaises(ValueError, SplitDateWidget)

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='dmy',
    )
    def test_decompress(self):
        widget = SplitDateWidget()

        ret = widget.decompress(None)
        self.assertListEqual(ret, [None, None])

        ret = widget.decompress(date(2000, 02, 01))
        self.assertListEqual(ret, [01, 02, 2000])

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='mdy',
    )
    def test_decompress_second_ordering(self):
        widget = SplitDateWidget()

        ret = widget.decompress(date(2000, 02, 01))
        self.assertListEqual(ret, [02, 01, 2000])

    @override_settings(
        SPLITDATE_PLACEHOLDER_DAY='DAY',
        SPLITDATE_PLACEHOLDER_MONTH='MONTH',
        SPLITDATE_PLACEHOLDER_YEAR='YEAR',
        SPLITDATE_ORDER='dmy',
    )
    def test_value_from_datadict_ok_value(self):
        widget = SplitDateWidget()

        ret = widget.value_from_datadict({'test_0': '01', 'test_1': '02', 'test_2': '2000'}, None, 'test')
        self.assertEqual(ret, date(2000, 02, 01))

    def test_value_from_datadict_missing_value(self):
        widget = SplitDateWidget()

        ret = widget.value_from_datadict({'test_0': '01', 'test_2': '2000'}, None, 'test')
        self.assertIsNone(ret)
