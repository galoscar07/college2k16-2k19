from django.conf.urls import url

from my_auth import views

app_name = 'my_auth'


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout')
]