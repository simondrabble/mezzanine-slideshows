from django.conf import settings

from mezzanine_slideshows.models import Slideshow


def get_slideshows(request):
    if request.user and request.user.is_staff:
        slideshows = Slideshow.objects.all()

    else:
        slideshows = Slideshow.objects.published()

    # except:
    #     random_block = Slideshow.objects.none()
    return {'slideshows': slideshows}
