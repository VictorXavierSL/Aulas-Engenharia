import requests
import pandas
import json
from typing import Protocol
import time
##esse bloco ira buscar a cotação das ações e ira devolver ao valor de cada uma delas
def requestAPI():

    url = "https://brapi.dev/api/quote/PETR4,VALE3"
    response = requests.request("GET", url)
    dados_json = response.json()
    lista_de_acoes = dados_json['results']
    df = pandas.DataFrame(lista_de_acoes)
    return df
# regularMarketPrice sera o atributo base para o prototipo



#sistema Notificat
class BolsaDeValores:
    _observadores = {}
    
    @staticmethod
    def add_observer(name: str, callback_method):
        if name not in BolsaDeValores._observadores:
            BolsaDeValores._observadores[name] = []
        BolsaDeValores._observadores[name].append(callback_method)

    @staticmethod
    def post_notification(name: str, dados=None):
        if name in BolsaDeValores._observadores:
            for method in BolsaDeValores._observadores[name]:
                method(dados)


class SistemaDeAlertaBolsa:
    def __init__(self, ):
       for i in range(len(requestAPI())):
            valor_dict = requestAPI().iloc[i].to_dict()
            BolsaDeValores.post_notification(name= valor_dict['symbol'] , dados= valor_dict['regularMarketPrice'])
        



class p_APIBolsa(Protocol):
    def __init__(self , Nome , Nome_acao):
        self.nome = Nome
        self.AcaoNome = Nome_acao
        self.AcaoValor = 0.0
        
        BolsaDeValores.add_observer(Nome_acao , self.receberValor)
    def receberValor(self , AcaoValor):
        ...


class BrunoContabilidades:
    def __init__(self, Nome, Nome_acao):
        self.AcaoNome = Nome_acao
        self.AcaoValor = None
        self.Nome = Nome
        BolsaDeValores.add_observer(self.AcaoNome , self.receberValor)
    def receberValor(self , AcaoValor):
        print(f"O sistema {self.Nome} recebeu o novo valor da {self.AcaoNome} de atualmete {AcaoValor}")
        self.AcaoValor = AcaoValor

class consultor(BrunoContabilidades):
   
   def receberValor(self , AcaoValor):
        print(f"O sistema {self.Nome} recebeu o novo valor da {self.AcaoNome} de atualmete {AcaoValor}")
        self.AcaoValor = AcaoValor

test = BrunoContabilidades(Nome= "BrunoContabilidade" , Nome_acao= "VALE3")
test2 = consultor(Nome= "Victor" , Nome_acao="PETR4")
while True:     

    time.sleep(2)

    lupnotificat= SistemaDeAlertaBolsa()


