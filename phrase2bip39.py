import hashlib
from mnemonic import Mnemonic
import string  # <-- Add this import

number_of_hashes = 1000

def phrase_to_mnemonic(phrase: str) -> str:
    # Step 1: Hash the input phrase using SHA-256 multiple times
    hashed = phrase.encode('utf-8')
    for _ in range(number_of_hashes):
        hashed = hashlib.sha256(hashed).digest()

    # Step 2: Use the final hash to generate a 24-word mnemonic seed phrase
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.to_mnemonic(hashed)

    return mnemonic_phrase

def mnemonic_to_private_key(mnemonic: str) -> str:
    # Step 1: Convert the mnemonic back to entropy
    mnemo = Mnemonic("english")
    entropy = mnemo.to_entropy(mnemonic)

    # Step 2: Hash the entropy several times times using SHA-256
    hashed = entropy
    for _ in range(number_of_hashes):
        hashed = hashlib.sha256(hashed).digest()

    # Step 3: Convert the final hash to a hexadecimal private key
    private_key = hashed.hex()
    return private_key

def phrase_to_mnemonic_and_password(phrase: str):
    # Step 1: Hash the input phrase using SHA-256 multiple times
    hashed = phrase.encode('utf-8')
    for _ in range(number_of_hashes):
        hashed = hashlib.sha256(hashed).digest()

    # Step 2: Use the final hash to generate a 24-word mnemonic seed phrase
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.to_mnemonic(hashed)

    # Step 3: Generate a deterministic 6-letter uppercase password from the hash
    alphabet = string.ascii_uppercase
    password = ""
    for i in range(6):
        idx = hashed[i] % len(alphabet)
        password += alphabet[idx]

    return mnemonic_phrase, password

if __name__ == "__main__":
    # Input phrase
    input_phrase = input("Enter a phrase: ")

    # Generate mnemonic seed phrase and password
    mnemonic_seed, password = phrase_to_mnemonic_and_password(input_phrase)

    # Format the mnemonic output
    words = mnemonic_seed.upper().split()
    print("\nGenerated 24-word Bitcoin mnemonic seed phrase:")
    print("-" * 60)
    for i in range(8):
        col1 = f"{i + 1}. {words[i]}"
        col2 = f"{i + 9}. {words[i + 8]}"
        col3 = f"{i + 17}. {words[i + 16]}"
        print(f"{col1:<20}{col2:<20}{col3:<20}")

    print("\nDeterministic 6-letter password:")
    print("-" * 60)
    print(password)
    
    input("\nPress Enter to exit...")
