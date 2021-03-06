from web3 import Web3
import json
import hashlib
url="httpprovider"
web3=Web3(Web3.HTTPProvider(url))
tx=web3.eth.getTransaction('transaction')
#print(tx)
def toDict(dictToParse):
    # convert any 'AttributeDict' type found to 'dict'
    parsedDict = dict(dictToParse)
    for key, val in parsedDict.items():
        # check for nested dict structures to iterate through
        if  'dict' in str(type(val)).lower():
            parsedDict[key] = toDict(val)
        # convert 'HexBytes' type to 'str'
        elif 'HexBytes' in str(type(val)):
            parsedDict[key] = val.hex()
    return parsedDict
dict_tx=toDict(tx)
data=dict_tx["input"]
file_hash=data[2:]
final_hash=bytes.fromhex(file_hash).decode('utf-8')
print("file hash received form blockchain is :"+final_hash)
file = "test.txt" 
BLOCK_SIZE = 65536 
file_hash = hashlib.sha256() 
with open(file, 'rb') as f: 
    fb = f.read(BLOCK_SIZE) 
    while len(fb) > 0: 
        file_hash.update(fb) 
        fb = f.read(BLOCK_SIZE) 
local_file_hash=file_hash.hexdigest()
print(local_file_hash)
if str(local_file_hash)==str(final_hash):
	print("THE FILE IS VERIFIED ON BLOCKCHAIN")
else:
	print("FILE ISN'T VERIFIED!!")	

