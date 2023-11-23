
from django.contrib import admin
from django.urls import path, include
from contact import views
from webchamps import views as my_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscibe/', views.subscibe, name='subscibe'),
    path("", include("myauth.urls")),
    # path('subscibe/', views.subscibe, name='subscibe'),
    path('about/', my_views.about, name='about'),
    path('portfolio/', my_views.portfolio, name='portfolio'),
    path('services/', my_views.services, name='services'),
    path('contact/', my_views.contact, name='contact'),
]
