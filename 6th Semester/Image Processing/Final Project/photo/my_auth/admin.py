from django.contrib import admin

# Register your models here.
from my_auth.models import UserProfileInfo

admin.site.register(UserProfileInfo)