var maxFreqSum = function(s) {
    let freq = Array(26).fill(0);

    // Count frequency of each character
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    let maxVowel = 0;
    let maxConsonant = 0;

    const vowels = "aeiou";

    // Find maximum vowel and consonant frequencies
    for (let i = 0; i < 26; i++) {
        let ch = String.fromCharCode(i + 97);

        if (vowels.includes(ch)) {
            maxVowel = Math.max(maxVowel, freq[i]);
        } else {
            maxConsonant = Math.max(maxConsonant, freq[i]);
        }
    }

    return maxVowel + maxConsonant;
};
