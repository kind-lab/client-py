
from . import element
from . import valid
import logging

logger = logging.getLogger(__name__)

class ExtensionOmbCategory(element.Element):
    """ Race text US core """
    resource_type = "ExtensionOmbCategory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.url = None
        """ OMB cateogry"""
        
        self.valueCoding = None
        """ Value of omb category """
        
        super(ExtensionOmbCategory, self).__init__(jsondict=jsondict, strict=strict)
        
        
    def elementProperties(self):
        js = super(ExtensionOmbCategory, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("valueCoding", "valueCoding", coding.Coding, False, None, True),
        ])
        return js

class ExtensionDetailed(element.Element):
    """ Race text US core """
    resource_type = "ExtensionDetailed"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.url = None
        """ OMB cateogry"""
        
        self.valueCoding = None
        """ Value of omb category """
        
        super(ExtensionDetailed, self).__init__(jsondict=jsondict, strict=strict)
        
        
    def elementProperties(self):
        js = super(ExtensionDetailed, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("valueCoding", "valueCoding", coding.Coding, False, None, True),
        ])
        return js
    
class ExtensionText(element.Element):
    """ Race text US core """
    resource_type = "ExtensionText"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.url = None
        """ OMB cateogry"""
        
        self.valueString = None
        """ Value of omb category """
        
        super(ExtensionText, self).__init__(jsondict=jsondict, strict=strict)
        
        
    def elementProperties(self):
        js = super(ExtensionText, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("valueString", "valueString", str, False, None, True),
        ])
        return js

class USCoreRace(element.Element):
    """ Race as defined by US Core """
    resource_type = "USCoreRace"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.url = None
        """ Race url for us-core-race """
        
        self.ombCategory = None
        """ OMB Category for race"""
        
        self.detailed = None
        """ Detailed description of race """
        
        self.text = None
        """ Text description of race """
        
        super(USCoreRace, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(USCoreRace, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("ombCategory", "ombCategory", ExtensionOmbCategory, True, None, False),
            ("detailed", "detailed", ExtensionDetailed, True, None, False),
            ("text", "text", ExtensionText, False, None, True),
        ])
        return js
    

class USCoreEthnicity(element.Element):
    """ Ethnicity as defined by US Core """
    resource_type = "USCoreEthnicity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        self.url = None
        """ Ethnicity url for us-core-ethnicity """
        
        self.ombCategory = None
        """ OMB Category for ethnicity"""
        
        self.detailed = None
        """ Detailed description of race """
        
        self.text = None
        """ Text description of race """
        
        super(USCoreEthnicity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(USCoreEthnicity, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("ombCategory", "ombCategory", ExtensionOmbCategory, False, None, False),
            ("detailed", "detailed", ExtensionDetailed, True, None, False),
            ("text", "text", ExtensionText, False, None, True),
        ])
        return js
    
    
class USCoreBirthSex(element.Element):
    """ Brithsex as defined by US Core """
    resource_type = "USCoreBirthSex"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        
        self.url = None
        """ Birthsex url for us-core-birthsex """
        
        self.valueCode = None
        """ Birthsex F or M"""    
        
        super(USCoreBirthSex, self).__init__(jsondict=jsondict, strict=strict)
      
    def __setattr__(self, name, value): 
        if hasattr(self,name):  
            if name == 'valueCode': self.validationCheck(name, value, valid.BIRTHSEX)          
        object.__setattr__(self, name, value)
        
    def validationCheck(self, name, value, value_list):
        if (not len(value_list)==0) & (value not in value_list):
            logger.error(f'ERROR: {name} not of proper type {value_list}, instead given: {value}')
            # raise ValueError(f'Birthsex not one of F or M, instead given: {value}')

    def elementProperties(self):
        js = super(USCoreBirthSex, self).elementProperties()
        
        js.extend([
            ("url", "url", str, False, None, True),
            ("valueCode", "valueCode", str, False, None, True)
        ])
        return js

import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']