from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views import generic
from django.http import HttpResponse
# Create your views here.


# -- ListView
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark


class FaceBookView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '2318934571':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')