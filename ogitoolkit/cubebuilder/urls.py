from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'^(?P<filename>(robots.txt)|(humans.txt))$', name='home-files'),
# ]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/(?P<api_name>[a-zA-Z0-9-]+)$', views.call_api, name='call_api'),
]

