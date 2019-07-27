from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('donate', views.donate, name='donate'),
    path('support',views.support, name ='support'),
    path('rehabilitation', views.rehabil, name='rehabil'),
    path('news', views.news, name='news')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)