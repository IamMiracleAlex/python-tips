from django.urls import path

from tweets import views

urlpatterns = [
    path('', views.TweetList.as_view()),
]