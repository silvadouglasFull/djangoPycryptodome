from django.http import JsonResponse
from rest_framework.views import APIView
import os
import json


class PublicKeyView(APIView):
    def get(self, request):
        # Caminho absoluto para o arquivo config.json
        config_file = os.path.join(os.path.dirname(__file__), "config", "config.json")

        try:
            with open(config_file, "r") as f:
                json_content = json.load(
                    f
                )  # Carrega o conteúdo do arquivo como um objeto JSON
                is_enable = json_content["cryptography"]["is_enable"]
                index_path = json_content["cryptography"]["index_path"]
                path_key_public = json_content["cryptography"]["path_key_public"]
            if not is_enable:
                # Se is_enable for falso, retornar uma mensagem indicando que está desativado
                return JsonResponse(
                    {"message": "Encryption is disabled", "public_key": ""}, status=200
                )

            # Caminho absoluto para o arquivo public_key.pem
            file_path = os.path.join(
                os.path.dirname(__file__),
                path_key_public[0],
                path_key_public[1],
                index_path,
                path_key_public[2],
            )

            try:
                with open(file_path, "r") as file:
                    public_key_content = (
                        file.read()
                    )  # Lê o conteúdo do arquivo como uma string

                return JsonResponse({"public_key": public_key_content}, status=200)

            except FileNotFoundError:
                return JsonResponse({"error": "File not found"}, status=404)

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)

        except FileNotFoundError:
            return JsonResponse({"error": "Config file not found"}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
