
var resultArray = function(nums) {
    const sorted = [...new Set(nums)].sort((a, b) => a - b);
    const rank = new Map();

    for (let i = 0; i < sorted.length; i++) {
        rank.set(sorted[i], i + 1);
    }

    const m = sorted.length;

    function createBIT() {
        const bit = new Array(m + 1).fill(0);

        return {
            query(i) {
                let count = 0;

                while (i > 0) {
                    count += bit[i];
                    i -= i & -i;
                }

                return count;
            },

            update(i) {
                while (i <= m) {
                    bit[i]++;
                    i += i & -i;
                }
            }
        };
    }

    const bit1 = createBIT();
    const bit2 = createBIT();

    const arr1 = [nums[0]];
    const arr2 = [nums[1]];

    bit1.update(rank.get(nums[0]));
    bit2.update(rank.get(nums[1]));

    for (let i = 2; i < nums.length; i++) {
        const r = rank.get(nums[i]);

        const greater1 = arr1.length - bit1.query(r);
        const greater2 = arr2.length - bit2.query(r);

        if (
            greater1 > greater2 ||
            (greater1 === greater2 && arr1.length <= arr2.length)
        ) {
            arr1.push(nums[i]);
            bit1.update(r);
        } else {
            arr2.push(nums[i]);
            bit2.update(r);
        }
    }

    return arr1.concat(arr2);
};

