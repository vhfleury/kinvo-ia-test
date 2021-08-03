from flask import Flask
import os
from extrair import noticias 

app = Flask(__name__)

@app.route('/get_news',methods=['PUT'])
def createTask():
    os.system("scrapy runspider raspagem.py -o ../news/noticias_extraidas.csv")

    if os.path.exists("../news/noticias_extraidas.csv"):
        resposta = get_response(200, "success")
    else:
        resposta = get_response(503, "ocorreu algum erro na hora de puxar as noticias")


    return resposta


@app.route('/get_entity',methods=['GET'])
def getTasks():
    # return all named entity from news
    try:
        dados = noticias().main()
        response = get_response(200, "success", 'data', dados)
    except:
        response = get_response(404, "arquivo nao encontrado, tente rodar puxar novamente as noticias")

    

    return  response


def get_response(status, mensagem, nome_conteudo=False, conteudo=False):

    response = {}
    response["status"] = status
    response['mensagem'] = mensagem

    if nome_conteudo and conteudo:
        response[nome_conteudo] = conteudo

    return response