import time
from biercoin.util.functions import hash


class Block:
    def __init__(self, transactions, prev_hash):
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = str(hash(self.toDict()).encode())

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
            self.hash = str(hash(self.toDict()).encode())
            # TODO: lieber als json
        print(self.nonce, self.hash)
        return self.toDict()
