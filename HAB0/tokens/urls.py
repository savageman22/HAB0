from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home/*', views.token_view),
    url(r'show_token/*', views.token_variable_view),
]
