from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data['username'].strip()
            password = request.data['password'].strip()
            if not username or not password:
                return Response({
                    'result': 'username or password is required'
                })

            user = authenticate(username=username, password=password)
            if user: # 用户名密码正确
                user_profile = UserProfile.objects.get(user=user)
                refresh = RefreshToken.for_user(user) # 生成jwt
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                    'user_id': user.id,
                    'username': user.username,
                    'photo': user_profile.photo.url, # 必须加url才能返回路径
                    'profile': user_profile.profile,
                })

                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age= 86400 * 7,
                )

                return response
            return Response({
                'result': 'username or password is wrong'
            })

        except:

            return Response({
                'result': 'System error, try again later',
            })