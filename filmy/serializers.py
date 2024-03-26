from rest_framework import serializers
from .models import Film, ExtraInfo, Ocena, Aktor
from django.contrib.auth.models import User


class AktorSerializer(serializers.ModelSerializer):
    filmy = serializers.SlugRelatedField(slug_field='tytul', queryset=Film.objects.all(), many=True)

    class Meta:
        model = Aktor
        fields = ['id', 'imie', 'nazwisko', 'filmy']


class OcenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocena
        fields = ['recenzja', 'gwiazdki', 'film']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        password = validated_data.get('password', None)
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user


class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tytul = serializers.CharField(required=True, allow_blank=False, max_length=64)
    rok = serializers.IntegerField(allow_null=False)
    opis = serializers.CharField(style={'base_template': 'textarea.html'}, default='')
    premiera = serializers.DateField(allow_null=True)
    imdb_points = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        return Film.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.rok = validated_data.get('rok', instance.rok)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.premiera = validated_data.get('premiera', instance.premiera)
        instance.imdb_points = validated_data.get('imdb_points', instance.imdb_points)
        instance.save()
        return instance


class FilmModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'tytul', 'rok', 'opis', 'premiera', 'imdb_points']

    def create(self, validated_data):
        return Film.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.rok = validated_data.get('rok', instance.rok)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.premiera = validated_data.get('premiera', instance.premiera)
        instance.imdb_points = validated_data.get('imdb_points', instance.imdb_points)
        instance.save()
        return instance


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = '__all__'

    def create(self, validated_data):
        return ExtraInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.rok = validated_data.get('rok', instance.rok)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.premiera = validated_data.get('premiera', instance.premiera)
        instance.imdb_points = validated_data.get('imdb_points', instance.imdb_points)
        instance.save()
        return instance
