from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    response = render(request, "jinja/index.jinja")
    return response



class Jinja2View(TemplateView):
    template_name = "jinja/tracker/index.jinja"


class HtmlView(TemplateView):
    template_name = "html/tracker/index.html"


