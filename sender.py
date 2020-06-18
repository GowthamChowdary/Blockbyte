from web3 import Web3
import hashlib
#hashing the file
file = "test.txt" 
BLOCK_SIZE = 65536 
file_hash = hashlib.sha256() 
with open(file, 'rb') as f: 
    fb = f.read(BLOCK_SIZE) 
    while len(fb) > 0: 
        file_hash.update(fb) 
        fb = f.read(BLOCK_SIZE) 
file_hashh=file_hash.hexdigest()
print(file_hashh)
file_hash_byte = str.encode(file_hashh)
url="httpprovider url"
web3=Web3(Web3.HTTPProvider(url))
account_1="0x8820191Fe960A41Ed0Ed1DbA494C869BDeA88305"
account_2="0x678fa825bfb3d43a229b1e9B5131EA612682Af14"
private_key="privatekey"
nonce=web3.eth.getTransactionCount(account_1)
tx={
	'nonce':nonce,
	'to':account_2,
	'value':web3.toWei(0.01,'ether'),
	'gas':2000000,
	'gasPrice':web3.toWei('50','gwei'),
	'data':b''+file_hash_byte
}
signed_tx=web3.eth.account.signTransaction(tx,private_key)
tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
hex_hash=(web3.toHex(tx_hash))
print(hex_hash)
