from django.conf.urls import patterns, url
from encuestas import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detalles'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='resultados'),
    url(r'^(?P<id_encuesta>\d+)/votos/$', views.votos, name='votos'),
)


