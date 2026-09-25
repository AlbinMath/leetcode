/**
 * @param {number} n
 * @return {number}
 */
var countCommas = function(n) {
    let count = 0;

    for (let i = 1000; i <= n; i++) {
        count += Math.floor((i.toString().length - 1) / 3);
    }

    return count;
};
