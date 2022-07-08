import hashlib
from logging import captureWarnings
from shutil import register_unpack_format

class MerkelTree:
    def __init__(self):
        pass

    def _hash_transaction(self, transaction):
        transaction = hashlib.sha256(transaction.encode())
        return transaction.hexdigest()

    ## transactions must be a list
    def merkel_hash(self, transactions):

        if type(transactions) != list: return "Transactions must be a list"

        if len(transactions) == 1: return transactions[0]

        blocks = []
        new_layer = []

        for transaction in transactions:
            blocks.append(transaction)

        if len(blocks) % 2 != 0:
            last_element = blocks[-1]
            blocks.append(last_element)

        while len(blocks) >=1:

            first_two = blocks[0:2]
            h1 = self._hash_transaction(first_two[0])
            h2 = self._hash_transaction(first_two[1])

            hashing = h1+h2

            combined_hash = self._hash_transaction(hashing)

            new_layer.append(combined_hash)
            blocks= blocks[2:]


        return self.merkel_hash(new_layer)

    # def test(self):
    #     t1 = "T1"
    #     t2 = "T2"
    #     t3 = "T3"
    #     t4 = "T4"

    #     t1_hash = self._hash_transaction(t1)
    #     t2_hash = self._hash_transaction(t2)
    #     t3_hash = self._hash_transaction(t3)
    #     t4_hash = self._hash_transaction(t4)

    #     hash_new1 = self._hash_transaction(t1_hash + t2_hash)
    #     # print(hash_new1)
    #     hash_new2 = self._hash_transaction(t3_hash + t4_hash)
    #     # print(hash_new2)

    #     final_hash = self._hash_transaction(hash_new1 + hash_new2)

    #     print(self._hash_transaction('87deb947b95198890b6bc5e01e8cab5c80411d171900ce6e8cdcc6a23b46864d' + 'f93397e2d5a43978d88b0e088bbe2e79a6f34526ab5a0415d5a2a694cda5638b'))

    #     return final_hash

# transactions = ["T1", "T2", "T3", "T4", "T5", "T6"]
# transactions2 = ["Tranactions"]

# m = MerkelTree()
# x = m.merkel_hash(transactions2)
# print(x)
# print(m.test())





