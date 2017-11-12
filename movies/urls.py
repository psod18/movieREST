from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MoviesView.as_view(), name='movies-view'),
    url(r'^(\d+)/$', views.MovieView.as_view(), name='movie_view'),
    url(r'^person/(\d+)/$', views.PersonView.as_view(), name='person_view'),
]