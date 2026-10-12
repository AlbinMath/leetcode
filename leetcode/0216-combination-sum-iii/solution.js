var combinationSum3 = function(k, n) {
    const result = [];
    const path = [];

    function backtrack(start, remaining) {
        if (path.length === k) {
            if (remaining === 0) {
                result.push([...path]);
            }
            return;
        }

        for (let num = start; num <= 9; num++) {
            if (num > remaining) {
                break;
            }

            path.push(num);
            backtrack(num + 1, remaining - num);
            path.pop();
        }
    }

    backtrack(1, n);
    return result;
};
