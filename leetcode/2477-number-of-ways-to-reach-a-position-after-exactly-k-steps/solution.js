var numberOfWays = function(startPos, endPos, k) {
    const MOD = 1000000007n;
    const distance = endPos - startPos;

    if (Math.abs(distance) > k || (k + distance) % 2 !== 0) {
        return 0;
    }

    const right = (k + distance) / 2;
    const left = k - right;

    let result = 1n;

    for (let i = 1; i <= Math.min(right, left); i++) {
        result = result * BigInt(k - i + 1) / BigInt(i);
    }

    return Number(result % MOD);
};
