from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from login_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("system/", include("server.urls")),
    url(r'^login_system/', include('login_system.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/', views.special, name='speical'),
    url(r'^$', views.index, name='index'),
]
