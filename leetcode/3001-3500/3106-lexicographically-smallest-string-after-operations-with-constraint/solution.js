
var getSmallestString = function(s, k) {
    let result = "";

    for (let ch of s) {
        const current = ch.charCodeAt(0) - 97;
        const cost = Math.min(current, 26 - current);

        if (k >= cost) {
            result += 'a';
            k -= cost;
        } else {
            result += String.fromCharCode(97 + current - k);
            k = 0;
        }
    }

    return result;
};

