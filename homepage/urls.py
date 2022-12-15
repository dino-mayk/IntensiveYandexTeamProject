from django.urls import path

from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('<filter>', views.home, name='home'),
]
