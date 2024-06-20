from pprint import pprint
from json import *
import requests
import json

token = {'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjU3MjZiODRjLTg4YTItNGNmZi05MjlhLWRiYTczNTM1OTVhNSIsImlhdCI6MTcxODMwMDMyNCwic3ViIjoiZGV2ZWxvcGVyLzU4YzljM2NhLTY5NDctOWVmOC1mMzQzLTE1NmMzNjk5ZmEyMSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTQzLjE3Ny40Mi4yMzgiXSwidHlwZSI6ImNsaWVudCJ9XX0.6dsmsnk_-sSW9viANrDYaqD-8lZcrxoBHayYXHWoZxoXDCuZ2mTKnxlvL4qrfgPP1we04CRvf5vwx8c3mjlmMw"}


class Engine():

    def PlayerLookup(tag=""):

        player = requests.get(f"https://api.brawlstars.com/v1/players/%23{tag.upper()}", headers=token)
        p_data = player.json()
        player = {"name": p_data["name"],
                  "3v3 Wins": p_data["3vs3Victories"],
                  "Solo wins": p_data["soloVictories"],
                  "Duo Wins": p_data["duoVictories"]}
        return player
    #PlayerLookup("2RRQRQ8G")



    def BrawlerLookup(query=''):
        if query == "":
            print("Getting availabe brawlers..")
            brawler = requests.get("https://api.brawlstars.com/v1/brawlers", headers=token)
            data = brawler.json()
            return data
        else:
            brawler = requests.get("https://api.brawlstars.com/v1/brawlers", headers=token)
            data = brawler.json()
            for x in range (0, len(data['items'])):
                #print(data['items'][x]['name'])
                if query.upper() == data['items'][x]['name']:
                    return data['items'][x]
                else:
                    continue


    def rankingLookup(country="GLOBAL"):
        if country != "GLOBAL" and len(country) >= 3:
            print("Invalid Country Code")
            exit()
        if country == "GLOBAL" or country=="":
            g_rankings = requests.get("https://api.brawlstars.com/v1/rankings/GLOBAL/players", headers=token)
            rankings = g_rankings.json()
            return rankings
        else:
            ranking_land = requests.get(f"https://api.brawlstars.com/v1/rankings/{country.upper()}/players", headers=token)  
            rank_land = ranking_land.json()
            return rank_land

