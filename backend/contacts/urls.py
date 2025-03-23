from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ContacList.as_view(), name='list'),
    path('search/', views.search_contacts, name='search'),
    path('new/', views.new_contact, name='new'), # my own
    path('create/', views.create_contact, name='create'),
    path('delete/<int:pk>/', views.delete_contact, name='delete'), # my own
    path('test-page/', views.custom_htmx_process01, name='test'), # my own
    path('export/', views.export, name='export'),
    path('charts/', views.charts, name='charts'),
]