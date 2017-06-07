# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension, Reference

from .backboneelement import BackboneElement
from .domainresource import DomainResource

from ._boolean import boolean
from ._code import code
from ._date import date
from ._datetime import dateTime
from ._integer import integer

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .humanname import HumanName
from .identifier import Identifier
from .period import Period

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Patient']

class Contact(BackboneElement):
    """Autogenerated class for implicit type."""
    relationship = Property(PropertyDefinition('relationship', 'CodeableConcept', '0', '*'))    
    name = Property(PropertyDefinition('name', 'HumanName', '0', '1'))    
    telecom = Property(PropertyDefinition('telecom', 'ContactPoint', '0', '*'))    
    address = Property(PropertyDefinition('address', 'Address', '0', '1'))    
    gender = Property(PropertyDefinition('gender', 'code', '0', '1'))    
    organization = Property(PropertyDefinition('organization', 'Reference(reference="None")', '0', '1'))    
    period = Property(PropertyDefinition('period', 'Period', '0', '1'))    

class Animal(BackboneElement):
    """Autogenerated class for implicit type."""
    species = Property(PropertyDefinition('species', 'CodeableConcept', '1', '1'))    
    breed = Property(PropertyDefinition('breed', 'CodeableConcept', '0', '1'))    
    genderStatus = Property(PropertyDefinition('genderStatus', 'CodeableConcept', '0', '1'))    

class Communication(BackboneElement):
    """Autogenerated class for implicit type."""
    language = Property(PropertyDefinition('language', 'CodeableConcept', '1', '1'))    
    preferred = Property(PropertyDefinition('preferred', 'boolean', '0', '1'))    

class Link(BackboneElement):
    """Autogenerated class for implicit type."""
    other = Property(PropertyDefinition('other', ['Reference(reference="None")', 'Reference(reference="None")'], '1', '1'))    
    type = Property(PropertyDefinition('type', 'code', '1', '1'))    


# ------------------------------------------------------------------------------
# Patient
# ------------------------------------------------------------------------------
class Patient(DomainResource):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Patient'
    
    identifier = Property(PropertyDefinition('identifier', Identifier, '0', '*'))
    active = Property(PropertyDefinition('active', boolean, '0', '1'))
    name = Property(PropertyDefinition('name', HumanName, '0', '*'))
    telecom = Property(PropertyDefinition('telecom', ContactPoint, '0', '*'))
    gender = Property(PropertyDefinition('gender', code, '0', '1'))
    birthDate = Property(PropertyDefinition('birthDate', date, '0', '1'))
    deceased = Property(PropertyDefinition('deceased', ['boolean', 'dateTime'], '0', '1'))
    address = Property(PropertyDefinition('address', Address, '0', '*'))
    maritalStatus = Property(PropertyDefinition('maritalStatus', CodeableConcept, '0', '1'))
    multipleBirth = Property(PropertyDefinition('multipleBirth', ['boolean', 'integer'], '0', '1'))
    photo = Property(PropertyDefinition('photo', Attachment, '0', '*'))
    contact = Property(PropertyDefinition('contact', Contact, '0', '*'))
    animal = Property(PropertyDefinition('animal', Animal, '0', '1'))
    communication = Property(PropertyDefinition('communication', Communication, '0', '*'))
    generalPractitioner = Property(PropertyDefinition('generalPractitioner', ['Reference(reference="None")', 'Reference(reference="None")'], '0', '*'))
    managingOrganization = Property(PropertyDefinition('managingOrganization', Reference(reference="None"), '0', '1'))
    link = Property(PropertyDefinition('link', Link, '0', '*'))
