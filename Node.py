# Todo
# - Transaktion
# - Hashbaum
# - GUI
# -
#
#
#
#
#
import time
import hashlib
from wallet import Wallet
mining_dificulty = 4
block_reward = 1

transactions = []


def hash(thingToHash):
    return str(hashlib.sha224(str(thingToHash).encode()).hexdigest())


# Coinbase
class Block:
    def __init__(self, transactions, prev_hash):
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = str(hashlib.sha224(
            str(self.toDict()).encode()).hexdigest())

    def toDict(self):
        """returns Dict of Values of Block"""
        return {
            "transactions": self.transactions,
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
        }

    def mine(self):
        while not self.hash.startswith("0" * mining_dificulty):
            self.nonce += 1
            self.hash = str(hashlib.sha224(
                str(self.toDict()).encode()).hexdigest())
        print(self.nonce, self.hash)
        return self.toDict()


class Chain:
    genisis_block = Block("genisis", "0").toDict()

    chain = [genisis_block]

    def append(self, block):
        if hash(block).startswith("0" * mining_dificulty):
            self.chain.append(block)


class Node:
    chain = Chain()

    wallet = Wallet()

    def start_mining(self):
        while True:
            transaction = input("Transaktion: ")
            block = Block(transaction, hash(self.chain.chain[-1]))
            block.mine()
            self.chain.append(block.toDict())
            print(self.chain.chain)


if __name__ == "__main___":
    # Trying Things
    node = Node()
    node.start_mining()
