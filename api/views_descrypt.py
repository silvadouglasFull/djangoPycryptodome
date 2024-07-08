from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import json
from api.views_config import get_config
from api.views_key_pem import KeyView


@csrf_exempt
def decrypt_payload(request):
    try:
        config = get_config()
        is_enable = config["cryptography"]["is_enable"]
        SECRET_KEY = KeyView.get_public_key()
        print(f"Tamanho da chave: {len(SECRET_KEY)} bytes")  # Deve ser 32 bytes
        if SECRET_KEY == "":
            return request
        body = json.loads(request.body)
        if not is_enable:
            return body
        payload = base64.b64decode(body.get("payload"))
        iv = base64.b64decode(body.get("iv"))
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        print(SECRET_KEY)
        decrypted = unpad(cipher.decrypt(payload), AES.block_size)
        data = json.loads(decrypted.decode("utf-8"))

        # Aqui você pode processar os dados descriptografados
        response = {}
        for field, value in data.items():
            response[field] = value
        return response

    except (ValueError, KeyError) as e:
        print(e)
        return request
