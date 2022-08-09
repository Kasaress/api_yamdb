from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdmin
from .serializers import UserSerializer
from .utils import generate_confirmation_code, send_confirmation_code

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        user = User.objects.filter(email=email, username=username)
        if len(user) > 0:
            if user.confirmation_code:
                send_confirmation_code(email, user.confirmation_code)
            else:
                confirmation_code = generate_confirmation_code()
                send_confirmation_code(email, user.confirmation_code)
        else:
            confirmation_code = generate_confirmation_code()
            data = {'email': email, 'confirmation_code': confirmation_code,
                    'username': username}
            serializer = UserSerializer(data=data)
            serializer.is_valid()
            serializer.save()
        send_confirmation_code(email, confirmation_code)
        return Response(f'Код отправлен на почту {email}')



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin,]
    lookup_field = 'username'
