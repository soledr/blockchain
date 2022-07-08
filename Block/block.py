import hashlib
from datetime import datetime
from Block import merkelTree
import json
import time

class Block:

    # Intitalize information for a block
    def __init__(self, previous_block_hash,transactions, nonce) -> None:
        self.version = 1.0 ## Version of protocol
        self.previous_block_hash = previous_block_hash ## Hash of previous block header
        self.merkle_root = merkelTree.MerkelTree().merkel_hash(transactions) ## Calculates merkel root of transactions
        self.timestamp = datetime.timestamp(datetime.now()) ## Timestamp of block
        self.difficulty_target = "0" ## Target difficulty *in this case the hash must start with 2 0's*
        self.transactions = transactions ## Transactions 
        self.nonce = nonce ## Nonce

    
    def header(self):
        header = {
            "version": self.version,
            "previous_block_hash": self.previous_block_hash,
            "merkle_root": self.merkle_root,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }

        return header
    
    def _hash_header(self, header):
        header = json.dumps(str(header))
        header = hashlib.sha256(header.encode())
        return header.hexdigest()
    
    def mine_block(self):
        while True:
            new_block = Block(self.previous_block_hash, self.transactions, self.nonce)
            print(new_block._hash_header(new_block.header()))
            if new_block._hash_header(new_block.header()).startswith(self.difficulty_target):
                print("New Block")
                break
            else :
                self.nonce += 1
            
            time.sleep(.1)
    
    def block_data(self):
        header = str(self.header())
        body = str(self.transactions)
        data = {
            header: header,
            body: body
        }

        return str(data)




            



# b1 = Block("0", ['T1', 'T2', 'T3', 'T4'], 1)
# print(b1.timestamp)

# print(b1.header())
# print(b1.calculate_merkel_root())

# print(4 % 2)
# print(5 % 2)
# print(6 % 2)

# x = hashlib.sha256("Hello World".encode())
# result = x.hexdigest()
# print(result)




