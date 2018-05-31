from django.contrib import admin
from django.conf.urls import url, include
from .views import signup,profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', signup, name='signup'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^', include('django.contrib.auth.urls')),
]