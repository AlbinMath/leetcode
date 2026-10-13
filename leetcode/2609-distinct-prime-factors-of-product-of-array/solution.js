
var distinctPrimeFactors = function(nums) {
    const primeFactors = new Set();

    for (let num of nums) {
        for (let i = 2; i * i <= num; i++) {
            if (num % i === 0) {
                primeFactors.add(i);

                while (num % i === 0) {
                    num /= i;
                }
            }
        }

        if (num > 1) {
            primeFactors.add(num);
        }
    }

    return primeFactors.size;
};

