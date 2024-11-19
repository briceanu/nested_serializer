import requests
import sys



# save a van
def create():

    url = 'http://127.0.0.1:8000/trucks/create'


    data= {
        'brand':'Daf',
        'weight':34,
        'fuel_consumption_per_day':30 ,
        'distance':324,
        'color':'blue',
        'fuel_type':'diesel'


    }

   

    res = requests.get(url=url,data=data)


    print(res.status_code)
    print(res.url)
    print(res.text)

 
 


def create_owner():

    url = 'http://127.0.0.1:8000/trucks/create_owner'


    data= {
        'age':43,
        'email':'ion@gmail.com',
        'address':'Birmingham' ,
        'truck':'3cee0e80-558f-48ec-8756-6f92c518d864',
   


    }

    res = requests.get(url=url,data=data)


    print(res.status_code)
    print(res.url)
    print(res.text)














if __name__ == '__main__':

    if sys.argv[1] == 'create':
        create()
    if sys.argv[1] == 'create_owner':
        create_owner()
    else: 
        exit()













# {"truck_id":"0b17d8c3-c4c4-44bb-8705-565c8f16c853","fuel_consumption":30.27,"brand":"Mercedes","weight":"58.00","fuel_consumption_per_day":"89.00","distance":294.0,"color":"black","fuel_type":"diesel"}
# {"truck_id":"79ca6d3b-928e-45c3-a02d-49bf46af2f41","fuel_consumption":31.45,"brand":"Scania","weight":"28.00","fuel_consumption_per_day":"39.00","distance":124.0,"color":"red","fuel_type":"lpg_gas"}
# {"truck_id":"3cee0e80-558f-48ec-8756-6f92c518d864","fuel_consumption":9.26,"brand":"Daf","weight":"34.00","fuel_consumption_per_day":"30.00","distance":324.0,"color":"blue","fuel_type":"diesel"}