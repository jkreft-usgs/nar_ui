from django.conf import settings

def default(request):

    # you can declare any variable that you would like and pass 
    # them as a dictionary to be added to each template's context like so:
    exposedSettingNames = ['DEBUG', 
                           'GEOSERVER_HOST_NAME', 
                           'GEOSERVER_PATH', 
                           'SOS_HOST_NAME', 
                           'SOS_PATH', 
                           'NAR_WEBSERVICE', 
                           'NAR_WEBSERVICE_PATH',
                           'NAR_CURRENT_WATER_YEAR',
                           'NAR_SOS_DEFS_BASE_URL']
    exposedSettings = {}
    for exposedSettingName in exposedSettingNames:
        if hasattr(settings, exposedSettingName):
            exposedSettings[exposedSettingName] = getattr(settings, exposedSettingName)
            
    return dict(
        settings = exposedSettings
    )
