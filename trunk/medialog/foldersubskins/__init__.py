# from Products.CMFPlone.CatalogTool import registerIndexableAttribute

from Products.ATContentTypes.interface import IATFolder
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
