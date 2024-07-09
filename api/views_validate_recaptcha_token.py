import requests
from api.views_config import get_config


def verificar_token(request):
    try:
        config = get_config()
        is_enable = config["repactcha"]["is_enable"]
        host = config["repactcha"]["host"]
        secret_key = config["repactcha"]["secret_key"]
        if not is_enable:
            return False

        token = request.headers.get("Recaptcha-Token")
        client_ip = request.META.get("REMOTE_ADDR")
        if token:
            verify_url = host
            payload = {"secret": secret_key, "response": token, "remoteip": client_ip}
            response = requests.post(verify_url, data=payload)
            data = response.json()
            print(data)
            if data.get("success"):
                return True
            else:
                return False
        else:
            return False
    except requests.RequestException as e:
        print(f"Erro na requisição do recaptcha: {e}")
        return False
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False
