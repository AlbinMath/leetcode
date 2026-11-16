/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var beautifulSubstrings = function(s, k) {
    const n = s.length;
    const isVowel = (ch) => ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u';
    let count = 0;

    for (let i = 0; i < n; i++) {
        let vowels = 0;
        let consonants = 0;

        for (let j = i; j < n; j++) {
            if (isVowel(s[j])) {
                vowels++;
            } else {
                consonants++;
            }

            if (vowels === consonants && (vowels * consonants) % k === 0) {
                count++;
            }
        }
    }

    return count;
};
