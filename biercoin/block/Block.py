import time
import json
from biercoin.util.functions import hash

mining_dificulty = 4
block_reward = 1


class Block:
    def __init__(self, transactions, prev_hash):
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = hash(self.json)

    def toDict(self):  # TODO Json
        """returns Dict of Values of Block"""
        return {
            "transactions": self.transactions,
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
        }

    def __str__(self):
        return self.json

    def __repr__(self):
        return self.json

    @property
    def json(self):
        return json.dumps(self.toDict())

    def mine(self):
        while not self.hash.startswith("0" * mining_dificulty):
            self.nonce += 1
            self.hash = hash(self.json)
        # print(self.nonce, self.hash)
        return self.toDict()
