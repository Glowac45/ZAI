from django.contrib.auth.models import User
from .models import Film, ExtraInfo, Ocena, Aktor
from .serializers import FilmModelSerializer, ExtraInfoSerializer, OcenaSerializer, AktorSerializer, UserSerializerShort
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class FilmCreateList(generics.ListCreateAPIView):
    # queryset = Film.objects.all().order_by('-rok','tytul')
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Film.objects.all().order_by('-rok','tytul')
        tytul = self.request.query_params.get('tytul')
        id = self.request.query_params.get('id')
        if tytul is not None:
            queryset = queryset.filter(tytul__startswith=tytul)
        if id is not None:
            queryset = queryset.filter(id__exact=id)
        return queryset

class FilmRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ExtraInfoCreateList(generics.ListCreateAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ExtraInfoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class OcenaCreateList(generics.ListCreateAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OcenaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class AktorCreateList(generics.ListCreateAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AktorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer


class UserCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort