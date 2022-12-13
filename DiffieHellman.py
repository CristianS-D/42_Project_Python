import random
p = 3
g = 100

class EndUser:
    def __init__(self, name, private_key=None, public_key=int, shared_secret=int):
        self.name = name
        self.private_key = private_key if private_key else random.randrange(p,g)
        self.public_key = public_key
        self.shared_secret = shared_secret

    # Preforms the diffie hellman oporation to get public key
    def dhAlgorithm_publicKey(self):
        self.public_key = p**self.private_key%g
        print(f"{self.name} Public Key: {self.public_key}")

    # Preforms the diffie hellman oporation to get public key
    def dhAlgorithm_sharedKey(self,shared_key):
        self.shared_secret = shared_key**self.private_key%g
        print(f"{self.name} Shared Key: {self.shared_secret}")

#creat users with
alice = EndUser("Alice")
bob = EndUser('Bob')

#display private key
print(f"{alice.name} Private Key: {alice.private_key}")
print(f"{bob.name} Private Key: {bob.private_key}")

# create individual public keys
alice.dhAlgorithm_publicKey()
bob.dhAlgorithm_publicKey()

# Create shared secret key
bob.dhAlgorithm_sharedKey(alice.public_key)
bob.dhAlgorithm_sharedKey(alice.public_key)

def network():
    None