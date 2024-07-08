from django.http import JsonResponse
from rest_framework.views import APIView
from api.views_descrypt import decrypt_payload
import json


class ConsultaCPFView(APIView):
    def post(self, request):

        try:
            return JsonResponse(
                {"cpf_cliente": request.body["cpf_cliente"]}, status=200
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
