from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign', views.signup, name='signup'),
    path('login', views.login1, name='login1'),
    path('instructions', views.inst, name='inst'),
    path('ctf/first.html', views.first, name='first'),
    path('logout', views.logout, name='logout'),
    path('leaderboard', views.leaderboard, name='leaderboard')
]
