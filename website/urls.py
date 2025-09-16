from django.urls import path
from .views import home,about, contact,room, dining, roomsingle
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('room', room, name='room'),
    path('dining', dining, name='dining'),
    path('roomsingle/<str:pk>/', roomsingle, name='roomsingle'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)