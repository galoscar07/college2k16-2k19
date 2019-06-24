from django.conf.urls import url
from photoeditor import views

app_name = 'photoeditor'


urlpatterns = [
    url(r'^editor/upload-photo/', views.upload_photo, name='upload'),
    url(r'^editor/your-photo/', views.your_photo, name='yourphoto'),
    url(r'home/', views.index, name='index')
]