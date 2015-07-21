from django.conf.urls import include, url

from api.views import hello

urlpatterns = [
    url(r'hello/', hello),
    url(r'movie/', api_movie_list_view, name="api_movie_list_view")

]
