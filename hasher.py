import hashlib
file = "test.txt" 
BLOCK_SIZE = 65536 
file_hash = hashlib.sha256() 
with open(file, 'rb') as f: 
    fb = f.read(BLOCK_SIZE) 
    while len(fb) > 0: 
        file_hash.update(fb) 
        fb = f.read(BLOCK_SIZE) 
print (file_hash.hexdigest())