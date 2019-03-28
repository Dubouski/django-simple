from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^articles$', CreateView.as_view(), name="create"),
    url(r'^articles/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
