from .views import FilmCreateList, FilmRetrieveUpdateDestroy,  ExtraInfoCreateList, ExtraInfoRetrieveUpdateDestroy, \
    OcenaCreateList, OcenaRetrieveUpdateDestroy, AktorCreateList, AktorRetrieveUpdateDestroy, \
    UserCreateList, UserRetrieveUpdateDestroy, api_root
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('', api_root),
    path('filmy/', FilmCreateList.as_view(), name='FilmCreateList'),
    path('filmy/<int:pk>/', FilmRetrieveUpdateDestroy.as_view(), name='FilmRetrieveUpdateDestroy'),
    path('extrainfo/', ExtraInfoCreateList.as_view(), name='ExtraInfoCreateList'),
    path('extrainfo/<int:pk>/',ExtraInfoRetrieveUpdateDestroy.as_view(), name='ExtraInfoRetrieveUpdateDestroy'),
    path('ocena/', OcenaCreateList.as_view(), name='OcenaCreateList'),
    path('ocena/<int:pk>/',OcenaRetrieveUpdateDestroy.as_view(), name='OcenaRetrieveUpdateDestroy'),
    path('aktor/', AktorCreateList.as_view(), name='AktorCreateList'),
    path('aktor/<int:pk>/', AktorRetrieveUpdateDestroy.as_view(), name='AktorRetrieveUpdateDestroy'),
    path('user/', UserCreateList.as_view(), name='UserCreateList'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='UserRetrieveUpdateDestroy')
]
