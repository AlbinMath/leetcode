/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var beautifulSubstrings = function(s, k) {
    // 1. Find smallest M > 0 such that (M * M) % (4 * k) === 0
    const target = 4 * k;
    let m = 1;
    while ((m * m) % target !== 0) {
        m++;
    }

    const isVowel = (ch) => ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u';
    
    // Map tracks counts of (balance, index % m) pairs
    // Initial state at index -1: balance = 0, (-1 mod m) = m - 1
    const seen = new Map();
    const initialMod = (m - 1) % m;
    seen.set(`0,${initialMod}`, 1);

    let balance = 0;
    let count = 0;

    for (let i = 0; i < s.length; i++) {
        balance += isVowel(s[i]) ? 1 : -1;
        const mod = i % m;
        const key = `${balance},${mod}`;

        const prevCount = seen.get(key) || 0;
        count += prevCount;
        seen.set(key, prevCount + 1);
    }

    return count;
};
