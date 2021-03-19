from django.urls import path, include

from gestionTurnos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('login/', views.login, name="Login"),
    path('registro/', views.registro, name="Registro"),
    path('turnos/', views.turnos, name="Turnos"),
    path('nosotros/', views.nosotros, name="Nosotros"),
     path('aviso/', views.aviso, name="Aviso"),
    path('misturnos/', views.misturnos, name="Usuario"),
    path('eliminar/<id>', views.eliminar, name="Eliminar"),
    path('canchas/', views.canchas, name="Canchas"),  
]