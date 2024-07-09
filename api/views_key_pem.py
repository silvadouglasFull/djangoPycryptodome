import os
import json
from Crypto.Random import get_random_bytes


class KeyView:
    @staticmethod
    def generate_key(file_path):
        # Gerar uma chave AES de 16 bytes
        key = get_random_bytes(16)
        key_hex = key.hex()
        print(f"Chave AES: {key_hex}")

        # Escrever a chave em um arquivo .pem
        with open(file_path, "w") as file:
            file.write(f"{key_hex}")

        return key_hex

    @staticmethod
    def get_public_key():
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
                return ""

            # Caminho absoluto para o arquivo public_key.pem
            file_path = os.path.join(
                os.path.dirname(__file__),
                path_key_public[0],
                path_key_public[1],
                index_path,
                path_key_public[2],
            )

            try:
                with open(file_path, "rb") as file:
                    public_key_content = (
                        file.read()
                    )  # Lê o conteúdo do arquivo como bytes

                return bytes(public_key_content)

            except FileNotFoundError:
                print("File not found")
                return KeyView.generate_key(file_path)

            except Exception as e:
                print(e)
                return ""

        except FileNotFoundError:
            print("Config file not found")
            return ""

        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def get_private_key():
        # Caminho absoluto para o arquivo config.json
        config_file = os.path.join(os.path.dirname(__file__), "config", "config.json")

        try:
            with open(config_file, "r") as f:
                json_content = json.load(
                    f
                )  # Carrega o conteúdo do arquivo como um objeto JSON
                is_enable = json_content["cryptography"]["is_enable"]
                index_path = json_content["cryptography"]["index_path"]
                path_key_private = json_content["cryptography"]["path_key_private"]
            if not is_enable:
                # Se is_enable for falso, retornar uma mensagem indicando que está desativado
                return ""

            # Caminho absoluto para o arquivo private_key.pem
            file_path = os.path.join(
                os.path.dirname(__file__),
                path_key_private[0],
                path_key_private[1],
                index_path,
                path_key_private[2],
            )

            try:
                with open(file_path, "rb") as file:
                    private_key_content = (
                        file.read()
                    )  # Lê o conteúdo do arquivo como bytes

                return private_key_content

            except FileNotFoundError:
                print("File not found")
                return KeyView.generate_key(file_path)

            except Exception as e:
                print(e)
                return ""

        except FileNotFoundError:
            print("Config file not found")
            return ""

        except Exception as e:
            print(e)
            return ""
