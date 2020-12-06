import requests
import argparse

parse=argparse.ArgumentParser()
parse.add_argument('-c','--country',action='store',dest='name',help='Country',required=True)
parse.add_argument('-d','--date',action='store',dest='date',help='date',required=True)
r=parse.parse_args()

url = "https://rapidapi.p.rapidapi.com/report/country/name"

querystring = {"date":r.date,"name":r.name}
#querystring = {"date":"2020-04-01","name":"Israel"}
headers = {
    'x-rapidapi-key': "d3cb8aa507msh0f3455a0c52c9bap17508bjsn4f549c7413ea",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


response=response.json()
country=response[0]["provinces"][0]["province"]
confirmed=response[0]["provinces"][0]["confirmed"]
recovered=response[0]["provinces"][0]["recovered"]
deaths=response[0]["provinces"][0]["deaths"]
active=response[0]["provinces"][0]["active"]
date=response[0]["date"]

#print(response[0]["provinces"][0]["province"])
#print(response[0]["provinces"][0]["confirmed"])
#print(response[0]["provinces"][0]["recovered"])
#print(response[0]["provinces"][0]["deaths"])
#print(response[0]["provinces"][0]["active"])
#print(response[0]["date"])


print("выбранная страна:"+" "+country+" ,"+"количество больных:"+" " +(str)(confirmed)+" ,"+ "количество выздоровевших:" +" "+(str)(recovered)+" ,"+  "количество умерших" +" "+str(deaths) +" ,"+ "число"
+" "+str(date))







#print(type(response))
#print(response.text)

