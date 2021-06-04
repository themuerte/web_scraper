from os import POSIX_FADV_RANDOM
import requests

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    #peticion al servidor 
    response = requests.get(URL)

    #si es exitosa se 
    if response.status_code == 200:
        #respuesta del servidor
        content = response.text

        regex_a = '<div title="buyer-name">'
        regex_b = '</div>'
        
        for line in content.split('\n'):
            
            if regex_a in line:
                
                start = line.find(regex_a) + len(regex_a)
                end = line.find(regex_b)

                title = line[start:end]

                print(title)
                