var countOrders = function(n) {
    const MOD = 1_000_000_007;
    let result = 1;

    for (let i = 2; i <= n; i++) {
        result = (result * (i * (2 * i - 1))) % MOD;
    }

    return result;
};
