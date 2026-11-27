
var maxTotal = function(value, limit) {
    const groups = new Map();
    for (let i = 0; i < value.length; i++) {
        if (!groups.has(limit[i])) {
            groups.set(limit[i], []);
        }

        groups.get(limit[i]).push(value[i]);
    }

    let ans = 0;

    for (const [lim, values] of groups) {
        values.sort((a, b) => b - a);

        for (let i = 0; i < Math.min(lim, values.length); i++) {
            ans += values[i];
        }
    }

    return ans;
};

