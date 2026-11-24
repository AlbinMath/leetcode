var getGoodIndices = function(variables, target) {
    const modPow = (base, exp, mod) => {
        if (mod === 1) return 0;
        let result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    };

    const goodIndices = [];
    for (let i = 0; i < variables.length; i++) {
        const [a, b, c, m] = variables[i];
        const first = modPow(a, b, 10);
        const second = modPow(first, c, m);
        if (second === target) {
            goodIndices.push(i);
        }
    }

    return goodIndices;
};
