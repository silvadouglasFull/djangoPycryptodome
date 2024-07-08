from django.http import JsonResponse
from rest_framework.views import APIView

from api.views_descrypt import Decrypt


class ConsultaCPFView(APIView):
    def post(self, request):

        # try:
        payload = request.data
        cpf_cliente = payload.get("cpf_cliente")
        Decrypt.descript(request=request)
        return JsonResponse({"data": {"cpf_cliente": cpf_cliente}}, status=200)

    # except FileNotFoundError:
    #     return JsonResponse({"error": "File not found"}, status=404)
    # except Exception as e:
    #     return JsonResponse({"error": str(e)}, status=500)
