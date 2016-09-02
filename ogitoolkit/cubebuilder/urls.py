from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'^(?P<filename>(robots.txt)|(humans.txt))$', name='home-files'),
# ]

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

