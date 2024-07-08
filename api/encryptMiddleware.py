# api/middleware.py
from api.views_descrypt import decrypt_payload
from api.views_config import get_config
from django.http import JsonResponse


class encryptMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Antes de chamar a view, podemos manipular a requisição se necessário
            config = get_config()
            is_enable = config["cryptography"]["is_enable"]
            if not is_enable:
                response = self.get_response(request)
                print("A criptografia não está ativada")
                return response
            if not request.body:
                print("Não há um corpo na requisição, nada a ser feito")
                return self.get_response(request)
            request._body = decrypt_payload(request)
            response = self.get_response(request)
            return response

        except Exception as e:
            error_message = {
                "error": f"Erro durante o processamento da requisição: {str(e)}"
            }
            return JsonResponse(error_message, status=500)
