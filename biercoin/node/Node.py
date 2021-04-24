# Todo
# - Transaktion
# - Hashbaum
import copy
import time
import json
from biercoin.transaction.Transaction import Transaction
from biercoin.wallet.Wallet import Wallet
from biercoin.chain.Chain import Chain
from biercoin.block.Block import Block
from biercoin.util.functions import hash
# from .util.functions import hash
mining_dificulty = 4
block_reward = 1

# TODO Später sollte das hier aus dem Netzwerk empfangen werden






class Node:
    chain = Chain()
    wallet = Wallet()
    # TODO macht vielleicht mehr sinn die funktion zum block hinzuzufügen

    # FIXME: Die FUNKTION wird nciht benutzt?
    @property
    def coinbase(self):
        return Transaction(1, "COINBASE", "COINBASE", {"n": self.wallet.pubkey.n, "e": self.wallet.pubkey.e}, "COINBASE")

    # TODO funktion um transaktionen auf zunehmen
    def get_transactions(self):
        return [self.coinbase].append(get_transactions())

    def start_mining(self):
        # transaction = input("Transaktion: ")

        block = Block(self.get_transactions(), hash(self.chain.chain[-1].json))

        block.mine()
        self.chain.append(block)
        print(self.wallet.find_unspent(self.chain.chain))
        # print(self.chain.chain)


if __name__ == "__main___":
    # Trying Things
    node = Node()
    node.start_mining()
