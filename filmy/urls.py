from .views import FilmList, FilmRetrieve, FilmCreateList, UserList, UserCreateList
from django.urls import path

urlpatterns = [
    path('filmlist/', FilmList.as_view(), name='FilmList'),
    path('filmretrieve/<int:pk>/',FilmRetrieve.as_view(), name='FilmRetrieve'),
    path('filmcreatelist/', FilmCreateList.as_view(), name='FilmCreateList'),
    path('userlist/', UserList.as_view(), name='UserList'),
    path('usercreatelist/', UserCreateList.as_view(), name='UserCreateList')
]

'''
from django.urls import path, include
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
'''