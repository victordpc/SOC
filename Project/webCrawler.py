#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import sys
import os

#procesarPagina done by Guillermo Jiménez Díaz
#there has been slightly modifications to his code
def procesarPagina(url):
    """
    Carga y  procesa el contenido de una URL usando request
    Muestra un mensaje de error en caso de no poder cargar la página
    """
    # Realizamos la petición a la web
    req = requests.get(url)

    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text,'html.parser')
        
        # Devolvemos el html cargado
        return html        
        
    else:
        print ("ERROR {}".format(statusCode))

url="https://boardgamegeek.com/boardgame/13/catan/ratings?pageid="
soup = procesarPagina(url + '1')

#<a class="comment-header-user" ng-href="/user/name" href="/user/name">name</a>
#Open file
file = open('user_names','w')
#Initialize counter and condition
cont = 1
condition = True
print ('Start!\n')

while condition:
	#Selection of the button to see if its active
	button = soup.select('button.btn.btn-xs.btn-subtle')
    print ('Page: %s\n' % (str(cont)))
    if 'uib-tooltip' in button:
        if button['uib-tooltip'] == "Next Page":
            #If not active exit while
            if 'disabled' in button:
                condition = False
                print ('Done!\n')
			#If active we continue recopilating data
            else:
				#Selection of the user names
                data = soup.select('a.comment-header-user')
                for i in data:
                    print ('.-%s\n' %(i.text)) 
                    file.write(i.text + '\n')
                    #Load of the next page
                cont = cont + 1				
                soup = procesarPagina(url + str(cont))
file.close()
