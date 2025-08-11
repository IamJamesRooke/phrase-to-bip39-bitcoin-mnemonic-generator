# 🧡 Phrase2BIP39 Bitcoin Seed Generator

**Convert any memorable phrase into a 3-tier Bitcoin wallet system for maximum security.**

## 🎯 Overview

This tool transforms a single memorable phrase into three Bitcoin wallets with different security levels:

- **Wallet 1**: Basic (24 words + no passphrase)
- **Wallet 2**: Decoy (24 words + 1-word passphrase) 
- **Wallet 3**: Vault (24 words + 3-word passphrase + account number)

**Key Concept**: Same 24 words + different passphrases = completely different wallets!

## 🔐 Security Through Deception

If compromised, attackers find Wallets #1 and #2 and think that's everything. The real wealth stays hidden in Wallet #3 with **860+ billion possible combinations**.

## 🚀 Quick Start

### Web Version (Recommended)
1. Navigate to `web-version/` folder
2. Open `index.html` in any browser
3. Generate your 3-tier wallet system
4. Follow the step-by-step instructions

### Python Version (Advanced Users)
```bash
cd python-version
python phrase2bip39.py
```

### For WhatsApp/Telegram Sharing
1. Zip the `web-version/` folder
2. Share the zip file with your group
3. Recipients extract and open `index.html`
4. Works on any device - no installation needed!

## 📁 Project Structure

```
phrase2bip39/
├── web-version/        # Standalone web app for sharing
│   ├── index.html      # Modern web interface
│   ├── styles.css      # Bitcoin-themed styling  
│   ├── script.js       # Core wallet generation logic
│   ├── bip39-simple.js # Local BIP39 implementation
│   └── README.md       # Web version guide
├── python-version/     # Original Python implementation
│   ├── phrase2bip39.py
│   ├── build_exe.py
│   └── phrase2BIP39.exe
└── README.md           # This file
```

## 🎨 Features

### Web Version
- ✅ **Modern Bitcoin-themed UI** with gold/orange gradients
- ✅ **Mobile responsive** design for demonstrations  
- ✅ **3-column word layout** (1-8, 9-16, 17-24)
- ✅ **No external dependencies** - works offline
- ✅ **Identical cryptographic results** to Python version

### Python Version  
- ✅ **Command-line interface** with detailed instructions
- ✅ **Windows executable** generation via [PyInstaller](https://pyinstaller.org/)
- ✅ **Complete step-by-step guidance** for [Sparrow Wallet](https://sparrowwallet.com/)
- ✅ **Advanced security recommendations**

## 🔧 How It Works

1. **Input**: Any memorable phrase (e.g., "my dog loves treats")
2. **Processing**: 
   - [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hashing (1000 iterations for mnemonic)
   - [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) standard word selection
   - Deterministic wallet generation
3. **Output**: 
   - 24-word mnemonic seed
   - Duress passphrase (1 word, intentionally weak)
   - Real passphrase (3 words + account number)

## 🎯 Usage Examples

### For Bitcoin Groups/Demonstrations
Share the web version link for educational purposes. Works on any smartphone or tablet with no installation required, making it perfect for teaching Bitcoin security concepts at meetups and conferences.

### For Personal Use
Use the Python version for maximum security when generating wallets for actual storage. Generate on an air-gapped computer, write everything on paper, and never store the results digitally.

## 🛡️ Security Features

- **Deterministic**: Same phrase always generates same wallets
- **Cryptographically secure**: [SHA-256](https://en.wikipedia.org/wiki/SHA-2) + [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) standards
- **Plausible deniability**: Hidden wallet appears non-existent
- **Brute-force resistant**: 860+ billion combinations for Wallet #3

## ⚠️ Security Warnings

**Never** store your phrase digitally or photograph the 24 words. Write everything on paper and store securely in multiple locations. **Test with small amounts** first before committing significant funds. **Use hardware wallets** like [Coldcard](https://coldcard.com/) or [Trezor](https://trezor.io/) for large amounts.

## 🔄 Version Compatibility

Both Python and JavaScript versions produce **identical results**. The same input phrase generates the same 24-word mnemonic, duress passphrase, and real wallet credentials across both implementations.

## 📱 Mobile Deployment

The web version is perfect for mobile Bitcoin group demonstrations. Simply zip the `web-version/` folder and share via [WhatsApp](https://whatsapp.com/), [Telegram](https://telegram.org/), or any messaging platform. Recipients extract and open `index.html` - it works seamlessly on iOS, Android, and desktop without requiring any app installations.

## 🏗️ Development

### Requirements
- **Web**: Any modern browser with JavaScript
- **Python**: Python 3.6+ with [`mnemonic`](https://pypi.org/project/mnemonic/) library

### Building
```bash
# Python executable (Windows)
cd python-version
python build_exe.py
```

## 📄 License

MIT License - Use responsibly for educational purposes.

## ⚡ Quick Test

Try with phrase: `Hello world!`

Expected results:
- **Duress passphrase**: `crisp`
- **Real passphrase**: `promote double only` 
- **Account**: `80`

---

**🧡 Remember: Your phrase is your master key to everything. Keep it safe!**
