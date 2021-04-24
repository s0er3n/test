import rsa
from biercoin.transaction import Transaction


class Wallet:
    def __init__(self):
        (self.pubkey, self.privkey) = rsa.newkeys(512)

    # def make_transaction(self, reciever, inputs):
    #     return Transaction(self.pubkey, inputs, "OUTPUT",
    #                        rsa.sign(inputs.encode(), self.privkey, "SHA-1"))

    # TODO search blockchain for unspent transactions and add it to balance

    def find_unspent(self, chain):
        balance = 0
        for block in chain:
            # print(block.transactions)
            if block.transactions != "genisis":
                for transaction in block.transactions:
                    # print(transaction)
                    if transaction.output_hash["n"] == self.pubkey["n"] and transaction.output_hash["e"] == self.pubkey["e"]:
                        balance += transaction.amt
                    if not transaction.input_hash == "COINBASE" and transaction.input_hash["n"] == self.pubkey["n"] and transaction.input_hash["e"] == self.pubkey["e"]:
                        balance -= transaction.amt
        return balance

        # TODO Transaktion aussenden, damit Node sie zur Blockchain hinzufügen kann

    def send_out_transaction(self, output):
        t = Transaction(1, self.wallet.pubkey, "tobefilled",
                        output, "sign")  # FIXME: HASH and SIGN
        add_transaction(self.make_transaktion())

        # tests


# wallet = Wallet()

# transaction = wallet.make_transaction("tilman", "lol")
# print(rsa.verify("lol".encode(), transaction.owner_sig, wallet.pubkey))
