import requests
import pandas
import json
from abc import ABC, abstractmethod
import time
from typing import Dict, List


##esse bloco ira buscar a cotação das ações e ira devolver ao valor de cada uma delas
def requestAPI():

    url = "https://brapi.dev/api/quote/PETR4,VALE3"
    response = requests.request("GET", url)
    dados_json = response.json()
    lista_de_acoes = dados_json['results']
    df = pandas.DataFrame(lista_de_acoes)
    return df

# regularMarketPrice sera o atributo base para o prototipo

class p_APIBolsa(ABC): #Contract
    @abstractmethod
    def receberValor(self , AcaoValor , varietion ) -> None:
        pass

#sistema Notificat
class BolsaDeValores:
    _observadores: Dict[str, List[p_APIBolsa]] = {}
    
    @staticmethod
    def add_observer(name: str, observador: p_APIBolsa):
        if not isinstance(observador, p_APIBolsa):
            print("Um objeto Nao pertence ao padrao p_API")
            return
        
        if name not in BolsaDeValores._observadores:
            BolsaDeValores._observadores[name] = []
        BolsaDeValores._observadores[name].append(observador) #adiciona o sistema que deseja receber a notificacao
        
    @staticmethod
    def post_notification(name: str, dados=None , varietion=None): #posta as notificacoes de valor atual da acao e da sua variacao de mercado
        if name in BolsaDeValores._observadores:
            for observador in BolsaDeValores._observadores[name]:
                observador.receberValor(dados, varietion)
                
                       

# construtor de dados notificados
class SistemaDeAlertaBolsa: #define os dados que serao notificados 
    def __init__(self):
       for i in range(len(requestAPI())):
            valor_dict = requestAPI().iloc[i].to_dict()
            BolsaDeValores.post_notification(name= valor_dict['symbol'] , dados= valor_dict['regularMarketPrice'] , varietion=valor_dict['fiftyTwoWeekRange'])
        

class BrunoContabilidades(p_APIBolsa):                #sistema integrado a minha "API"
    def __init__(self, Nome, Nome_acao):
        self.AcaoNome = Nome_acao
        self.AcaoValor = 0.0
        self.Nome = Nome
        self.varietion = None       
        BolsaDeValores.add_observer(self.AcaoNome , self)
    def receberValor(self , AcaoValor , varietion):
        print(f"O sistema {self.Nome} recebeu o novo valor da {self.AcaoNome} de atualmete {AcaoValor}. sua variacao de mercado e {varietion}")
        self.AcaoValor = AcaoValor
        self.varietion = varietion


class consultor(BrunoContabilidades):    #sistema Filho do BrunoContabilidades
   def __init__(self, Nome, Nome_acao):
       super().__init__(Nome, Nome_acao)

class VictorValores:
    
    def __init__(self, Nome, Nome_acao):
        self.AcaoNome = Nome_acao
        self.AcaoValor = 0.0
        self.Nome = Nome
        self.varietion = None       
        BolsaDeValores.add_observer(self.AcaoNome , self)
    def receberValor(self , AcaoValor , varietion):
        print(f"O sistema {self.Nome} recebeu o novo valor da {self.AcaoNome} de atualmete {AcaoValor}. sua variacao de mercado e {varietion}")
        self.AcaoValor = AcaoValor
        self.varietion = varietion



test = BrunoContabilidades(Nome= "BrunoContabilidade" , Nome_acao= "VALE3")
test2 = consultor(Nome= "Victor" , Nome_acao="PETR4")
test3 =VictorValores(Nome= "Victor" , Nome_acao="PETR4")
while True:     

    time.sleep(2)

    lupnotificat= SistemaDeAlertaBolsa()


