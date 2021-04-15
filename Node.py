# Todo
# - Transaktion
# - Hashbaum

import time
import hashlib
from wallet import Wallet
from Transaction import Transaction

mining_dificulty = 4
block_reward = 1

transactions = []

# TODO überall diese hashfunktion benutzen
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

    def toDict(self):  # TODO Json
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
                str(self.toDict()).encode()).hexdigest())  # TODO: lieber als json
        print(self.nonce, self.hash)
        return self.toDict()


class Chain:
    genisis_block = Block("genisis", "0").toDict()

    chain = [genisis_block]

    def append(self, block):
        if hash(block).startswith("0" * mining_dificulty):
            self.chain.append(block)

    # TODO stimmmen hashes von transaktionen und blöcke überein


class Node:
    chain = Chain()

    wallet = Wallet()
    # TODO macht vielleicht mehr sinn die funktion zum block hinzuzufügen
    @property
    def coinbase(self):
        return str(Transaction(0.01, "COINBASE", "COINBASE", self.wallet.pubkey, "COINBASE"))

    # TODO funktion um transaktionen auf zunehmen
    def get_transactions(self):
        return [self.coinbase]

    def start_mining(self):
        # transaction = input("Transaktion: ")

        block = Block(self.get_transactions(), hash(self.chain.chain[-1]))
        block.mine()
        self.chain.append(block.toDict())
        print(self.chain.chain)


if __name__ == "__main___":
    # Trying Things
    node = Node()
    node.start_mining()
