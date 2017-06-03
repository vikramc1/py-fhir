# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension



from .quantity import Quantity

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Range']


# ------------------------------------------------------------------------------
# Range
# ------------------------------------------------------------------------------
class Range(Element):
    """
    A set of ordered Quantities defined by a low and high limit.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Range'
    
    low = Property(PropertyDefinition('low', Quantity, '0', '1'))
    high = Property(PropertyDefinition('high', Quantity, '0', '1'))
    