var lastVisitedIntegers = function(nums) {
    const seen = [];
    const ans = [];
    let k = 0;

    for (const num of nums) {
        if (num !== -1) {
            seen.push(num);
            k = 0;
        } else {
            k++;
            if (k <= seen.length) {
                ans.push(seen[seen.length - k]);
            } else {
                ans.push(-1);
            }
        }
    }

    return ans;
};
