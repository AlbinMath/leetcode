
var clumsy = function(n) {
    let total = 0;
    let current = n;
    let sign = 1;

    for (let i = n - 1; i > 0; i--) {
        const op = (n - i - 1) % 4;

        if (op === 0) {
            // Multiplication
            current *= i;
        }
        else if (op === 1) {
            // Floor division
            current = Math.floor(current / i);
        }
        else if (op === 2) {
            // Addition: finish previous group
            total += sign * current;
            sign = 1;
            current = i;
        }
        else {
            // Subtraction: finish previous group
            total += sign * current;
            sign = -1;
            current = i;
        }
    }

    return total + sign * current;
};

