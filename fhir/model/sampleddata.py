# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension


from ._string import string
from ._positiveint import positiveInt
from ._decimal import decimal

from .quantity import Quantity

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['SampledData']


# ------------------------------------------------------------------------------
# SampledData
# ------------------------------------------------------------------------------
class SampledData(Element):
    """
    A series of measurements taken by a device, with upper and lower
    limits. There may be more than one dimension in the data.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/SampledData'
    
    origin = Property(PropertyDefinition('origin', Quantity, '1', '1'))
    period = Property(PropertyDefinition('period', decimal, '1', '1'))
    factor = Property(PropertyDefinition('factor', decimal, '0', '1'))
    lowerLimit = Property(PropertyDefinition('lowerLimit', decimal, '0', '1'))
    upperLimit = Property(PropertyDefinition('upperLimit', decimal, '0', '1'))
    dimensions = Property(PropertyDefinition('dimensions', positiveInt, '1', '1'))
    data = Property(PropertyDefinition('data', string, '1', '1'))
    