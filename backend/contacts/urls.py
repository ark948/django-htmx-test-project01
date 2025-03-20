from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ContacList.as_view(), name='list'),
    path('search/', views.search_contacts, name='search'),
    path('new/', views.new_contact, name='new'), # my own
    path('create/', views.create_contact, name='create'),
    path('test-page/', views.custom_htmx_page, name='test'),
]