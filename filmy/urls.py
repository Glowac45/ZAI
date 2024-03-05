from django.urls import path
from filmy.views import wszystkie, szczegoly, nowy

urlpatterns = [
    path('wszystkie/', wszystkie),
    path('szczegoly/<int:film_id>/', szczegoly),
    path('nowy/', nowy)
]
