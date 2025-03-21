from django.urls import path
from . import views
from . import api


app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('publish-article/<int:pk>/', views.publish_article, name='publish-article'),
    path('api/', api.index)
]