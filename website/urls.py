from django.conf.urls import url

from . import views

app_name = 'website'

urlpatterns = [
	#/music/
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^team/$', views.TeamView.as_view(), name='team'),
    url(r'^gallery/$', views.GalleryView.as_view(), name='gallery'),
    url(r'^sopnsors/$', views.SponsView.as_view(), name='sponsors'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),

]