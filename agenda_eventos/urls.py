from django.conf.urls import url

from agenda_eventos import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
