from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('core.urls')),
    url('admin/', admin.site.urls),
]
