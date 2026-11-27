
var rearrangeString = function(s, x, y) {
    let other = "";
    let xChars = "";
    let yChars = "";

    for (const ch of s) {
        if (ch === y) {
            yChars += ch;
        } else if (ch === x) {
            xChars += ch;
        } else {
            other += ch;
        }
    }

    return other + yChars + xChars;
};

