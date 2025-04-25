# Phrase to BIP-39 Bitcoin Mnemonic Generator

This Python script takes a user-provided phrase, hashes it multiple times using SHA-256, and generates a valid 24-word Bitcoin mnemonic seed phrase using the BIP-39 standard. It also allows converting the mnemonic into a private key.

## Features
- Converts any input phrase into a secure 24-word Bitcoin mnemonic seed phrase.
- Hashes the input phrase multiple times (`number_of_hashes` times) for added security.
- Converts the mnemonic seed phrase into a private key.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IamJamesRooke/phrase-to-bip39-bitcoin-mnemonic-generator.git
   cd phrase-to-bip39-bitcoin-mnemonic-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python phrase_to_bip39_bitcoin_mnemonic.py
   ```

## Usage

1. Run the script:
   ```bash
   python phrase_to_bip39_bitcoin_mnemonic.py
   ```

2. Enter a phrase when prompted:
   ```
   Enter a phrase: Hello!
   ```

3. The script will output:
   - A 24-word Bitcoin mnemonic seed phrase.
   - Optionally, you can extend the script to generate a private key from the mnemonic.

## Example Output

```
Enter a phrase: Hello!

Generated 24-word Bitcoin mnemonic seed phrase:
------------------------------------------------------------
1. DISAGREE         9. RIOT             17. FIGURE
2. CIVIL            10. SPARE           18. FLAG
3. RELAX            11. PACT            19. WHISPER
4. JAGUAR           12. TRUST           20. VOLUME
5. SURVEY           13. FORK            21. ART
6. RULE             14. SHOULDER        22. HURT
7. WISE             15. ESSENCE         23. PROOF
8. PATCH            16. SESSION         24. MARGIN
```

## Configuration

- You can configure the number of SHA-256 hash iterations by modifying the `number_of_hashes` variable in the script:
  ```python
  number_of_hashes = 1000
  ```

## Dependencies
- Python 3.7 or higher
- `mnemonic` library

## License
This project is licensed under the MIT License.