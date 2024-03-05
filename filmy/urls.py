from django.urls import path
from filmy.views import wszystkie, szczegoly, nowy, edycja, usun
from django.contrib import admin

urlpatterns = [
    path('wszystkie/', wszystkie),
    path('szczegoly/<int:film_id>/', szczegoly),
    path('nowy/', nowy),
    path('edycja/<int:film_id>/', edycja),
    path('usun/<int:film_id>/', usun),
    path('admin/', admin.site.urls)
]
