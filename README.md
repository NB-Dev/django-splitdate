[![PyPI version](https://badge.fury.io/py/django-splitdate.png)](http://badge.fury.io/py/django-splitdate) [![Build Status](https://travis-ci.org/NB-Dev/django-splitdate.svg?branch=master)](https://travis-ci.org/NB-Dev/django-splitdate) [![Coverage Status](https://coveralls.io/repos/NB-Dev/django-splitdate/badge.svg?branch=master)](https://coveralls.io/r/NB-Dev/django-splitdate?branch=master) [![Downloads](https://pypip.in/download/django-splitdate/badge.svg)](https://pypi.python.org/pypi/django-splitdate/) [![Supported Python versions](https://pypip.in/py_versions/django-splitdate/badge.svg)](https://pypi.python.org/pypi/django-splitdate/) [![License](https://pypip.in/license/django-splitdate/badge.svg)](https://pypi.python.org/pypi/django-splitdate/)
=====
django-splitdate
=====

This app provides a form widget that uses three text inputs to enter the day, month and year of a date for a standard
DateField. The field is based on Django's forms.SplitDateTimeWidget.

Quick start
-----------

1. Install django-splitdate:
    * From the pip repository: ```pip install django_splitdate```
    * or directly from github: ```pip install git+git://github.com/NB-Dev/django-splitdate.git``

2. (optional) Customize the Settings (see below)

3. Define the widget for your form's date field:

    ```
    from django_splitdate.forms import SplitDateWidget
    date = forms.DateField(widget=SplitDateWidget())
    ```

Global Configuration
--------------------

The SplitDateWidget can be configured globally in your settings.py file with the following options

#### SPLITDATE_ORDER (String):
Defines the ordering of the day, month and year fields.

A three character string, that contains the characters 'd'(day), 'm'(month), 'y'(year) in the desired order.

Default: _('mdy')

Using the translation to provide different default values for different languages:
* English: 'mdy'
* German: 'dmy'

#### SPLITDATE_PLACEHOLDER_DAY (String):
A string defining the placeholder of the day field.

Default: _('DD')

#### SPLITDATE_PLACEHOLDER_MONTH (String):
A string defining the placeholder of the month field.

Default: _('MM')

#### SPLITDATE_PLACEHOLDER_YEAR (String):
A string defining the placeholder of the year field.

Default: _('YYYY')

Per-Instance Configuration
--------------------------
The global configuration can be overwritten on a per-instance basis using instantiation attributes:

#### field_ordering (String):
Local overwrite for SPLITDATE_ORDER. Possible values, see above.

#### placeholder_day (String):
Local overwrite for SPLITDATE_PLACEHOLDER_DAY. Possible values, see above.

#### placeholder_month (String):
Local overwrite for SPLITDATE_PLACEHOLDER_MONTH. Possible values, see above.

#### placeholder_year (String):
Local overwrite for SPLITDATE_PLACEHOLDER_YEAR. Possible values, see above.

Running the tests
----
The included tests can be run standalone by running the ```tests/runtests.py``` script. The only requirement for this is
Django >= 1.7. If you also want to run coverage, you need to install it before running the tests
