from . import models as config

def get_config(request):
    data={
        # 'social' : config.Social.objects.filter(status=True),
        # 'front' : config.Front.objects.filter(status=True),
        # 'site' : config.Site.objects.filter(status=True),
    }
    return data