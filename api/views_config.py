import json
from django.http import JsonResponse
from django.views import View
import os

def get_config():
    # Caminho absoluto para o arquivo config.json
    file_path = os.path.join(os.path.dirname(__file__), 'config', 'config.json')

    try:
        with open(file_path, 'r') as file:
            config_data = json.load(file)
            return config_data
        
    except FileNotFoundError:
        raise Exception("Config file not found")
    
    except json.JSONDecodeError as e:
        raise Exception(f"Error decoding JSON: {str(e)}")
    
    except Exception as e:
        raise Exception(str(e))

class ConfigView(View):
    def get(self, request):
        try:
            config_data = get_config()
            return JsonResponse(config_data, status=200)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
