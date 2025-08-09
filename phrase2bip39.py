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

def generate_duress_passphrase(phrase: str) -> str:
    """
    Generate a deterministic duress wallet passphrase using a word from the BIP-39 word list.
    This passphrase is intentionally weak and discoverable via dictionary attack.
    
    Args:
        phrase (str): The original input phrase
        
    Returns:
        str: A word from the BIP-39 word list to use as duress wallet passphrase
    """
    # Get the BIP-39 word list
    mnemo = Mnemonic("english")
    word_list = mnemo.wordlist
    
    # Hash the phrase to get a deterministic seed for word selection
    # Use fewer hashes to make it different from main wallet generation
    duress_seed = phrase.encode('utf-8')
    for _ in range(100):  # Fewer hashes for duress seed
        duress_seed = hashlib.sha256(duress_seed).digest()
    
    # Select a word from the BIP-39 word list deterministically
    word_index = int.from_bytes(duress_seed[:4], byteorder='big') % len(word_list)
    duress_passphrase = word_list[word_index]
    
    return duress_passphrase

def generate_real_wallet_credentials(phrase: str):
    """
    Generate deterministic credentials for the real wallet with maximum security.
    
    Args:
        phrase (str): The original input phrase
        
    Returns:
        tuple: (wallet_index, three_word_passphrase)
    """
    # Get the BIP-39 word list
    mnemo = Mnemonic("english")
    word_list = mnemo.wordlist
    
    # Hash the phrase with a different iteration count for real wallet
    real_seed = phrase.encode('utf-8')
    for _ in range(2000):  # More hashes for real wallet (different from main and duress)
        real_seed = hashlib.sha256(real_seed).digest()
    
    # Generate deterministic wallet index (0-99 for convenience)
    wallet_index = int.from_bytes(real_seed[:4], byteorder='big') % 100
    
    # Generate three-word passphrase from BIP-39 word list
    word1_index = int.from_bytes(real_seed[4:8], byteorder='big') % len(word_list)
    word2_index = int.from_bytes(real_seed[8:12], byteorder='big') % len(word_list)
    word3_index = int.from_bytes(real_seed[12:16], byteorder='big') % len(word_list)
    
    word1 = word_list[word1_index]
    word2 = word_list[word2_index]
    word3 = word_list[word3_index]
    three_word_passphrase = f"{word1} {word2} {word3}"
    
    return wallet_index, three_word_passphrase

def phrase_to_duress_wallet(phrase: str):
    """
    Generate a duress wallet with the same mnemonic but a weak, discoverable passphrase.
    
    Args:
        phrase (str): The original input phrase
        
    Returns:
        tuple: (mnemonic_phrase, duress_passphrase, main_password)
    """
    # Generate the main mnemonic and password
    mnemonic_phrase, main_password = phrase_to_mnemonic_and_password(phrase)
    
    # Generate the duress passphrase
    duress_passphrase = generate_duress_passphrase(phrase)
    
    return mnemonic_phrase, duress_passphrase, main_password

def phrase_to_complete_wallet_system(phrase: str):
    """
    Generate the complete three-tier wallet system.
    
    Args:
        phrase (str): The original input phrase
        
    Returns:
        tuple: (mnemonic_phrase, duress_passphrase, main_password, real_wallet_index, real_wallet_passphrase)
    """
    # Generate the basic components
    mnemonic_phrase, duress_passphrase, main_password = phrase_to_duress_wallet(phrase)
    
    # Generate real wallet credentials
    real_wallet_index, real_wallet_passphrase = generate_real_wallet_credentials(phrase)
    
    return mnemonic_phrase, duress_passphrase, main_password, real_wallet_index, real_wallet_passphrase

