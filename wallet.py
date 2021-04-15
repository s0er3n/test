import rsa
# from Transaction import Transaction


class Wallet:
    def __init__(self):
        (self.pubkey, self.privkey) = rsa.newkeys(512)

    # def make_transaction(self, reciever, inputs):
    #     return Transaction(self.pubkey, inputs, "OUTPUT",
    #                        rsa.sign(inputs.encode(), self.privkey, "SHA-1"))

    # TODO search blockchain for unspent transactions and add it to balance

    def find_unspent(self):

        # TODO Transaktion aussenden, damit Node sie zur Blockchain hinzufügen kann

    def send_out_transaction(self):
        pass
        # main.transaction.append(self.make_transaktion())

        # tests


# wallet = Wallet()

# transaction = wallet.make_transaction("tilman", "lol")
# print(rsa.verify("lol".encode(), transaction.owner_sig, wallet.pubkey))
