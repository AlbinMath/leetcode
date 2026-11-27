
var largestInteger = function(n, s) {
    if (s > 9 * n) {
        return -1;
    }

    if (s === 0) {
        return 0;
    }

    let result = "";

    while (s >= 9) {
        result += "9";
        s -= 9;
    }

    if (s > 0) {
        result += String(s);
    }

    while (result.length < n) {
        result += "0";
    }

    return Number(result);
};

