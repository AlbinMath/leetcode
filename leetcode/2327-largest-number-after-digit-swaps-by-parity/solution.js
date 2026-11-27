
var largestInteger = function(num) {
    const digits = num.toString().split("").map(Number);

    const odd = [];
    const even = [];

    for (const digit of digits) {
        if (digit % 2 === 0) {
            even.push(digit);
        } else {
            odd.push(digit);
        }
    }

    odd.sort((a, b) => b - a);
    even.sort((a, b) => b - a);
    let result = "";

    for (const digit of digits) {
        if (digit % 2 === 0) {
            result += even.shift();
        } else {
            result += odd.shift();
        }
    }

    return Number(result);
};

