import hashlib
from mnemonic import Mnemonic

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

if __name__ == "__main__":
    # Input phrase
    input_phrase = input("Enter a phrase: ")

    # Generate mnemonic seed phrase
    mnemonic_seed = phrase_to_mnemonic(input_phrase)

    # Format the mnemonic output
    words = mnemonic_seed.upper().split()
    print("\nGenerated 24-word Bitcoin mnemonic seed phrase:")
    print("-" * 60)
    for i in range(8):
        col1 = f"{i + 1}. {words[i]}"
        col2 = f"{i + 9}. {words[i + 8]}"
        col3 = f"{i + 17}. {words[i + 16]}"
        print(f"{col1:<20}{col2:<20}{col3:<20}")