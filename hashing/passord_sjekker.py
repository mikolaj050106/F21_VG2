import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_saved_hash(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def verify_password(input_password, filename):
    saved_hash = get_saved_hash(filename)
    input_hash = hash_password(input_password)
    
    if input_hash == saved_hash:
        return True
    else:
        return False

user_password = input("SKriv inn passord: ")

file_name = "passord_hash.txt"

is_correct = verify_password(user_password, file_name)

if is_correct:
    print("Passord er korrekt!")
else:
    print("feil passord.")
