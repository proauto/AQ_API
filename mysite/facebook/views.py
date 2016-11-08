from django.views import generic
from django.http import HttpResponse
# Create your views here.

class FaceBookView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'WEBHOOK':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')