import json 
import requests
from Class.Insertion import Insertion
from Class.Reading import Reading
from Class.Updation import Updation
from Class.Creation import Creation
from Class.Drop import Drop
def create():
    create=Creation('Covid19.db','covid19_info',Country={'pk':True,'type':'text','null':False},cases={'pk':False,'type':'integer','null':False},deaths={'pk':False,'type':'integer','null':False})
    create.sql_execute()

#https://od.cdc.gov.tw/eic/covid19/covid19map.json
def crawl(url):
    data_=[]
    req=requests.get(url)
    datas=json.loads(req.text)
 
    for data in datas['features']:
        data_list=(data['properties']['name'],data['properties']['cases'],data['properties']['deaths'])
        if data_list not in data_:
            data_.append(data_list)
    return data_

def insert(datas):
    insert = Insertion('Covid19.db','covid19_info',datas)
    insert.sql_execute()
def update(datas):
    update=Updation('Covid19.db','covid19_info',datas)
    update.sql_execute()
def read_all_row():
    read=Reading('Covid19.db','covid19_info')
    read.sql_execute()
    return read.read_datas

def search_country(country):
    read=Reading('Covid19.db','covid19_info',country)
    read.sql_execute()
    return read.read_datas
def refresh(sql_datas,web_datas):
    new_cases_or_deaths=[]
    new_datas=list(set(web_datas)-set(sql_datas))
    for old_data in sql_datas:
        for new_data in new_datas:
            if new_data[0]==old_data[0]:
                new_cases_or_deaths.append(new_data)
                break
    new_infected_country=list(set(new_datas)-set(new_cases_or_deaths))
    
    if len(new_datas) != 0:
        if len(new_infected_country) !=0:
            insert(new_infected_country)
        if len(new_cases_or_deaths) !=0:
            update(new_datas)
        return 'have new datas'
    
    return 'no new datas'
def generate_all(data_list,condition):
    value_list=[value[condition] for value in data_list]
    
    while 1:
        value_register=value_list[0:5]
        for five_value in value_register:
            yield five_value
        del value_list[0:5]
        for i in value_register:
            value_list.append(i)

def generate_one_country(country,condition):
    while 1:
        yield search_country(country)[0][condition]
def main():
    try:
        create()
        insert(crawl('https://od.cdc.gov.tw/eic/covid19/covid19map.json'))
    except:
        print(refresh(read_all_row(),crawl('https://od.cdc.gov.tw/eic/covid19/covid19map.json')))

main()
