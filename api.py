

import requests
import json

# esse link pode mudar se os donos da API mudarem
#cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#cotacoes_dic = cotacoes.json()
#cotacao_dolar = cotacoes_dic['USDBRL']['bid']
lista_campos = requests.get("https://plugcrm.net/api/v1/tasks?token=6205315036fb10000fb934fa")
rd_teste_j2 = lista_campos.json()

for key in rd_teste_j2:
    if key == "tasks":
        for key2 in rd_teste_j2[key]:
            deal_id = ""
            subject = ""
            type = ""
            hour = ""
            data = ""
            user_ids = ""
            
            for key3 in key2:
                if key3 == "deal_id":
                    deal_id = key2[key3]
                if key3 == "subject":
                    subject = key2[key3]
                if key3 == "type":
                    type = key2[key3]    
                if key3 == "hour":
                    hour = key2[key3]
                if key3 == "data":
                    data = key2[key3] 
                if  key3 == "user_ids": 
                    user_ids = key2[key3]
print(rd_teste_j2)    
                                   
            # params = {
            #     'token':'6205315036fb10000fb934fa',
            #     'deal_id': deal_id,
            #     'subject' : subject,
            #     'type' : type,
            #     'hour' : hour,
            #     'data' : data,
            #     'user_ids' : user_ids                
            # }

            # rd_teste = requests.post("https://plugcrm.net/api/v1/tasks",params)
            # rd_teste_j =rd_teste.json()
            # print(rd_teste_j)
           
       #
         #   funcao_createTask({'deal_id': deal_id})     
                    


#funcao_createTask(obj){


#rd_api = rd_teste['page']['limit']['deal_id']['done']

#print(rd_teste_j)  
#}
