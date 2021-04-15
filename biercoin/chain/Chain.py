import json
from biercoin.util.functions import hash
from biercoin.block.Block import Block


mining_dificulty = 4


class Chain:
    genisis_block = Block("genisis", "0")

    chain = [genisis_block]

    def append(self, block):
        if hash(block.json).startswith("0" * mining_dificulty):
            self.chain.append(block)

    # TODO stimmmen hashes von transaktionen und blöcke überein
