from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from http import HTTPStatus
from . import throttles
from . import serializers




@api_view(['GET', 'POST'])
@throttle_classes([throttles.CustomThrottleForFuncViews])
def index(request):
    if request.method == 'POST':
        serializer = serializers.SampleSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
    elif request.method == 'GET':
        serializer = serializers.SampleSerializer()
        return Response(serializer.data)
    


class SampleView(APIView):
    throttle_scope = 'basic'
    def get(self, request, format=None):
        return Response('hi')