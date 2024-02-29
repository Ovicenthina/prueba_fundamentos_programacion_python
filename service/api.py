import requests
import json


#Llamar a la api para recopilar la informacion
def obtener_aves(url):
    
    """
    Llama a la API para extraer la informacion sobre las aves

    :param url: La URL de la API
    :type url: (dict)
    :return: dict - diccionario con la informacion si la consulta es exitosa de lo contrario None
    """
    response = requests.request("GET",url)
    if response.status_code ==200:
        content = response.content
        print(f'Consulta exitosa a la API {url}\n')
        return json.loads(content)
    else:
        print(f'Error al obtener datos de la API. Código de estado: {response.status_code}')
        return None
    
# api_aves = obtener_aves(url)
# print(api_aves[0].keys())



