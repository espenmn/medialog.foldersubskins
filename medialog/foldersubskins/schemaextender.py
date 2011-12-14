from zope.interface import implements
from zope.component import adapts
from zope.i18nmessageid import MessageFactory

from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender, IOrderableSchemaExtender   
from archetypes.schemaextender.field import ExtensionField

from Products.Archetypes.atapi import *
from Products.ATContentTypes.interface import IATFolder 

from Products.SmartColorWidget.Widget import SmartColorWidget

from interfaces import IFolderSubskinsLayer

# Any field you tack on must have ExtensionField as its first subclass:
class _StringExtensionField (ExtensionField, StringField): 
    pass

class _LinesExtensionField (ExtensionField, LinesField):
    pass



class ContentTypeExtender(object):
    """Adapter that adds custom css settings."""
    adapts(IATFolder)
    implements(ISchemaExtender, IBrowserLayerAwareExtender, IOrderableSchemaExtender)
    layer = IFolderSubskinsLayer
    _fields = [
        _LinesExtensionField('extracss',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = LinesWidget(
            label=u"Extra css",
            description=u"Names of css file(s) that will work for everything in this folder.",            
            )
        ),
        
        _StringExtensionField(
        'SubSkinsColor1', 
        required=False,
        schemata = "settings",
        searchable=False,
        widget = SmartColorWidget(
            label=u"Definition of SubSkinsColor1",
            description=u"The name of colour 1.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor2',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = SmartColorWidget(
            label=u"Definition of SubSkinsColor2",
            description=u"Write the name of colour 2.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor3',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = SmartColorWidget(
            label=u"Definition of SubSkinsColor3",
            description=u"Write the name of colour 3.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor4',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = SmartColorWidget(
            label=u"Definition of SubSkinsColor4",
            description=u"Write the name of colour 4.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor5',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = SmartColorWidget(
            label=u"Definition of SubSkinsColor5",
            description=u"Write the name of colour 5.",            
            )
        ),
        
        _StringExtensionField('SubSkinsColor6',
        required=False,
        schemata = "settings",
        searchable=False,
        widget = SmartColorWidget(
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
    	
    def getOrder(self, schematas):
        """ Manipulate the order in which fields appear.
        @param schematas: Dictonary of schemata name -> field lists

        @return: Dictionary of reordered field lists per schemata.
                """
        schematas["foldersubskins"] = ['extracss', 'SubSkinsColor1', 'SubSkinsColor2', 'SubSkinsColor3', 'SubSkinsColor4', 'SubSkinsColor5', 'SubSkinsColor6', 'SubSkinsWidth1', 'SubSkinsWidth2', 'SubSkinsWidth3']

        return schematas

    def getFields(self):
        return self._fields

#    def __init__(self, contentType):
#        pass    
