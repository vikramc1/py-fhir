# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension, Reference


from ._code import code
from ._xhtml import xhtml


__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Narrative']


# ------------------------------------------------------------------------------
# Narrative
# ------------------------------------------------------------------------------
class Narrative(Element):
    """
    A human-readable formatted text, including images.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Narrative'
    
    status = Property(PropertyDefinition('status', code, '1', '1'))
    div = Property(PropertyDefinition('div', xhtml, '1', '1', 'text'))
