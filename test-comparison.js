// Quick test to verify both Python and JavaScript produce same results
// Test the mnemonic generation with a known phrase

async function testPhrase(phrase) {
    console.log(`Testing phrase: "${phrase}"`);
    
    try {
        // Generate using our functions (same logic as main script)
        const mnemonic = await generateMnemonic(phrase);
        const duressPassphrase = await generateDuressPassphrase(phrase);
        const realWallet = await generateRealWalletCredentials(phrase);
        
        console.log('JavaScript Results:');
        console.log('Mnemonic:', mnemonic);
        console.log('Duress passphrase:', duressPassphrase);
        console.log('Real passphrase:', realWallet.passphrase);
        console.log('Account:', realWallet.walletIndex);
        
        // Check specific words
        const words = mnemonic.split(' ');
        console.log('\nFirst few words:');
        for (let i = 0; i < 5; i++) {
            console.log(`${i+1}. ${words[i]}`);
        }
        
        console.log('\n=== Compare with Python output ===');
        
    } catch (error) {
        console.error('Error:', error);
    }
}

// Test with "Hello world!" which should give known results
async function runTest() {
    await testPhrase("Hello world!");
}

// Include our functions
// (This would include the same functions from script.js)
