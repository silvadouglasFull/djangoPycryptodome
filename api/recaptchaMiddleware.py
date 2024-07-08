# api/middleware.py
from api.views_validate_recaptcha_token import verificar_token
from django.http import JsonResponse
from api.views_config import get_config


class encryptMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            config = get_config()
            is_enable = config["repactcha"]["is_enable"]
            if not is_enable:
                response = self.get_response(request)
                return response
            is_valid = verificar_token(request=request)
            if not request.headers.get("Recaptcha-Token"):
                print("Não encontramos o campo Recaptcha-Token no cabeçalho")
            if not is_valid:
                return JsonResponse(
                    {"message": "Token recaptcha Não é válido"}, status=403
                )
            response = self.get_response(request)
            return response
        except Exception as e:
            error_message = {
                "error": f"Erro durante o processamento da requisição: {str(e)}"
            }
            return JsonResponse(error_message, status=500)
