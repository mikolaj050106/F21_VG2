import hashlib

passord = input("SKriv inn passordet du vil bruke: ")

hash_objekt = hashlib.sha256(passord.encode())
hash_hex = hash_objekt.hexdigest()

with open("passord_hash.txt", "w") as fil:
    fil.write(hash_hex)
