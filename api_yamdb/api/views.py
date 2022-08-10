from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
# from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import mixins, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reviews.models import Category, Genre, Title

from .permissions import IsAdmin
from .serializers import SignUpSerializer, TokenSerializer, UserSerializer
from .serializers import TitleReadSerializer, TitleWriteSerializer,\
    CategorySerializer, GenreSerializer
from .utils import generate_confirmation_code, send_confirmation_code

User = get_user_model()

PERMISSION_CLASS = [IsAuthenticatedOrReadOnly, IsAdmin]


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid()
        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')
        if serializer.is_valid():
            confirmation_code = generate_confirmation_code()
            user = User.objects.filter(email=email).exists()
            if not user:
                User.objects.create_user(email=email, username=username)
                User.objects.filter(email=email).update(
                confirmation_code = generate_confirmation_code())
                send_confirmation_code(email, confirmation_code)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('Такой пользователь уже зарегистирован', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        confirmation_code = request.data.get('confirmation_code')
        user = get_object_or_404(
            User,
            username=username,
        )
        if user.confirmation_code != confirmation_code:
            return Response(
                'Confirmation code is invalid',
                status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response(
            {'access_token': str(refresh.access_token)},
            status=status.HTTP_200_OK
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin, ]
    lookup_field = 'username'
    search_fields = ('username', )


class CLDMixinSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class GenreViewSet(CLDMixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = PERMISSION_CLASS
    pagination_class = PageNumberPagination
    search_fields = ('name',)
    lookup_field = "slug"
    # filter_backends = DjangoFilterBackend


class CategoryViewSet(CLDMixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = PERMISSION_CLASS
    pagination_class = PageNumberPagination
    search_fields = ('=name',)
    lookup_field = "slug"
    # filter_backends =


class TitleViewSet(CLDMixinSet):
    queryset = Title.objects.all()  # .annotate(Avg('reviews__score'))
    # annotate(rating=Avg('reviews__score')).order_by('name')
    permission_classes = PERMISSION_CLASS
    pagination_class = PageNumberPagination
    search_fields = ('=name',)
    lookup_field = "slug"
    # filter_backends = DjangoFilterBackend

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer
