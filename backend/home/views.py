from django.shortcuts import render
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404



from .models import Article



def index(request: HttpRequest) -> HttpResponse:
    context = {'articles': Article.objects.all()}
    return render(request, 'index.html', context)



@require_http_methods(['POST'])
def publish_article(request: HttpRequest, pk: int) -> JsonResponse:
    article = get_object_or_404(Article, pk=pk)
    article.published = True
    article.save()
    return JsonResponse({'status': 'published'})