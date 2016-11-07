from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins
from mysite.quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework.views  import APIView

class UserViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GroupViewSet(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
