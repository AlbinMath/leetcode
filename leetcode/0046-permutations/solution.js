var permute = function(nums) {
    const result = [];

    function backtrack(current, used) {
        if (current.length === nums.length) {
            result.push([...current]);
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;

            current.push(nums[i]);
            used[i] = true;

            backtrack(current, used);

            current.pop();
            used[i] = false;
        }
    }

    backtrack([], Array(nums.length).fill(false));

    return result;
};
