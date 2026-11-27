
var smallestNumber = function(num) {
    const digits = Math.abs(num).toString().split("");

    if (num >= 0) {
        digits.sort((a, b) => a - b);
        const firstNonZero = digits.findIndex(digit => digit !== "0");
        if (firstNonZero !== -1) {
            [digits[0], digits[firstNonZero]] =
                [digits[firstNonZero], digits[0]];
        }
        return Number(digits.join(""));
    } else {
        digits.sort((a, b) => b - a);
        return -Number(digits.join(""));
    }
};

