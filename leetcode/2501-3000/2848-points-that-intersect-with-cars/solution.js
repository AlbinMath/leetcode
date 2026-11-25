
var numberOfPoints = function(nums) {
    const covered = new Array(101).fill(false);
    for (let [start, end] of nums) {
        for (let i = start; i <= end; i++) {
            covered[i] = true;
        }
    }
    let ans = 0;

    for (let i = 1; i <= 100; i++) {
        if (covered[i]) {
            ans++;
        }
    }

    return ans;
};

