import datetime as dt
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Genre, Title
from django.core.validators import MaxValueValidator

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=254, required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        max_length=150, required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = (
            'email',
            'username')

    def validate_username(self, name):
        if name == 'me':
            raise serializers.ValidationError(
                "Использовать 'me' для username нельзя."
            )
        return name  


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code')

    def validate(self, data):
        username = data.get('username')
        confirmation_code = data.get('confirmation_code')
        if not username and not confirmation_code:
            raise serializers.ValidationError(
                f"Пустые поля: {username}, {confirmation_code}"
            )
        return data

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError(
                "Поле username не должно быть пустым"
            )
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email',
            'first_name', 'last_name',
            'bio', 'role',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')
        read_only_fields = ('role',)

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    description = serializers.CharField(required=False)
    rating = serializers.FloatField(source='reviews__score__avg',
                                    read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'description', 'category',
                  'genre', 'year', 'rating')


class TitleWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all())
    year = serializers.IntegerField(
        validators=[MaxValueValidator(dt.date.today().year)]
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'description', 'category',
                  'genre', 'year')

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Неверный год')
        return value
