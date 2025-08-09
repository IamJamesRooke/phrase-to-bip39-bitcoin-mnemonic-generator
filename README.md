# Passphrase to Bitcoin Seed Generator

A deterministic Bitcoin wallet generator that creates a three-tier security system from a single memorable phrase. Uses the same 24-word seed with different passphrases to create completely different wallets for maximum security through deception.

## 🔑 Key Features

- **One Phrase, Multiple Wallets**: Generate 3 different Bitcoin wallets from one memorable phrase
- **Plausible Deniability**: Duress wallet system protects your main funds under coercion
- **Deterministic**: Same phrase always generates the same wallets - no randomness
- **BIP-39 Compliant**: Uses standard Bitcoin seed phrase format
- **Educational Interface**: Step-by-step instructions for non-technical users

## 🛡️ Security Model

The system creates three wallets with escalating security:

1. **Wallet #1 (Basic)**: Same seed + NO passphrase
   - Found immediately by anyone with your phrase
   - Keep small amounts for believability

2. **Wallet #2 (Decoy)**: Same seed + 1-word passphrase  
   - Found by smart attackers (2,048 combinations)
   - Keep moderate funds - your "main savings" performance

3. **Wallet #3 (Main Vault)**: Same seed + 3-word passphrase + account number
   - 860+ billion combinations (virtually impossible to find)
   - Your actual Bitcoin wealth stays hidden

## 📋 Requirements

- Python 3.6 or higher
- `mnemonic` library for BIP-39 functionality

## 🚀 Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/IamJamesRooke/phrase-to-bip39-bitcoin-mnemonic-generator.git
   cd phrase-to-bip39-bitcoin-mnemonic-generator
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install mnemonic
   ```

3. **Download Sparrow Wallet** (recommended Bitcoin wallet software)
   - Go to: [sparrowwallet.com](https://sparrowwallet.com) ⚠️ **Check spelling - avoid fake sites!**
   - Download and install for your operating system

## 💻 Usage

### Basic Usage
```bash
python phrase2bip39.py "your memorable phrase here"
```

### Interactive Mode
```bash
python phrase2bip39.py
# Follow the prompts to enter your phrase
```

### Example
```bash
python phrase2bip39.py "coffee shop on main street"
```

## 📖 How It Works

1. **Enter your memorable phrase** - something you'll never forget
2. **Get 24-word seed** - generated deterministically from your phrase
3. **Create 3 wallets** in Sparrow using the SAME 24 words but different passphrases:
   - Wallet 1: No passphrase
   - Wallet 2: Generated 1-word passphrase
   - Wallet 3: Generated 3-word passphrase + account number

## 🔒 Security Best Practices

### ✅ DO:
- Keep 24 words written on paper in safe place
- Test with small amounts first
- Choose memorable but private phrases
- Practice the 'under duress' scenario
- Keep some funds in Wallets #1 and #2 (make decoys believable)
- Act stressed when 'giving up' Wallet #2

### ❌ DON'T:
- Photo the 24 words
- Store 24 words digitally
- Try to memorize 3-word passwords
- Share your memorable phrase
- Keep all wallets empty
- Mention 'multiple wallets' to anyone
- Use obvious phrases others might guess

## ⚠️ Important Security Notes

- **Under duress**: Give ONLY your memorable phrase. They'll find Wallets #1 and #2.
- **Never reveal**: The 3-word passphrase, account number, or that Wallet #3 exists.
- **After compromise**: Move ALL funds to new wallets with a new phrase.
- **Sparrow warning**: Only use the official sparrowwallet.com site - fake sites steal Bitcoin!

## 🛠️ Technical Details

- **Hashing**: SHA-256 with different iteration counts for each wallet type
- **Word List**: Standard BIP-39 English wordlist (2,048 words)
- **Combinations**:
  - Wallet 2: 2,048 combinations (intentionally weak)
  - Wallet 3: 860+ billion combinations (8.6B passphrases × 100 accounts)

## 📁 Files

- `phrase2bip39.py` - Main program with step-by-step wallet generation
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## 🤝 Use Cases

- **Emergency recovery**: Give instructions to family/partners for Bitcoin access
- **Inheritance planning**: Simple phrase-based access to funds
- **Security through deception**: Protect wealth from coercion/theft
- **Simplified backup**: One phrase instead of multiple complex passwords

## ⚖️ Legal & Responsibility

This tool is for educational and personal security purposes. Users are responsible for:
- Keeping their memorable phrases secure
- Understanding Bitcoin wallet security
- Complying with local laws regarding cryptocurrency
- Testing with small amounts before storing significant funds

## 🆘 Support

If you need help:
1. Check this README for common issues
2. Ensure Python and dependencies are properly installed
3. Verify you're using the correct Sparrow Wallet website
4. Test with small amounts first

---

**Remember**: Your memorable phrase is your master key to everything. Choose wisely and keep it safe!