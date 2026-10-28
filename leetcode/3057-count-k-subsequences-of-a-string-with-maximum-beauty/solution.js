var countKSubsequencesWithMaxBeauty = function(s, k) {
    const MOD = 1000000007n;
    const freq = new Array(26).fill(0);

    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    const counts = freq.filter(x => x > 0).sort((a, b) => b - a);

    if (counts.length < k) return 0;

    const threshold = counts[k - 1];
    let greater = 0;
    let equal = 0;

    for (const f of counts) {
        if (f > threshold) greater++;
        if (f === threshold) equal++;
    }

    let answer = 1n;

    for (let i = 0; i < greater; i++) {
        answer = answer * BigInt(counts[i]) % MOD;
    }

    const choose = k - greater;

    let combination = 1n;
    for (let i = 1; i <= choose; i++) {
        combination = combination * BigInt(equal - i + 1) % MOD;
        combination = combination * modPow(BigInt(i), MOD - 2n, MOD) % MOD;
    }

    answer = answer * combination % MOD;

    for (let i = 0; i < choose; i++) {
        answer = answer * BigInt(threshold) % MOD;
    }

    return Number(answer);
};

function modPow(base, exp, mod) {
    let result = 1n;
    while (exp > 0n) {
        if (exp % 2n === 1n) result = result * base % mod;
        base = base * base % mod;
        exp /= 2n;
    }
    return result;
}
