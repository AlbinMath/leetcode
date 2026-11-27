
var maximumValue = function(n, s, m) {
    if (n === 1) {
        return s;
    }

    return s + m + Math.floor((n - 2) / 2) * (m - 1);
};

