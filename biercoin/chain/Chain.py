from biercoin.util.functions import hash
from biercoin.block.Block import Block


class Chain:
    genisis_block = Block("genisis", "0").toDict()

    chain = [genisis_block]

    def append(self, block):
        if hash(block).startswith("0" * mining_dificulty):
            self.chain.append(block)

    # TODO stimmmen hashes von transaktionen und blöcke überein
