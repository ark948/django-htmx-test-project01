from django.urls import path
from tracker import views

app_name = "tracker"
urlpatterns = [
    path("", views.index, name='index'),
    path("html/", views.HtmlView.as_view()),
    path("jinja/", views.Jinja2View.as_view()),
]