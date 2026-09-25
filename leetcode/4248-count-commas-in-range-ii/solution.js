/**
 * @param {number} n
 * @return {number}
 */
var countCommas = function(n) {
    let ans = 0;
    let power = 1000;

    while (power <= n) {
        ans += n - power + 1;
        power *= 1000;
    }

    return ans;
};
