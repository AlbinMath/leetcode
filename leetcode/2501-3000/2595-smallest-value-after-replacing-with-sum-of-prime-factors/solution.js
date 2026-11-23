
var smallestValue = function(n) {
    function sumPrimeFactors(num) {
        let sum = 0;

        for (let i = 2; i * i <= num; i++) {
            while (num % i === 0) {
                sum += i;
                num /= i;
            }
        }

        if (num > 1) {
            sum += num;
        }

        return sum;
    }

    while (true) {
        const sum = sumPrimeFactors(n);

        if (sum === n) {
            return n;
        }

        n = sum;
    }
};

