from zope.interface import implements
from zope.component import adapts
from zope.i18nmessageid import MessageFactory

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.atapi import *
from Products.ATContentTypes.interface import IATFolder
#from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
#from zope.component import getUtility 


# Any field you tack on must have ExtensionField as its first subclass:
class _StringExtensionField (ExtensionField, StringField): 
    pass

class _LinesExtensionField (ExtensionField, LinesField):
    pass



class ContentTypeExtender(object):
    """Adapter that adds custom css settings."""
    adapts(IATFolder)

    implements(ISchemaExtender)
    _fields = [
        _LinesExtensionField('extracss',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = LinesWidget(
            label=u"Extra css",
            description=u"The name of a css file that will work for everything in this folder.",            
            )
        ),
        
        _StringExtensionField(
        'SubSkinsColor1', 
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsColor1",
            description=u"The name of colour 1.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor2',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsColor2",
            description=u"Write the name of colour 2.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor3',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsColor3",
            description=u"Write the name of colour 3.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor4',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsColor4",
            description=u"Write the name of colour 4.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor5',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsColor5",
            description=u"Write the name of colour 5.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor6',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsColor6",
            description=u"Write the name of colour 6.",            
            )
        ),
        
        _StringExtensionField('SubSkinsWidth1',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsWidth1",
            description=u"Write the width of the layout.",            
            )
        ),
        
        _StringExtensionField('SubSkinsWidth2',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsWidth2",
            description=u"Write the width of the left column.",            
            )
        ),
        
        _StringExtensionField('SubSkinsWidth3',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = StringWidget(
            label=u"Definition of SubSkinsWidth3",
            description=u"Write the width of the right column.",            
            )
        ),
        
    ]
    
    
    def __init__(self, context):
    	self.context = context

    def getFields(self):
        return self._fields

#    def __init__(self, contentType):
#        pass    