import requests
import json
import base64
from Crypto.Util.number import *
url='http://seed1.neo.org:10332'
# url='http://127.0.0.1:10332/'

mapping_name={'NeoSPCC': '03d9e8b16bd9b22d3345d6d4cde31be1c3e1d161532e3d0ccecb95ece2eb58336e', 'NF1': '03b209fd4f53a7170ea4444e0cb0a6bb6a53c2bd016926989cf85f9b0fba17a70c', 'NF7': '02486fd15702c4490a26703112a5cc1d0923fd697a33406bd5a1c00e0013b09a70', 'NF3': '03b8d9d5771d8f513aa0869b9cc8d50986403b78c6da36890638c3d46a5adce04a', 'NF4': '02ca0e27697b9c248f6f16e085fd0061e26f44da85b58ee835c110caa5ec3ba554', 'NF6': '02aaec38470f6aad0042c6e877cfd8087d2676b0f516fddd362801b9bd3936399e', 'The Neo Order': '0239a37436652f41b3b802ca44cbcb7d65d3aa0b88c9a0380243bdbe1aaa5cb35b', 'NF2': '02df48f60e8f3e01c48ff40b9b7f1310d7a8b2a193188befe1c2e3df740e895093', 'NGD1': '0353f7aff015d3d204eecd508f4aa67f447df4d15ec4ba649f4fa91bdb7a78a354', 'NGD2': '022f1beae94cf0d266d7d26691b431958c8d13768103ab20aed817b57568da293f', 'lazynode': '0389ba00856f58bdc2b7c3fd6c2e73ed4829252f38083c1e295574ca599e93fe82', 'COZ': '02946248f71bdf14933e6735da9867e81cc9eea0b5895329aa7f71e7745cf40659', 'Everstake': '035d574cc6a904e82dfd82d7f6fc9c2ca042d4410a4910ecc8c07a07db49dc6513', 'chainnode': '02e4e0db9314a42bebcb7e348a7e1ab8d4a87f518371485b0d66dbc0368f8cf58d', 'Switcheo Labs': '0392fbd1d809a3c62f7dcde8f25454a1570830a21e4b014b3f362a79baf413e115', 'Flamingo': '03a3aba8edacd820f0b6c55f0bad25b733af00694c8194c04b71ce628c197fbe98', 'AxLabs (neow3j)': '02ec143f00b88524caf36a0121c2de09eef0519ddbe1c710a00f0e2663201ee4c0', 'Neo News Today': '0248a37e04c7a5fb9fdc9f0323b2955a94cbb2296d2ad1feacea24ec774a87c4a4', 'NEXT（NeoLine）': '02237309a0633ff930d51856db01d17c829a5b2e5cc2638e9c03b4cfa8e9c9f971', 'Nash.io': '03fd04de983f4e04c9629ab3cfc83f41be7431b96bf852a91873c38ca8f737ee2c', 'InfStones': '02cc10d0e929ca752cfd3408bedda06463e2d93fd435e4c2b86a895b3792dee4c8'}
data="""{
    "jsonrpc": "2.0",
    "method": "invokefunction",
    "params":["0xef4073a0f2b305a38ec4050e4d3d28bc40ea63f5","getCandidates"],
    "id":"1"
}
""" 
response = requests.post(url=url,data=str(data))
dict={}
for i in json.loads(response.text)['result']['stack'][0]['value']:
    dict[hex(bytes_to_long(base64.b64decode((i['value'][0]['value'].encode()))))[2:].rjust(66,'0')]=i['value'][1]['value']

vote={} # key(name) => [public key, getvoted]

for i in mapping_name:
    vote[i]=[mapping_name.get(i),dict[mapping_name.get(i)]]



burneo={'Neo News Today': '0x38844e806adb7a4ec6d396fbabe908361c600e87', 'COZ': '0x6c1a002394d57fa48349e12f83cca95b5c1c5f01', 'InfStones': '0x64a93c07145d3361a5299c63d32795ebc687d82b', 'chainnode': '0xf1656deda84d1a3db210898d28a5b3bf3e525031', 'Everstake': '0x7fb4e2ee78537d1629c904f0f929303da5fe83e2', 'Nash.io': '0x837e1e5e4133cd9fb1ea47afe5ec699aed60b86a'}

_burneo={} # key(name) => [smartcontract, voted]
for i in burneo:
    _url=url+'?jsonrpc=2.0&method=getnep17balances&id=1&params=[\"'+burneo[i]+'\"]'
    response = requests.get(url=_url)
    # print(response.text)
    for j in json.loads(response.text)['result']['balance']:
        if j['assethash']=='0xef4073a0f2b305a38ec4050e4d3d28bc40ea63f5':
            _burneo[i]=[burneo[i],j['amount']]

_vote=vote.copy()  
for i in _burneo:
    _vote.pop(i)

min=int(_vote['NeoSPCC'][1],10)
for i in _vote.values():
    _min=int(i[1],10)
    if _min<min :
        min=_min
min_burneo=int(_burneo['Neo News Today'][1],10)/int(vote['Neo News Today'][1],10)
name_burneo='Neo News Today'
for i in _burneo:
    _min=int(_burneo.get(i)[1],10)/int(vote.get(i)[1],10)
    # print(_min)
    if _min<min_burneo :
        min_burneo=_min
        name_burneo=i
# print(min)
# print(min_burneo)
# print(name_burneo)
# print(_burneo[name_burneo][1])
print(min+int(_burneo[name_burneo][1],10)-int(vote[name_burneo][1],10))