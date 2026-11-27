
var maxTotal = function(nums, s) {
    const NEG_INF = -Infinity;

    let prev = -1;
    let dpLeft = NEG_INF;
    let dpStay = NEG_INF;

    for (let i = 0; i < nums.length; i++) {
        if (s[i] === '0') continue;

        if (prev === -1) {
            dpLeft = i > 0 ? nums[i - 1] : NEG_INF;
            dpStay = nums[i];
        } else {
            const best = Math.max(dpLeft, dpStay);

            if (i === prev + 1) {
                dpLeft = dpLeft + nums[i - 1];
                dpStay = best + nums[i];
            } else {
                dpLeft = best + nums[i - 1];
                dpStay = best + nums[i];
            }
        }

        prev = i;
    }

    if (prev === -1) return 0;

    return Math.max(dpLeft, dpStay);
};

