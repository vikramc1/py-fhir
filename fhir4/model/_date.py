# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, DateTimeProperty, BaseType, dateTimeBase

__all__ = ['date', ]

class date(dateTimeBase):
    """Autogenerated date type."""
    _regex = '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?'    
    
    value = DateTimeProperty('value', str, '1', '1', 'xmlAttr')


