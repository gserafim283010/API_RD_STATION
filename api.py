import requests
import json
#from flask import Flask

#api = Flask(__name__)

lista_campos = requests.get("https://plugcrm.net/api/v1/deals?token=6205315036fb10000fb934fa")
rd_teste_j2 = lista_campos.json()

for key in rd_teste_j2:
    if key == "deals":
        for key2 in rd_teste_j2[key]:
            page = "" 
            name = ""
            win = ""
            user_id = ""
            closed_at = ""
            closed_at_period = ""
            created_at_period = ""
            prediction_date_period = ""
            start_date = ""
            end_date = ""           
            campaign_id = ""
            deal_stage_id = ""
            deal_lost_reason_id = ""
            hold = ""
            
            
            for key3 in key2:
                if key3 == "page":
                    page = key2[key3]
                if key3 == "name":
                    name = key2[key3]
                if key3 == "win":
                    win = key2[key3]    
                if key3 == "user_id":
                    user_id = key2[key3]
                if key3 == "closed_at":
                    closed_at = key2[key3] 
                if  key3 == "closed_at_period": 
                    closed_at_period = key2[key3]
                if key3 =='created_at_period': 
                   created_at_period = key2[key3] 
                if key3 == 'prediction_date_period':
                   prediction_date_period = key2[key3]
                if key3 == 'start_date':
                   start_date = key2[key3]
                if key3 == 'end_date':
                   end_date = key2[key3]
                if key3 == 'campaign_id':         
                   campaign_id = key2[key3]
                if key3 == 'deal_stage_id':
                   deal_stage_id = key2[key3]  
                if key3 == 'deal_lost_reason_id':
                    deal_lost_reason_id = key2[key3]
                if key3 == 'hold':
                  hold = key2[key3]  
                  
    
    
    # print(rd_teste_j2)    
        params = {'page':page,
                  'name':name,
                  'win':win,
                  'user_id':user_id,
                  'closed_at':closed_at,
                  'created_at_period':created_at_period,
                  'prediction_date_period':prediction_date_period,
                  'start_date':start_date,
                  'end_date' :end_date, 
                  'campaign_id':campaign_id,
                  'deal_lost_reason_id':deal_lost_reason_id,
                  'deal_stage_id':deal_stage_id,
                  'hold':hold
                  }

rd_teste = requests.get("https://plugcrm.net/api/v1/deals?token=6205315036fb10000fb934fa",params)
rd_teste_j = rd_teste.json()
#@api.route('/')
#def index():
f = open("Resultado.json","w")
result_json = json.dumps(rd_teste_j)
f.write(result_json)
f.close()
#.
           
       