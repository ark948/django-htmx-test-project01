from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        return Response('hi')