if __name__ == "__main__":
    print("=" * 50)
    print("PASSPHRASE TO BITCOIN SEED GENERATOR")
    print("=" * 50)
    print()
    print("This tool converts any memorable phrase into Bitcoin")
    print("wallet seeds. The genius: ONE phrase generates")
    print("everything you need - no need to memorize multiple")
    print("passwords, seed phrases, or account numbers.")
    print()
    print("KEY CONCEPT: Same 24 words + different passphrases")
    print("= completely different wallets!")
    print()
    print("It creates 3 wallets with different security levels:")
    print()
    print("• Wallet 1: Same seed + NO passphrase")
    print("• Wallet 2: Same seed + 1-word passphrase")
    print("• Wallet 3: Same seed + 3-word passphrase + account")
    print()
    print("Why 3 wallets? Security through deception.")
    print("If anyone forces access, they find the first two")
    print("and think that's everything. The real wealth")
    print("stays hidden in wallet 3.")
    print()
    
    print("=" * 50)
    print("STEP 1: ENTER YOUR MEMORABLE PHRASE")
    print("=" * 50)
    print()
    print("Enter any phrase you can always remember:")
    print("Examples: 'my dog max loves treats'")
    print("         'pizza friday movie night'")
    print("         'coffee shop on main street'")
    print()
    print()
    input_phrase = input("Enter your memorable phrase: ")

    print("\nGenerating wallet information...")

    # Generate complete three-tier wallet system
    mnemonic_seed, duress_passphrase, main_password, real_wallet_index, real_wallet_passphrase = phrase_to_complete_wallet_system(input_phrase)

    print()
    print("=" * 50)
    print("STEP 2: WRITE DOWN 24 WORDS")
    print("=" * 50)
    print()
    print("These words control all wallets. Write on paper!")
    print()
    print("IMPORTANT: All 3 wallets use these SAME 24 words.")
    print("Only the passphrase changes to create different wallets.")
    print()

    # Format the mnemonic output
    words = mnemonic_seed.upper().split()
    for i in range(8):
        col1 = f"{i + 1}. {words[i]}"
        col2 = f"{i + 9}. {words[i + 8]}"
        col3 = f"{i + 17}. {words[i + 16]}"
        print(f"{col1:<16}{col2:<16}{col3:<16}")

    print()
    print("=" * 50)
    print("STEP 3: DOWNLOAD SPARROW WALLET")
    print("=" * 50)
    print()
    print("⚠️  WARNING: Only use the official site!")
    print("There are fake Sparrow sites that steal Bitcoin.")
    print()
    print("1. Go to: sparrowwallet.com (check spelling!)")
    print("2. Download and install")
    print("3. Open the program")
    print()
    print("This is free Bitcoin software for managing wallets.")
    print()

    print("=" * 50)
    print("STEP 4: CREATE WALLET #1 (BASIC)")
    print("=" * 50)
    print()
    print("This wallet uses the 24 words + NO passphrase.")
    print("Anyone with your phrase finds this first.")
    print()
    print("1. Sparrow: File > New Wallet")
    print("2. Name: 'Bitcoin Wallet'")
    print("3. Choose: New or Imported Software Wallet")
    print("4. Select: Use 24 Words")
    print("5. Import Existing Mnemonic")
    print("6. Type your 24 words from Step 2")
    print("7. Passphrase: LEAVE EMPTY")
    print("8. Create Wallet")
    print()
    print("This wallet shows your basic holdings.")
    print()

    print("=" * 50)
    print("STEP 5: CREATE WALLET #2 (DECOY)")
    print("=" * 50)
    print()
    print("This uses the SAME 24 words + 1-word passphrase.")
    print("Smart attackers find this by trying BIP-39 words.")
    print()
    print("1. Sparrow: File > New Wallet")
    print("2. Name: 'Savings'")
    print("3. Choose: New or Imported Software Wallet")
    print("4. Select: Use 24 Words")
    print("5. Import Existing Mnemonic")
    print("6. Type SAME 24 words from Step 2")
    print(f"7. Passphrase: {duress_passphrase}")
    print("8. Create Wallet")
    print()
    print("This wallet shows more substantial holdings.")
    print()

    print("=" * 50)
    print("STEP 5A: SAVE WALLET #2 DETAILS")
    print("=" * 50)
    print()
    print("Write this down (or run this program again):")
    print()
    print(f"Passphrase: {duress_passphrase}")
    print()
    print("This 1-word password is INTENTIONALLY weak.")
    print("Smart attackers can find it by trying all 2,048")
    print("BIP-39 words. That's the point - they find this")
    print("decoy wallet and think they're done!")
    print()

    print("=" * 50)
    print("STEP 7: CREATE WALLET #3 (MAIN VAULT)")
    print("=" * 50)
    print()
    print("This uses the SAME 24 words + 3-word passphrase")
    print("+ account number. Maximum security combination!")
    print()
    print("1. Sparrow: File > New Wallet")
    print("2. Name: 'Main'")
    print("3. Choose: New or Imported Software Wallet")
    print("4. Select: Use 24 Words")
    print("5. Import Existing Mnemonic")
    print("6. Type SAME 24 words from Step 2")
    print(f"7. Passphrase: {real_wallet_passphrase}")
    print("8. Advanced Options")
    print(f"9. Account: {real_wallet_index} (this creates a different wallet path)")
    print("10. Create Wallet")
    print()
    print("This wallet contains your main Bitcoin wealth.")
    print()
    
    print("=" * 50)
    print("STEP 8: SAVE WALLET #3 DETAILS")
    print("=" * 50)
    print()
    print("Write this down (or run this program again):")
    print()
    print(f"Passphrase: {real_wallet_passphrase}")
    print(f"Account: {real_wallet_index}")
    print()

    print("=" * 50)
    print("STEP 9: HOW TO USE WALLETS")
    print("=" * 50)
    print()
    print("SEND BITCOIN:")
    print("1. Open wallet > Send tab")
    print("2. Paste destination address")
    print("3. Enter amount")
    print("4. Create Transaction > Broadcast")
    print()
    print("RECEIVE BITCOIN:")
    print("1. Open wallet > Receive tab")
    print("2. Copy the address")
    print("3. Give address to sender")
    print()
    print("CHECK BALANCE:")
    print("• Balance shows on main screen")
    print("• Transactions take 10-60 minutes")
    print()

    print("=" * 50)
    print("STEP 10: IF COMPROMISED")
    print("=" * 50)
    print()
    print("IF SOMEONE FORCES ACCESS:")
    print("1. Give them ONLY your memorable phrase")
    print("2. They find Wallet #1 (basic)")
    print("3. Smart ones find Wallet #2 (duress)")
    print("4. They think that's everything and leave")
    print()
    print("NEVER TELL THEM:")
    print(f"• 3-word password: {real_wallet_passphrase}")
    print(f"• Account number: {real_wallet_index}")
    print("• That there's a 3rd wallet")
    print()
    print("⚠️  CRITICAL: They must never even SUSPECT")
    print("that Wallet #3 exists. Act like Wallet #2")
    print("is your main savings. Sell the performance!")
    print()
    print("Wallet #3 has 860+ BILLION password combinations")
    print("(8.6B passphrases × 100 accounts = 860B total).")
    print("They'll never find it without the exact details!")
    print()

    print("=" * 50)
    print("STEP 11: AFTER COMPROMISE")
    print("=" * 50)
    print()
    print("1. Move ALL Bitcoin to completely new wallets")
    print("2. Choose a new memorable phrase")
    print("3. Never use the old phrase again")
    print()
    print("Once anyone knows your phrase, assume everything")
    print("is compromised (even if they didn't find Wallet #3).")
    print()

    print("=" * 50)
    print("SECURITY REMINDERS")
    print("=" * 50)
    print()
    print("✅ DO:")
    print("• Keep 24 words written on paper in safe place")
    print("• Test with small amounts first")
    print("• Choose memorable but private phrases")
    print("• Run this program anytime to regenerate")
    print("• Practice the 'under duress' scenario")
    print("• Keep some funds in Wallets #1 and #2")
    print("• Act stressed when 'giving up' Wallet #2")
    print()
    print("❌ DON'T:")
    print("• Photo the 24 words")
    print("• Store 24 words digitally")
    print("• Try to memorize 3-word passwords")
    print("• Share your memorable phrase")
    print("• Keep all wallets empty (make decoys believable)")
    print("• Mention 'multiple wallets' to anyone")
    print("• Use obvious phrases others might guess")
    print()
    
    print("=" * 50)
    print("COMPLETE!")
    print("=" * 50)
    print()
    print("You now have deterministic access to 3 Bitcoin")
    print("wallets, all generated from your one memorable")
    print("phrase. Your phrase is your master key to")
    print("everything - keep it safe!")
    
    input("\nPress Enter to exit...")