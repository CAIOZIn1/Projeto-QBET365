import requests
import json


bets =  requests.get('https://betsapi.com/docs/samples/bet365_inplay.json')
bets = bets.json()
#print(bets)

od = bets['results'][0][86]

print(od)
