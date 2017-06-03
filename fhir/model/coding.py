# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension


from ._uri import uri
from ._string import string
from ._boolean import boolean
from ._code import code


__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Coding']


# ------------------------------------------------------------------------------
# Coding
# ------------------------------------------------------------------------------
class Coding(Element):
    """
    A reference to a code defined by a terminology system.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Coding'
    
    system = Property(PropertyDefinition('system', uri, '0', '1'))
    version = Property(PropertyDefinition('version', string, '0', '1'))
    code = Property(PropertyDefinition('code', code, '0', '1'))
    display = Property(PropertyDefinition('display', string, '0', '1'))
    userSelected = Property(PropertyDefinition('userSelected', boolean, '0', '1'))
    