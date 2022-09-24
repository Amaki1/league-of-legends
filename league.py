#imports
from riotwatcher import LolWatcher

#initilize
def getApiKey():
    f= open('../ApiKeys/riotApiKey.txt','r')
    return f.read()


key_api = getApiKey()

watcher = LolWatcher(key_api)

platformRoutingValue = "EUW1"

summonerName = "amaaki"

summoner = watcher.summoner.by_name(platformRoutingValue,summonerName)

puuid = summoner['puuid']
print(puuid)

matchlists = watcher.match.matchlist_by_puuid(platformRoutingValue,puuid)

print(matchlists[0])

match = watcher.match.by_id(platformRoutingValue, matchlists[0])

print(len(match['metadata']['participants']))