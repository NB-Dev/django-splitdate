v0.1.8 (2015-02-24)
----
* Refactoring to reduce code replication
* Bugfix

v0.1.7 (2015-02-24)
---
* Cannot work with standard DateField as the SHORT_DATE_FORMAT might not contain a 4 digit year field, resulting in
	strange date results. Going back to a SplitDateField
* Not using translation for different languages anymore. Instead using a dictionary for the mapping.

v0.1.6 (2015-02-23)
---
* Version to allow reuploading of version 0.1.5 with better readme

v0.1.5 (2015-02-23)
---
* Including the default SHORT_DATE_FORMAT to be able to use the widget on a standard DateField

v0.1.4 (2015-02-19)
----
* Renaming app to django_splitdate as the minus is not allowed

v0.1.3 (2015-02-19)
----
* Adding coverage to runtest.py if it is available
* Updating README.md

v0.1.2 (2015-02-18)
----
* Adding tests and runtest.py

v0.1.1 (2015-02-18)
----
* Removing .po files from package

v0.1 (2015-02-18)
----
* initial release