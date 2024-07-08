from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
class HelloWorldView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Hello world"})