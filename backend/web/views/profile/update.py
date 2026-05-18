from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.user import UserProfile
from web.views.utils.photo import remove_old_photo


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            username = request.data.get('username').strip()
            profile = request.data.get('profile').strip()[:500]
            photo = request.FILES.get('photo', None)

            if not username:
                return Response({
                    'result': 'User name is required.',
                })

            if not profile:
                return Response({
                    'result': 'User profile is required.',
                })

            if username != user.username and User.objects.filter(username=username).exists():
                return Response({
                    'result': 'User name already exists.',
                })

            if photo:
                remove_old_photo(user_profile.photo)
                user_profile.photo = photo

            user_profile.profile = profile
            user_profile.update_time = now()
            user_profile.save()

            user.username = username
            user.save()

            return Response({
                'result': 'success',
                'user_id': user.id,
                'username': user.username,
                'profile': user_profile.profile,
                'photo': user_profile.photo.url,
            })

        except:
            return Response({
                'result': 'Something went wrong, Try again later!'
            })