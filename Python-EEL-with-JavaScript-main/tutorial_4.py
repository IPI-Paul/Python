import io
import eel
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import os
import base64

eel.init("html")
@eel.expose

def get_data(cname):
    url = 'https://covid-193.p.rapidapi.com/statistics'
    headers = {
        'x-rapidapi-host': 'covid-193.p.rapidapi.com',
        'x-rapidapi-key': '7d18fd6581msh81a4886d454a322p1e64c5jsn2c784c87b0cf'
        }
    try:
        response = requests.request('Get', url, headers=headers)
        data=response.text
        data=json.loads(data)
        print('Used web data for statistics report!')
    except:
        print('Will try local data for statistics report!')
        return get_local_data(cname)
    for i in range(len(data['response'])):
        x=data['response'][i]['country']
        if (x.lower() ==cname.lower()):
            total = data['response'][i]['cases']['total']
            active = data['response'][i]['cases']['active']
            recovered = data['response'][i]['cases']['recovered']
            critical = data['response'][i]['cases']['total']
            new = data['response'][i]['cases']['new']
            try:
                new=int(new.replace('+', ''))
            except:
                new = 0
            total_deaths = data['response'][i]['deaths']['total']
            try:
                new_deaths = data['response'][i]['deaths']['new']
                new_deaths = int(new_deaths.replace('+', ''))
            except:
                new_deaths = 0
            data = update_data(cname, total, active, recovered, critical, new, total_deaths, new_deaths)
            return data
    return 'Country not found!'

def get_local_data(cname):
    src = 'html/json/tutorial_4.json'
    response = open(src, 'r')
    data = response.read()
    response.close()
    data = data.replace("'", '"').replace('None', '0').replace(chr(10),',').replace('}]},','}]}')
    data = json.loads(data)
    for i in range(len(data['response'])):
        x = data['response'][i]['country']
        if (x.lower() == cname.lower()):
            total = data['response'][i]['cases'][0]['total']
            active = data['response'][i]['cases'][0]['active']
            recovered = data['response'][i]['cases'][0]['recovered']
            critical = data['response'][i]['cases'][0]['total']
            new = data['response'][i]['cases'][0]['new']
            try:
                new=int(new.replace('+', ''))
            except:
                new = 0
            total_deaths = data['response'][i]['deaths'][0]['total']
            try:
                new_deaths = data['response'][i]['deaths'][0]['new']
                new_deaths = int(new_deaths.replace('+', ''))
            except:
                new_deaths = 0
            data = update_data(cname, total, active, recovered, critical, new, total_deaths, new_deaths)
            return data
    return 'Country not found!'

def update_data(*args):
    cname, total, active, recovered, critical, new, total_deaths, new_deaths = args
    def commas(num):
        if (str(num).isnumeric()):
            return format(num, ',d')
        return num
    folder = os.path.dirname(os.path.abspath(__file__))
    data = {}
    data.update({len(data)+1:{'Total Cases':commas(total)}})
    data.update({len(data)+1:{'Active Cases':commas(active)}})
    data.update({len(data)+1:{'Recovered Cases':commas(recovered)}})
    data.update({len(data)+1:{'Critical Cases':commas(critical)}})
    data.update({len(data)+1:{'New Cases':commas(new)}})
    data.update({len(data)+1:{'Total Deaths':commas(total_deaths)}})
    data.update({len(data)+1:{'New Deaths':commas(new_deaths)}})
    columns = []
    values = []
    idx = []
    for i in data:
        columns += [list(data[i])[0]]
        values += [float((data[i][list(data[i])[0]]).replace(',',''))]
    #df = pd.DataFrame.from_dict(data, orient='index', columns=['ALL CATEGORIES'])
    df = pd.DataFrame(values, index = columns, columns=['ALL CATEGORIES'])
    fig = plt.figure(figsize=(15, 10))
    plt.style.use('dark_background')
    df['ALL CATEGORIES'].plot(kind='bar', color=['red', 'blue', 'yellow', 'orange', 'white', 'green', 'purple'], fontsize=40)
    plt.xlabel('ALL CATEGORIES', fontsize=40, color='red', fontweight='bold', labelpad=20.0)
    plt.grid(b=True, which='both', color='white', linestyle='-')
    plt.title('Live Data of Corona Virus For: ' + cname.upper(), color='blue', fontsize=80, pad=20)
    #plt.savefig(folder + '/html/images/' + cname + '.png', bbox_inches='tight')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    val = buf.getvalue()
    buf.close()
    data.update({len(data)+1:{'image':'data:image/png;base64,' + base64.b64encode(val).decode() }})
    return data

@eel.expose
def get_countries():
    url = 'https://covid-193.p.rapidapi.com/statistics'
    headers = {
        'x-rapidapi-host': 'covid-193.p.rapidapi.com',
        'x-rapidapi-key': '7d18fd6581msh81a4886d454a322p1e64c5jsn2c784c87b0cf'
        }
    try:
        response = requests.request('Get', url, headers=headers)
        data=response.text
        print('Used web data for Country List!')
    except:
        print('Will try local data for Country List!')
        src = 'html/json/tutorial_4.json'
        response = open(src, 'r')
        data = response.read()
        response.close()
        data = data.replace("'", '"').replace('None', '0').replace(chr(10),',').replace('}]},','}]}')
    data = json.loads(data)
    obj = []
    for i in range(len(data['response'])):
        obj += [data['response'][i]['country']]
    return sorted(obj)
    
eel.start("tutorial_4.html", size=(1024, 950))
