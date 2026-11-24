/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function (s) {
    let arr = s.split("").map(Number);

    while (arr.length > 2) {
        const next = [];
        for (let i = 0; i < arr.length - 1; i++) {
            next.push((arr[i] + arr[i + 1]) % 10);
        }
        arr = next;
    }

    return arr[0] === arr[1];
};
