# api/views.py

import os
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import action


class EncryptographyView(APIView):
    def get(self, request):
        print(request.path)
        return JsonResponse({"message": "OI"})
