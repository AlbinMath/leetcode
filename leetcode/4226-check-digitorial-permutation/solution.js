
var isDigitorialPermutation = function(n) {
    const fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880];

    // Step 1: Calculate sum of digit factorials
    let temp = n;
    let sum = 0;

    while (temp > 0) {
        let digit = temp % 10;
        sum += fact[digit];
        temp = Math.floor(temp / 10);
    }

    // Step 2: Count digits of original number
    const freq1 = new Array(10).fill(0);
    const freq2 = new Array(10).fill(0);

    temp = n;

    while (temp > 0) {
        freq1[temp % 10]++;
        temp = Math.floor(temp / 10);
    }

    // Step 3: Count digits of factorial sum
    temp = sum;

    while (temp > 0) {
        freq2[temp % 10]++;
        temp = Math.floor(temp / 10);
    }

    // Step 4: Compare digit frequencies
    for (let i = 0; i < 10; i++) {
        if (freq1[i] !== freq2[i]) {
            return false;
        }
    }

    return true;
};

