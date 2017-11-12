from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MoviesView.as_view(), name='show_movies')

]