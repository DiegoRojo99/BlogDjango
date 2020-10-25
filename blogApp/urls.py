from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:postTitle>', views.postDetail, name='postDetail'),
    path('equipo/<str:teamName>', views.team, name='equipo'),
    path('tag/<str:tagName>', views.tag, name='tag'),
    path('tema/<str:temaName>', views.theme, name='tema'),
    path('liga', views.league, name='liga'),
    path('temas', views.temas, name='temas'),
    path('tags', views.tags, name='tags'),
]