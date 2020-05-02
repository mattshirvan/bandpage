from django.conf.urls import url
from . import views

# app name for urls 
app_name = "oldband"

# url patterns for band app
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
    url(r'^discography$', views.DiscographyView.as_view(), name="discography"),
    url(r'^tour$', views.TourView.as_view(), name="tour"),
    url(r'^video$', views.VideoView.as_view(), name="video"),
    url(r'^game$', views.GameView.as_view(), name="game"),
    url(r'^contact$', views.ContactView.as_view(), name="contact"),
]