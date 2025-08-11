// Version Information
const VERSION = "1.1.0";
const SCRIPT_NAME = "Phrase2BIP39 Bitcoin Seed Generator";
const NUMBER_OF_HASHES = 1000;

// Utility function to hash data multiple times
async function hashMultipleTimes(data, iterations) {
    let result = CryptoJS.enc.Utf8.parse(data);
    for (let i = 0; i < iterations; i++) {
        result = CryptoJS.SHA256(result);
    }
    return result;
}

// Convert WordArray to Uint8Array
function wordArrayToUint8Array(wordArray) {
    const words = wordArray.words;
    const sigBytes = wordArray.sigBytes;
    const u8 = new Uint8Array(sigBytes);
    for (let i = 0; i < sigBytes; i++) {
        u8[i] = (words[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
    }
    return u8;
}

// Convert Uint8Array to number (big endian) - matches Python's int.from_bytes
function uint8ArrayToNumber(uint8Array, offset, length) {
    let result = 0;
    for (let i = 0; i < length && offset + i < uint8Array.length; i++) {
        result = (result << 8) | uint8Array[offset + i];
    }
    // Ensure unsigned result (matches Python behavior)
    return result >>> 0;
}

// Generate duress passphrase
async function generateDuressPassphrase(phrase) {
    const duressHash = await hashMultipleTimes(phrase, 100);
    const duressBytes = wordArrayToUint8Array(duressHash);
    const wordIndex = uint8ArrayToNumber(duressBytes, 0, 4) % bip39.wordlists.english.length;
    return bip39.wordlists.english[wordIndex];
}

// Generate real wallet credentials
async function generateRealWalletCredentials(phrase) {
    const realHash = await hashMultipleTimes(phrase, 2000);
    const realBytes = wordArrayToUint8Array(realHash);
    
    const walletIndex = uint8ArrayToNumber(realBytes, 0, 4) % 100;
    const word1Index = uint8ArrayToNumber(realBytes, 4, 4) % bip39.wordlists.english.length;
    const word2Index = uint8ArrayToNumber(realBytes, 8, 4) % bip39.wordlists.english.length;
    const word3Index = uint8ArrayToNumber(realBytes, 12, 4) % bip39.wordlists.english.length;
    
    const word1 = bip39.wordlists.english[word1Index];
    const word2 = bip39.wordlists.english[word2Index];
    const word3 = bip39.wordlists.english[word3Index];
    
    return {
        walletIndex: walletIndex,
        passphrase: `${word1} ${word2} ${word3}`
    };
}

// Generate mnemonic from phrase
async function generateMnemonic(phrase) {
    const hash = await hashMultipleTimes(phrase, NUMBER_OF_HASHES);
    const hashBytes = wordArrayToUint8Array(hash);
    
    // Take first 32 bytes (256 bits) for 24-word mnemonic
    const entropy = hashBytes.slice(0, 32);
    const entropyHex = Array.from(entropy).map(b => b.toString(16).padStart(2, '0')).join('');
    
    if (entropyHex.length !== 64) {
        throw new Error(`Invalid entropy length: ${entropyHex.length}. Expected 64 hex characters.`);
    }
    
    return bip39.entropyToMnemonic(entropyHex);
}

// Main function to generate all wallet information
async function generateWallets() {
    const inputPhrase = document.getElementById('inputPhrase').value.trim();
    
    if (!inputPhrase) {
        alert('Please enter a memorable phrase first!');
        return;
    }

    try {
        // Check if libraries are loaded
        if (typeof bip39 === 'undefined' || typeof CryptoJS === 'undefined') {
            throw new Error('Required libraries not loaded');
        }
        
        // Generate all wallet components
        const mnemonic = await generateMnemonic(inputPhrase);
        const duressPassphrase = await generateDuressPassphrase(inputPhrase);
        const realWallet = await generateRealWalletCredentials(inputPhrase);
        
        // Display results
        displayResults(mnemonic, duressPassphrase, realWallet);
        
    } catch (error) {
        console.error('Error generating wallets:', error);
        alert(`Error generating wallets: ${error.message}`);
    }
}

// Display the generated wallet information
function displayResults(mnemonic, duressPassphrase, realWallet) {
    // Show results section
    document.getElementById('results').classList.remove('hidden');
    
    // Display mnemonic words in 3 columns (1-8, 9-16, 17-24)
    const words = mnemonic.toUpperCase().split(' ');
    const wordsGrid = document.getElementById('mnemonicWords');
    wordsGrid.innerHTML = '';
    
    // Create 3 columns
    for (let col = 0; col < 3; col++) {
        const columnDiv = document.createElement('div');
        columnDiv.className = 'word-column';
        
        // Add 8 words to each column
        for (let row = 0; row < 8; row++) {
            const wordIndex = col * 8 + row;
            if (wordIndex < words.length) {
                const wordDiv = document.createElement('div');
                wordDiv.className = 'word-item';
                wordDiv.textContent = `${wordIndex + 1}. ${words[wordIndex]}`;
                columnDiv.appendChild(wordDiv);
            }
        }
        
        wordsGrid.appendChild(columnDiv);
    }
    
    // Display wallet details
    const elements = ['duressPass', 'duressPassSave', 'realPass', 'realPassSave', 
                     'realAccount', 'realAccountSave', 'compromisePass', 'compromiseAccount'];
    
    elements.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            if (id.includes('duress')) {
                element.textContent = duressPassphrase;
            } else if (id.includes('Account')) {
                element.textContent = realWallet.walletIndex;
            } else {
                element.textContent = realWallet.passphrase;
            }
        }
    });
    
    // Scroll to results
    document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const inputPhrase = document.getElementById('inputPhrase');
    if (inputPhrase) {
        inputPhrase.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                generateWallets();
            }
        });
    }
});
