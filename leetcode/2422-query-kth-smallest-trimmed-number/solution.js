/**
 * @param {string[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var smallestTrimmedNumbers = function(nums, queries) {
    const answer = [];

    for (const [k, trim] of queries) {
        const indices = nums.map((num, i) => ({
            value: num.slice(-trim),
            index: i
        }));

        indices.sort((a, b) => {
            if (a.value < b.value) return -1;
            if (a.value > b.value) return 1;
            return a.index - b.index;
        });

        answer.push(indices[k - 1].index);
    }

    return answer;
};
