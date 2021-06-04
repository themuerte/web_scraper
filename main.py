from os import POSIX_FADV_RANDOM
import requests
import re

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    #peticion al servidor 
    response = requests.get(URL)

    #si es exitosa se 
    if response.status_code == 200:
        #respuesta del servidor
        #obteniendo el maquetado
        content = response.text

        regex = '<div title="buyer-name">(.+?)</div>'

        for title in re.findall(regex, content):
            print(title)