# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference


from ._datetime import dateTime


__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Period']


# ------------------------------------------------------------------------------
# Period
# ------------------------------------------------------------------------------
class Period(Element):
    """
    A time period defined by a start and end date and optionally time.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Period'
    
    start = Property('start', dateTime, '0', '1')
    end = Property('end', dateTime, '0', '1')
