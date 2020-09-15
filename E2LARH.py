import requests
import os
import sys
try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install bs4')
    print('Instalando BeautifulSoup')
    exit()
try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    print('Instalando webbrowser')
    exit()

# Luis Alfredo Ramirez Huerta

print("Este script navega en las páginas de noticas de la UANL")
inicial = int(input("Pagina inicial para buscar: "))
final = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")

# Si hay error de usuario confundiendo el inicial con el final se invierten
# para que los valores sean correctos
if inicial > final:
    inicial, final = final, inicial

# Busca en la lista de la pagina de noticias el contenido en HTML cualquier
# coincidencia con la variable 'dependencia' y al encontrarse una o más
# inicie el navegador abriendo el link que coincide con la variable
for i in range(inicial, final, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo", url2)
                        webbrowser.open(url2)
                        break
