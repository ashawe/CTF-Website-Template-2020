from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('register', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('login', views.login1, name='login1'),
    path('instructions', views.inst, name='inst'),
    path('QUEST', views.first, name='first'),
    path('logout', views.logout, name='logout'),
    path('leaderboard', views.leaderboard, name='leaderboard')
]
