# Phrase2BIP39 Bitcoin Seed Generator v1.0.1

A deterministic Bitcoin wallet generator that creates a three-tier security system from a si## 📁 Files

### **Root Directory:**
- `phrase2bip39.html` - **Web version** - works on any device with browser
- `WEB-README.md` - Documentation for web version
- `README.md` - This main documentation
- `requirements.txt` - Python dependencies

### **Python Version (`python-version/` folder):**
- `phrase2bip39.py` - Original Python script with step-by-step wallet generation
- `phrase2BIP39.exe` - Pre-built Windows executable (no Python required)
- `build_exe.py` - Script to build your own executable with PyInstaller

## 🌟 **Which Version Should You Use?**

| Use Case | Recommended Version |
|----------|-------------------|
| **Mobile demos for Bitcoin groups** | 📱 **Web Version** |
| **Sharing with non-technical users** | 📱 **Web Version** |
| **Personal use on Windows** | 💻 **Python Executable** |
| **Development/Scripting** | 💻 **Python Script** |
| **Maximum compatibility** | 📱 **Web Version** |

**Both versions produce identical results** - same cryptographic security!rase. Uses the same 24-word seed with different passphrases to create completely different wallets for maximum security through deception.

## 🚀 Quick Start - Choose Your Version:

### 📱 **Web Version (Recommended for Mobile)**
**Perfect for demos and sharing with non-technical users!**
- ✅ **Single HTML file** - works on ANY device with a browser
- ✅ **No installation required** - just open and use
- ✅ **Mobile-optimized** - perfect for phone demonstrations
- ✅ **Share via email/link** - recipients just click and use

**How to use:** Open `phrase2bip39.html` in any browser

### 💻 **Python Version (For Developers)**
**Full-featured command-line version with Windows executable**
- ✅ **Python script** - for developers and scripting
- ✅ **Windows executable** - no Python installation needed
- ✅ **Build your own** - includes build script

**Location:** All Python files are in `python-version/` folder

## 🔑 Key Features

- **One Phrase, Multiple Wallets**: Generate 3 different Bitcoin wallets from one memorable phrase
- **Plausible Deniability**: Duress wallet system protects your main funds under coercion
- **Deterministic**: Same phrase always generates the same wallets - no randomness
- **BIP-39 Compliant**: Uses standard Bitcoin seed phrase format
- **Educational Interface**: Step-by-step instructions for non-technical users
- **Bitcoin Selling Guide**: Instructions for converting Bitcoin to fiat via P2P exchanges
- **Security Warnings**: ColdCard recommendations and keylogger protection advice

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

### 📱 **Web Version (Zero Setup)**
1. **Download or open `phrase2bip39.html`**
2. **That's it!** Works in any browser on any device

### 💻 **Python Version**
1. **Navigate to `python-version/` folder**
2. **Option A: Use the pre-built executable**
   - Run `phrase2BIP39.exe` (Windows only)
   - No Python installation required

3. **Option B: Run from Python source**
   - Install Python dependencies: `pip install -r requirements.txt`
   - Run: `python phrase2bip39.py`

4. **Option C: Build your own executable**
   ```bash
   python build_exe.py
   ```

## 💻 Usage

### 📱 **Web Version**
1. **Open `phrase2bip39.html`** in any browser (Chrome, Safari, Firefox, etc.)
2. **Enter your memorable phrase** in the input field
3. **Click "Generate Bitcoin Wallets"**
4. **Follow the step-by-step guide** that appears
5. **Perfect for mobile demos** - share the HTML file with anyone!

### 💻 **Python Version**
```bash
cd python-version/
python phrase2bip39.py
# Follow the interactive prompts
```

### 🎯 **Example Session**
1. Enter: `coffee shop on main street`
2. Get your 24-word seed phrase
3. Follow the 12-step guided process
4. Create your three Bitcoin wallets in Sparrow

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

- `phrase2bip39.py` - Main program with step-by-step wallet generation (v1.0)
- `phrase2BIP39.exe` - Pre-built executable (no Python required)
- `build_exe.py` - Script to build your own executable with PyInstaller
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## 🔧 Building Executable

To create your own standalone executable:

1. Install PyInstaller: `pip install pyinstaller`
2. Run the builder: `python build_exe.py`
3. Find your executable in the root folder: `phrase2BIP39.exe`

The build script automatically cleans up temporary files for a clean setup.

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