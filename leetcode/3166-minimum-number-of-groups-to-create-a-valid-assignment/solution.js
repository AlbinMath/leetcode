var minGroupsForValidAssignment = function(balls) {
    let freq = new Map();
    for (let num of balls) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    let minFreq = Math.min(...freq.values());
    for (let k = minFreq; k >= 1; k--) {
        let ans = 0;
        let valid = true;

        for (let f of freq.values()) {
            let groups = Math.ceil(f / (k + 1));

            if (groups * k > f) {
                valid = false;
                break;
            }

            ans += groups;
        }

        if (valid) {
            return ans;
        }
    }

    return -1;
};
