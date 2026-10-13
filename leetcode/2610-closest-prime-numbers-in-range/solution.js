
var closestPrimes = function(left, right) {
    const isPrime = new Uint8Array(right + 1);
    isPrime.fill(1);

    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= right; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= right; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    let prev = -1;
    let minGap = Infinity;
    let ans = [-1, -1];

    for (let num = left; num <= right; num++) {
        if (isPrime[num]) {
            if (prev !== -1 && num - prev < minGap) {
                minGap = num - prev;
                ans = [prev, num];

                if (minGap === 2) {
                    return ans;
                }
            }

            prev = num;
        }
    }

    return ans;
};

