# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension, Reference

from .backboneelement import BackboneElement
from .resource import Resource

from ._unsignedint import unsignedInt
from ._code import code
from ._decimal import decimal
from ._string import string
from ._uri import uri
from ._instant import instant

from .signature import Signature
from .identifier import Identifier
from .backboneelement import BackboneElement

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Bundle']

class Link(BackboneElement):
    """Autogenerated class for implicit type."""
    relation = Property(PropertyDefinition('relation', 'string', '1', '1'))    
    url = Property(PropertyDefinition('url', 'uri', '1', '1'))    

class Entry(BackboneElement):
    """Autogenerated class for implicit type."""
    link = Property(PropertyDefinition('link', 'Link', '0', '*'))    
    fullUrl = Property(PropertyDefinition('fullUrl', 'uri', '0', '1'))    
    resource = Property(PropertyDefinition('resource', 'Resource', '0', '1'))    
    search = Property(PropertyDefinition('search', 'Search', '0', '1'))    
    request = Property(PropertyDefinition('request', 'Request', '0', '1'))    
    response = Property(PropertyDefinition('response', 'Response', '0', '1'))    

class Search(BackboneElement):
    """Autogenerated class for implicit type."""
    mode = Property(PropertyDefinition('mode', 'code', '0', '1'))    
    score = Property(PropertyDefinition('score', 'decimal', '0', '1'))    

class Request(BackboneElement):
    """Autogenerated class for implicit type."""
    method = Property(PropertyDefinition('method', 'code', '1', '1'))    
    url = Property(PropertyDefinition('url', 'uri', '1', '1'))    
    ifNoneMatch = Property(PropertyDefinition('ifNoneMatch', 'string', '0', '1'))    
    ifModifiedSince = Property(PropertyDefinition('ifModifiedSince', 'instant', '0', '1'))    
    ifMatch = Property(PropertyDefinition('ifMatch', 'string', '0', '1'))    
    ifNoneExist = Property(PropertyDefinition('ifNoneExist', 'string', '0', '1'))    

class Response(BackboneElement):
    """Autogenerated class for implicit type."""
    status = Property(PropertyDefinition('status', 'string', '1', '1'))    
    location = Property(PropertyDefinition('location', 'uri', '0', '1'))    
    etag = Property(PropertyDefinition('etag', 'string', '0', '1'))    
    lastModified = Property(PropertyDefinition('lastModified', 'instant', '0', '1'))    
    outcome = Property(PropertyDefinition('outcome', 'Resource', '0', '1'))    


# ------------------------------------------------------------------------------
# Bundle
# ------------------------------------------------------------------------------
class Bundle(Resource):
    """
    A container for a collection of resources.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Bundle'
    
    identifier = Property(PropertyDefinition('identifier', Identifier, '0', '1'))
    type = Property(PropertyDefinition('type', code, '1', '1'))
    total = Property(PropertyDefinition('total', unsignedInt, '0', '1'))
    link = Property(PropertyDefinition('link', Link, '0', '*'))
    entry = Property(PropertyDefinition('entry', Entry, '0', '*'))
    signature = Property(PropertyDefinition('signature', Signature, '0', '1'))