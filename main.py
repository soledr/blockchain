from Chain import blockchain
from Block import block
import random



def main():
    chain = blockchain.Blockchain()
    prev_block = chain.chain[-1]
    previous_block_hash = prev_block._hash_header(prev_block.header())

    while True:
        new_block = block.Block(previous_block_hash, [str(random.random()), str(random.random())], 0)

        new_block.mine_block()
        chain.add_block(new_block)

        # print(new_block.block_data())

        prev_block = new_block
        previous_block_hash = prev_block._hash_header(prev_block.header())
        
        print(f'''

        {chain.chain}
        
        ''')

if __name__ == "__main__":
    main()