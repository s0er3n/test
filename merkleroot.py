
class Merkle_Root:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def make_Hash(self):
        return hash((self.left, self.right))


tree = Merkle_Root()

tree.data = "transaktion"


tree2 = Merkle_Root()

tree2.data = "transaktion2"


parent = Merkle_Root()

parent.left = tree

parent.right = tree2

parent.data = parent.make_Hash()


print(parent.data)
