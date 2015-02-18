=====
django-splitdate
=====

This app provides a form widget that uses three text inputs to enter the day, month and year of a date for a standard
DateField

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

Configuration
-------------

#### SPLITDATE_ORDER:
Defines the ordering of the day, month and year fields.

One of the predefined values:
- django-splitdate.SPLITDATE_ORDER_DMY (Default)

    Day/Month/Year
- django-splitdate.SPLITDATE_ORDER_DYM

    Day/Year/Month
- django-splitdate.SPLITDATE_ORDER_MDY

    Month/Day/Year
- django-splitdate.SPLITDATE_ORDER_MYD

    Month/Year/Day
- django-splitdate.SPLITDATE_ORDER_YDM

    Year/Day/Month
- django-splitdate.SPLITDATE_ORDER_YMD

    Year/Month/Day

#### SPLITDATE_PLACEHOLDER_DAY
A string defining the placeholder of the day field.

Default: _('DD')

#### SPLITDATE_PLACEHOLDER_MONTH
A string defining the placeholder of the month field.

Default: _('MM')

#### SPLITDATE_PLACEHOLDER_YEAR
A string defining the placeholder of the year field.

Default: _('YYYY')