import hashlib
# Overrides Python default hash function


def hash(thingToHash):
    return str(hashlib.sha224(str(thingToHash).encode()).hexdigest())
