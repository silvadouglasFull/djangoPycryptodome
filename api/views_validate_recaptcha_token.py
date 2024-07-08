import requests
from api.views_config import get_config


def verificar_token(request):
    config = get_config()
    is_enable = config["repactcha"]["is_enable"]
    host = config["repactcha"]["host"]
    secret_key = config["repactcha"]["secret_key"]
    if not is_enable:
        return False

    token = request.headers.get("Recaptcha-Token")
    if token:
        verify_url = f"{host}={secret_key}&response={token}"
        response = requests.post(verify_url)
        data = response.json()
        if data.get("success"):
            return True
        else:
            return False
    else:
        return False
