from collective.easyslider import easyslider_message_factory as _
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.component import getUtility 
from zope.schema.interfaces import IVocabularyFactory 
from Acquisition import aq_inner
from zope.app.component.hooks import getSite

def FoldersubskinsVocabulary(self): 
    context = getSite()
    extraskins = context.portal_skins.subskins_composites  

    terms = extraskins
    
    return SimpleVocabulary(terms) 
    