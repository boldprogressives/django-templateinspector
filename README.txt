Usage::

>>> from djtemplateinspector import get_variables
>>> from django.template import Template
>>> tmpl = Template("Welcome, {{ user }}!")
>>> get_variables(tmpl)
["user"]
