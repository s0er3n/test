import rsa


class Person:
    def __init__(self):
        (self.pubkey, self.privkey) = rsa.newkeys(512)


alice = Person()
bob = Person()

# Bob sendet alice Nachricht

nachricht = "hallo".encode("UTF-8")  # zu bytes

geheime_nachricht = rsa.encrypt(nachricht, alice.pubkey)


# Alice empfängt Nachricht

entschlüsselte_nachricht = rsa.decrypt(geheime_nachricht, alice.privkey)

print(entschlüsselte_nachricht.decode("utf-8"))

# Bob signiert Nachricht

nachricht = "Dies ist meine signierte Nachricht".encode()

signatur = rsa.sign(nachricht, bob.privkey, "SHA-1")

# Alice verifziert die Nachricht mit Bobs-Public-Key

verify = rsa.verify(nachricht+"asd"), signatur, bob.pubkey)

print(verify)
# Da kommt nciht true raus sondern die hash methode wenn es funktioniert ansonsten error


class Transaction:
    def __init__(self, owner_pk, input_hash, prev_owner_sig):
        self.owner_pk=owner_pk
        self.input_hash=input_hashs
        self.output_hash=output_hashs
        self.prev_owner_sig=prev_owner_sig
