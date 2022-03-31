import requests
import json
#from flask import Flask

#api = Flask(__name__)

# lista_campos = requests.get("https://plugcrm.net/api/v1/deals?token=6205315036fb10000fb934fa")
# rd_teste_j2 = lista_campos.json()

# for key in rd_teste_j2:
#     if key == "deals":
#         for key2 in rd_teste_j2[key]:
#             page = "" 
#             name = ""
#             win = ""
#             user_id = ""
#             closed_at = ""
#             closed_at_period = ""
#             created_at_period = ""
#             prediction_date_period = ""
#             start_date = ""
#             end_date = ""           
#             campaign_id = ""
#             deal_stage_id = ""
#             deal_lost_reason_id = ""
#             hold = ""
            
            
#             for key3 in key2:
#                 if key3 == "page":
#                     page = key2[key3]
#                 if key3 == "name":
#                     name = key2[key3]
#                 if key3 == "win":
#                     win = key2[key3]    
#                 if key3 == "user_id":
#                     user_id = key2[key3]
#                 if key3 == "closed_at":
#                     closed_at = key2[key3] 
#                 if  key3 == "closed_at_period": 
#                     closed_at_period = key2[key3]
#                 if key3 =='created_at_period': 
#                    created_at_period = key2[key3] 
#                 if key3 == 'prediction_date_period':
#                    prediction_date_period = key2[key3]
#                 if key3 == 'start_date':
#                    start_date = key2[key3]
#                 if key3 == 'end_date':
#                    end_date = key2[key3]
#                 if key3 == 'campaign_id':         
#                    campaign_id = key2[key3]
#                 if key3 == 'deal_stage_id':
#                    deal_stage_id = key2[key3]  
#                 if key3 == 'deal_lost_reason_id':
#                     deal_lost_reason_id = key2[key3]
#                 if key3 == 'hold':
#                   hold = key2[key3]  
                  
    
    
#     # print(rd_teste_j2)    
#         params = {'page':page,
#                   'name':name,
#                   'win':win,
#                   'user_id':user_id,
#                   'closed_at':closed_at,
#                   'created_at_period':created_at_period,
#                   'prediction_date_period':prediction_date_period,
#                   'start_date':start_date,
#                   'end_date' :end_date, 
#                   'campaign_id':campaign_id,
#                   'deal_lost_reason_id':deal_lost_reason_id,
#                   'deal_stage_id':deal_stage_id,
#                   'hold':hold
#                   }

oportunidades = requests.get("https://plugcrm.net/api/v1/deals?token=6205315036fb10000fb934fa")
result_oportunidades = oportunidades.json()

tarefas = requests.get ("https://plugcrm.net/api/v1/tasks?token=6205315036fb10000fb934fa")
result_tarefas = tarefas.json()

anotações = requests.get ("https://plugcrm.net/api/v1/activities?token=6205315036fb10000fb934fa")
result_anotações = anotações.json()

# lista_oportunidades = requests.get("https://plugcrm.net/api/v1/deals/ID_DA_OPORTUNIDADE/deal_products?token=6205315036fb10000fb934fa")
# result_list_oportunidades = lista_oportunidades.json()

empresas = requests.get("https://plugcrm.net/api/v1/organizations/?token=6205315036fb10000fb934fa&page=1&limit=200")
result_empresas = empresas.json()

contatos = requests.get("https://plugcrm.net/api/v1/contacts?token=6205315036fb10000fb934fa")
result_contatos = contatos.json()

produtos = requests.get("https://plugcrm.net/api/v1/products?token=6205315036fb10000fb934fa")
result_produtos = produtos.json()

f = open("Oportunidades.json","w")
result_json = json.dumps(result_oportunidades)
f.write(result_json)
f.close()

f2 = open("Tarefas.json","w")
result_json2 = json.dumps(result_tarefas)
f2.write(result_json2)
f2.close()

f3 = open("Anotações.json","w")
result_json3 = json.dumps(result_anotações)
f3.write(result_json3)
f3.close()

# f4 = open("Lista_oportunidades.json","w")
# result_json4 = json.dumps(result_list_oportunidades)
# f4.write(result_json4)
# f4.close()

f5 = open("Empresas.json","w")
result_json5 = json.dumps(result_empresas)
f5.write(result_json5)
f5.close()

f6 = open("Contatos.json","w")
result_json6 = json.dumps(result_contatos)
f6.write(result_json6)
f6.close() 

f7=open("Produtos.json","w")
result_json7 = json.dumps(result_produtos)
f7.write = result_json7
f7.close()

          
       