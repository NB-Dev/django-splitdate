=====
django-splitdate
=====

This app provides a form widget that uses three text inputs to enter the day, month and year of a date for a standard
DateField. The field is based on Django's forms.SplitDateTimeWidget.

Quick start
-----------

1. Add "django-splitdate" to your INSTALLED_APPS setting like this:

    ```
    INSTALLED_APPS = (
        ...
        'django-splitdate',
    )
    ```
2. (optional) Customize the Settings

3. Define the widget for your form's date field:

    ```
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