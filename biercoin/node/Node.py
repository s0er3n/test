# Todo
# - Transaktion
# - Hashbaum

import time
from biercoin.transaction.Transaction import Transaction
from biercoin.wallet.Wallet import Wallet
from biercoin.chain.Chain import Chain
from biercoin.block.Block import Block
from biercoin.util.functions import hash
# from .util.functions import hash
mining_dificulty = 4
block_reward = 1

# TODO Später sollte das hier aus dem Netzwerk empfangen werden
transactions = []


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

        block = Block(self.get_transactions(), hash(self.chain.chain[-1].json))

        block.mine()
        self.chain.append(block)
        print(self.chain.chain)


if __name__ == "__main___":
    # Trying Things
    node = Node()
    node.start_mining()
