import json


# TODO mehre outputs hinzufügen um nicht das ganze geld einer anderen Person zu schicken
# Außerdem auch mehr

class Transaction(dict):  # to make it json serializable
    """
    args: amt, owner_pk, input_hash, output_hash, owner_sig
    """

    def __init__(self, amt, owner_pk, input_hash, output_hash, owner_sig):
        self.amt = amt
        self.owner_pk = owner_pk
        self.input_hash = input_hash
        self.output_hash = output_hash
        self.owner_sig = owner_sig
        dict.__init__(self, amt=self.amt, owner_pk=self.owner_pk,
                      input_hash=self.input_hash, output_hash=self.output_hash, owner_sig=self.owner_sig)

    @property
    def as_dict(self):
        return {
            "amt": self.amt,
            "owner_pk": self.owner_pk,
            "input_hash": self.input_hash,
            "output_hash": self.output_hash,
            "owner_sig": self.owner_sig,
        }
    # TODO sowie hier vielleciht überall json als string repräsentation

    def __str__(self):
        return json.dumps(self.as_dict)

    @property
    def hash(self):
        return hash(str(self))
