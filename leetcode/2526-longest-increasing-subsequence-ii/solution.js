
var lengthOfLIS = function(nums, k) {
    const MAX = 100000;
    const tree = new Array(4 * (MAX + 1)).fill(0);

    function query(node, start, end, left, right) {
        if (right < start || end < left) {
            return 0;
        }

        if (left <= start && end <= right) {
            return tree[node];
        }

        const mid = Math.floor((start + end) / 2);

        return Math.max(
            query(node * 2, start, mid, left, right),
            query(node * 2 + 1, mid + 1, end, left, right)
        );
    }

    function update(node, start, end, index, value) {
        if (start === end) {
            tree[node] = Math.max(tree[node], value);
            return;
        }

        const mid = Math.floor((start + end) / 2);

        if (index <= mid) {
            update(node * 2, start, mid, index, value);
        } else {
            update(node * 2 + 1, mid + 1, end, index, value);
        }

        tree[node] = Math.max(
            tree[node * 2],
            tree[node * 2 + 1]
        );
    }

    let answer = 0;

    for (const x of nums) {
        const left = Math.max(1, x - k);
        const right = x - 1;

        const best = left <= right
            ? query(1, 1, MAX, left, right)
            : 0;

        const current = best + 1;

        update(1, 1, MAX, x, current);

        answer = Math.max(answer, current);
    }

    return answer;
};

