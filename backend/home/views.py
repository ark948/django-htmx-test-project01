from django.shortcuts import render
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods



from .models import Article



def index(request: HttpRequest) -> HttpResponse:
    context = {'articles': Article.objects.all()}
    return render(request, 'index.html', context)



@require_http_methods(['POST'])
def publish_article(request, pk):
    print("\n", pk, "\n")