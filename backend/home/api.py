from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from .throttles import CustomThrottleForFuncViews




@api_view(['GET'])
@throttle_classes([CustomThrottleForFuncViews])
def index(request):
    if request.method == 'GET':
        return Response('hi')
    


class SampleView(APIView):
    throttle_scope = 'basic'
    def get(self, request, format=None):
        return Response('hi')