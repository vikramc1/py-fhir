# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference

from .backboneelement import BackboneElement
from .backboneelement import BackboneElement

from ._boolean import boolean
from ._integer import integer
from ._string import string

from .codeableconcept import CodeableConcept
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .timing import Timing

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Dosage']

class DoseAndRate(Element):
    """Autogenerated class for implicit type."""
    type = Property('type', 'CodeableConcept', '0', '1')
    dose = Property('dose', ['Range', 'Quantity'], '0', '1')
    rate = Property('rate', ['Ratio', 'Range', 'Quantity'], '0', '1')


# ------------------------------------------------------------------------------
# Dosage
# ------------------------------------------------------------------------------
class Dosage(BackboneElement):
    """
    Indicates how the medication is/was taken or should be taken by the
    patient.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Dosage'
    
    sequence = Property('sequence', integer, '0', '1')
    text = Property('text', string, '0', '1')
    additionalInstruction = Property('additionalInstruction', CodeableConcept, '0', '*')
    patientInstruction = Property('patientInstruction', string, '0', '1')
    timing = Property('timing', Timing, '0', '1')
    asNeeded = Property('asNeeded', ['boolean', 'CodeableConcept'], '0', '1')
    site = Property('site', CodeableConcept, '0', '1')
    route = Property('route', CodeableConcept, '0', '1')
    method = Property('method', CodeableConcept, '0', '1')
    doseAndRate = Property('doseAndRate', DoseAndRate, '0', '*')
    maxDosePerPeriod = Property('maxDosePerPeriod', Ratio, '0', '1')
    maxDosePerAdministration = Property('maxDosePerAdministration', Quantity, '0', '1')
    maxDosePerLifetime = Property('maxDosePerLifetime', Quantity, '0', '1')