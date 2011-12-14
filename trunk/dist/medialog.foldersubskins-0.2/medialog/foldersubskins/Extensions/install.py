from medialog.foldersubskins.schemaextender import ContentTypeExtender

def install(portal):
	"""Register the extender so it only takes effekt on this site"""
	sm = portal.getSiteManager()
	sm.registerAdapter(ContentTypeExtender, name='medialog.foldersubskins.ContentTypeExtender')
	
	return "Register the schemaextender at the root of the Plone site"
	
def uninstall(portal):
	"""Unregister the schemaextender so it no longer takes effekt on this site"""
	sm=portal.getSiteManager()
	sm.unregisterAdapter(ContentTypeExtender, name='medialog.foldersubskins.ContentTypeExtender')
	
	return "Removed the schemaextender from the root of the Plone site"
