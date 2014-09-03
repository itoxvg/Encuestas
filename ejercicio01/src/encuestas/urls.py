from django.conf.urls import patterns, url
from encuestas import views

urlpatterns = patterns('',
	#Encuesta localhost:8000/encuestas/
	url(r'^$', views.index, name='index'),
	#Encuesta localhost:8000/encuestas/5/
	url(r'^detalles/(?P<id_encuesta>\d+)/$', views.detalles, name='detalles'),
	#Encuesta localhost:8000/encuestas/5/resultados
	url(r'^(?P<id_encuesta>\d+)/votos/$', views.votos, name='votos'),
    #Encuesta localhost:8000/encuestas/5/
	url(r'^(?P<id_encuesta>\d+)/resultados/$', views.resultados, name='resultados'),
)



