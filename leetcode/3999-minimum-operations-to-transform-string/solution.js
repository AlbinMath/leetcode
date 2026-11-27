
var minOperations = function(s) {
    let ans = 0;

    for (let i = 0; i < s.length; i++) {
        const distance = 26 - (s.charCodeAt(i) - 97);

        ans = Math.max(ans, distance === 26 ? 0 : distance);
    }

    return ans;
};

