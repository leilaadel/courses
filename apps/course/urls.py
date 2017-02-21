from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^course$', views.course),
    url(r'^destroy/[0-9]$', views.destroy)
    # url(r'^destroy/(?P<id>\d+)$', views.destroy)
    # url(r'^$', views.id)
]
