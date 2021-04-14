
class Transaction:
    def __init__(self, owner_pk, input_hash, output_hash, owner_sig):
        self.owner_pk = owner_pk
        self.input_hash = input_hash
        self.output_hash = output_hash
        self.owner_sig = owner_sig
        
