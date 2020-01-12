from time import time

import os
import sys
import csv
import requests
import json

URL = 'https://jsonplaceholder.typicode.com/users/?username='
FILENAME = 'cache.csv'
COLUNMS = ['username', 'email', 'website', 'hemisphere']


def verifyEmpty():
    """Verifica se o o csv está vazio,caso sim adiciona o titulo das colunas"""

    with open(FILENAME, 'r') as FILE:
        row_count = sum(1 for row in csv.reader(FILE))
        if row_count == 0:
            with open(FILENAME, 'a') as F:
                writer = csv.writer(F)
                writer.writerow(COLUNMS)


def writeCSV(params):
    """Escreve no csv os parametros passados.

    Parameters:
        params (list): Lista contendo os valores a serem adicionados no csv.

    """
    with open(FILENAME, 'a') as FILE:
        csv_write = csv.writer(FILE)
        csv_write.writerow(params)


def storeCache():
    """Armazena todo os valore em cache à uma variavél global"""

    global data
    data = {}
    with open(FILENAME, 'r') as FILE:
        csv_read = csv.DictReader(FILE)
        for row in csv_read:
            data.update({
                row['username']: {
                    'username': row['username'],
                    'website': row['website'],
                    'email': row['email'],
                    'hemisphere': row['hemisphere']
                }
            })


def showUser(params):
    """Mostra o usuário e seus respectivos valores em tela

    Parameters:
        params (list): Dados do usuário.

    """

    print('''
{}'s Data

Email: {}
Website: {}
Hemisphere: {}
              '''.format(params[0], params[1], params[2], params[3]))


def getData(username):
    """Consulta os dados do usuário passado, caso o usuário esteja guardado em cache
       será consultado dentro dá variavel global, caso não, será consultado por uma
       requisição à api.

    Parameters:
        username (string): Nome do usuário a ser consultado.

    """

    initial_time = time()
    user = data.get(username)

    if user is None:
        try:
            response = requests.get(URL+username).json()[0]
        except ConnectionError:
            print('Internet não está Funcionando')

            return
        except:
            print('Não existe o usuário no banco de dados')

            return

        user = [username,
                response['email'],
                response['website'],
                'norte' if float(response['address']
                                 ['geo']['lat']) > 0 else 'sul']

        writeCSV(user)
    else:
        user = list(user.values())

    showUser(user)

    print('''Tempo de Execução:  {} '''.format(time()-initial_time))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        # Seu código entra aqui
        verifyEmpty()
        storeCache()
        getData(username)
    else:
        print("Passe um username")
