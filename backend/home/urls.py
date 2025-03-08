from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('publish-article/<int:pk>/', views.publish_article, name='publish-article'),
]