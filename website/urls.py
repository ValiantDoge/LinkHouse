from website import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<slug:profile_slug>', views.profile, name="profile")
]
