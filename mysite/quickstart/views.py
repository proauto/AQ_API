from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from quickstart.serializers import UserSerializer, GroupSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET'])
def FaceBookView(request):
        if request.GET['hub.verify_token'] == 'WebHook':
            return Response(request.GET['hub.challenge'])
        else:
            return Response('Error, invalid token')
