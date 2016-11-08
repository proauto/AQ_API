from django.conf.urls import url
from facebook.views import FaceBookView

urlpatterns = [
    # Class - based views
    url(r'^$', FaceBookView.as_view()),
]