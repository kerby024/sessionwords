from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addword$', views.add),
    url(r'^results$', views.result)]