from django.conf.urls import url
from django.contrib import admin
from main import views
from posts import views as views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home.as_view()),
    url(r'^blog/$',views2.ListView.as_view()),
    url(r'^detalle/(?P<id>\d+)/$',
    	views2.DetailView.as_view(),
    	name="detalle"),
]
