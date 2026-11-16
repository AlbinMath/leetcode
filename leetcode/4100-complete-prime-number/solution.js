
var completePrime = function(num) {
    const isPrime = (x) => {
        if (x < 2) return false;
        if (x === 2 || x === 3) return true;
        if (x % 2 === 0 || x % 3 === 0) return false;

        for (let i = 5; i * i <= x; i += 6) {
            if (x % i === 0 || x % (i + 2) === 0) {
                return false;
            }
        }
        return true;
    };

    // 1. Check all prefixes (including num itself)
    let prefix = num;
    while (prefix > 0) {
        if (!isPrime(prefix)) return false;
        prefix = Math.floor(prefix / 10);
    }

    // 2. Check all proper suffixes
    let mod = 10;
    while (mod <= num) {
        if (!isPrime(num % mod)) return false;
        mod *= 10;
    }

    return true;
};
