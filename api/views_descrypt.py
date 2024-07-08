import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import json


class Decrypt:
    def descript(request):

        # Caminho absoluto para o arquivo config.json
        config_file = os.path.join(os.path.dirname(__file__), "config", "config.json")
        with open(config_file, "r") as f:
            json_content = json.load(
                f
            )  # Carrega o conteúdo do arquivo como um objeto JSON
            is_enable = json_content["cryptography"]["is_enable"]
            index_path = json_content["cryptography"]["index_path"]
            path_key_private = json_content["cryptography"]["path_key_private"]
        if not is_enable:
            # Se is_enable for falso, retornar uma mensagem indicando que está desativado
            return request.data

        private_key_path = os.path.join(
            os.path.dirname(__file__),
            path_key_private[0],
            path_key_private[1],
            index_path,
            path_key_private[2],
        )
        with open(private_key_path, "r") as file:
            private_key = file.read()  # Lê o conteúdo do arquivo como uma string
        rsa_key = RSA.import_key(private_key, passphrase="2024master")
        cipher = PKCS1_OAEP.new(rsa_key)
        object = request.data.items()
        decrypted_data = {}
        try:
            for field, value in object:
                # Exemplo de descriptografia
                encrypt_data = base64.b64decode(value)
                print(value)
                decrypt_data = cipher.decrypt(encrypt_data)
                decrypted_data[field] = decrypt_data.decode("utf-8")
        except ValueError as e:
            print(f"Erro durante a descriptografia: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

        print(decrypted_data)
