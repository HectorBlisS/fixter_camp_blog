from django.conf.urls import url
from django.contrib import admin
from main import views
from posts import views as views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home.as_view()),
    url(r'^blog/$',views2.Blog.as_view()),
]
