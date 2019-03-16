from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from PhotoEditor.album import views


urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
    url(r'^edit/(?P<photo_id>[a-zA-Z0-9-]*)/$', views.photo_edit, name='photo_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
