from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="Index"),
    url(r'^create-new/$', views.create, name="create"),
    url(r'(?P<blog_id>[0-9]+)/favorite/$', views.data, name="data")
]
