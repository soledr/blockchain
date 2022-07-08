from Block import block
import time
import random

class Blockchain:
    def __init__(self):
        self.mem_pool = []
        self.chain = []
        self.generate_genisis_block()

    def generate_genisis_block(self):
        blk = block.Block("", ["GENISIS"], 0)
        self.chain.append(blk)

    def add_block(self,block):
        return self.chain.append(block)



        