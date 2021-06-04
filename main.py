import requests

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    #peticion al servidor 
    response = requests.get(URL)

    #si es exitosa se 
    if response.status_code == 200:
        #respuesta del servidor
        content = response.text

        with open('econpy.html','w+') as file:
           file.write(content)
