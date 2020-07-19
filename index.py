
import csv
import json
import math
import requests
import re




def index_world():
    index_dict={}
    m_list=["$",",","[","]","#","(",")","\\","|",">","<"]
    
    table_list=['city','country','countrylanguage']
    for table in table_list:
        with open(table+'.json','r') as f:
            j=json.loads(f.read())
        for dic in j:
            for x in dic.items():
                key=x[0]
                value=x[1]
                if type(value)!=str:
                    try:
                        value=str(value)
                    except:
                        pass
                if type(value)==str:
                    value=value.lower()
                    for m in m_list:
                        if m in value:
                            value=value.replace(m,'')
                    if "-"or"/"or" " in value:
                        value=re.split(r'[-,/,\s]',value)
                        for e in value:
                            dic_e={'TABLE':table,'data':dic}
                            if index_dict.get(e)==None:                                             
                                index_dict[e]=[dic_e]
                            else:
                                index_dict[e].append(dic_e)
                    else:
                        dic_e={'TABLE':table,'data':dic}
                        if index_dict.get(value)==None:                                             
                            index_dict[value]=[dic_e]
                        else:
                            index_dict[value].append(dic_e)
                                                
    index_dict_1={}
    for x in index_dict.keys():
        x_1=re.sub(r'[^a-z0-9]','',x)      
        if index_dict_1.get(x_1)==None:                                             
            index_dict_1[x_1]=index_dict[x]
        else:
            index_dict_1[x_1].extend(index_dict[x])
    del index_dict_1['']
    
    return index_dict_1                      


def index_nba():
    index_dict={}
    m_list=["$",",","[","]","#","(",")","\\","|",">","<"]
    
    table_list=['joined_drafted_all_players_original','Player','Team','Game','Actions']
    for table in table_list:
        with open(table+'.json','r') as f:
            j=json.loads(f.read())
        for dic in j:
            for x in dic.items():
                key=x[0]
                value=x[1]
                if type(value)!=str:
                    try:
                        value=str(value)
                    except:
                        pass
                if type(value)==str:
                    value=value.lower()
                    for m in m_list:
                        if m in value:
                            value=value.replace(m,'')
                    if "-"or"/"or" " in value:
                        value=re.split(r'[-,/,\s]',value)
                        for e in value:
                            dic_e={'TABLE':table,'data':dic}
                            if index_dict.get(e)==None:                                             
                                index_dict[e]=[dic_e]
                            else:
                                index_dict[e].append(dic_e)
                    else:
                        dic_e={'TABLE':table,'data':dic}
                        if index_dict.get(value)==None:                                             
                            index_dict[value]=[dic_e]
                        else:
                            index_dict[value].append(dic_e)
                                                
    index_dict_1={}
    for x in index_dict.keys():
        x_1=re.sub(r'[^a-z0-9]','',x)      
        if index_dict_1.get(x_1)==None:                                             
            index_dict_1[x_1]=index_dict[x]
        else:
            index_dict_1[x_1].extend(index_dict[x])
    del index_dict_1['']
    
    return index_dict_1                      




def index_uw_std():
    index_dict={}
    m_list=["$",",","[","]","#","(",")","\\","|",">","<"]
    
    table_list=['course','person','advisedBy','taughtBy']
    for table in table_list:
        with open(table+'.json','r') as f:
            j=json.loads(f.read())
        for dic in j:
            for x in dic.items():
                key=x[0]
                value=x[1]
                if type(value)!=str:
                    try:
                        value=str(value)
                    except:
                        pass
                if type(value)==str:
                    value=value.lower()
                    for m in m_list:
                        if m in value:
                            value=value.replace(m,'')
                    if "-"or"/"or" " in value:
                        value=re.split(r'[-,/,\s]',value)
                        for e in value:
                            dic_e={'TABLE':table,'data':dic}
                            if index_dict.get(e)==None:                                             
                                index_dict[e]=[dic_e]
                            else:
                                index_dict[e].append(dic_e)
                    else:
                        dic_e={'TABLE':table,'data':dic}
                        if index_dict.get(value)==None:                                             
                            index_dict[value]=[dic_e]
                        else:
                            index_dict[value].append(dic_e)
                                                
    index_dict_1={}
    for x in index_dict.keys():
        x_1=re.sub(r'[^a-z0-9]','',x)      
        if index_dict_1.get(x_1)==None:                                             
            index_dict_1[x_1]=index_dict[x]
        else:
            index_dict_1[x_1].extend(index_dict[x])
    
    return index_dict_1                      

if __name__ == '__main__':
    world=index_world()
    js = json.dumps(world, indent=4, separators=(',', ':'))
    requests.put('https://inf551project-8d971.firebaseio.com/world/'+'index.json',js)

    nba=index_nba()
    js = json.dumps(nba, indent=4, separators=(',', ':'))
    requests.put('https://inf551project-8d971.firebaseio.com/nba/'+'index.json',js)

    uw_std=index_uw_std()
    js = json.dumps(uw_std, indent=4, separators=(',', ':'))
    requests.put('https://inf551project-8d971.firebaseio.com/uw_std/'+'index.json',js)





