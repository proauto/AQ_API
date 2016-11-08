from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
# Create your views here.


# -- ListView
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

