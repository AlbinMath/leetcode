
var maximumSumQueries = function(nums1, nums2, queries) {
    const n = nums1.length;

    // Store points as [x, y, sum]
    const points = [];
    const ys = [...nums2].sort((a, b) => a - b);

    for (let i = 0; i < n; i++) {
        points.push([nums1[i], nums2[i], nums1[i] + nums2[i]]);
    }

    // Sort points by x descending
    points.sort((a, b) => b[0] - a[0]);

    // Sort queries by x descending, retaining original indices
    const sortedQueries = queries
        .map(([x, y], i) => [x, y, i])
        .sort((a, b) => b[0] - a[0]);

    // Coordinate compression of nums2
    const uniqueY = [...new Set(ys)];
    const m = uniqueY.length;

    // Iterative segment tree storing maximum sums
    let size = 1;
    while (size < m) size *= 2;

    const tree = new Array(size * 2).fill(-1);

    function update(pos, value) {
        let i = pos + size;
        tree[i] = Math.max(tree[i], value);

        for (i >>= 1; i > 0; i >>= 1) {
            tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    // Maximum sum over compressed indices [left, m - 1]
    function query(left) {
        let l = left + size;
        let r = m - 1 + size;
        let result = -1;

        while (l <= r) {
            if (l % 2 === 1) result = Math.max(result, tree[l++]);
            if (r % 2 === 0) result = Math.max(result, tree[r--]);

            l >>= 1;
            r >>= 1;
        }

        return result;
    }

    const answer = new Array(queries.length).fill(-1);
    let p = 0;

    for (const [x, y, index] of sortedQueries) {
        // Insert every point satisfying nums1 >= x
        while (p < n && points[p][0] >= x) {
            const [px, py, sum] = points[p++];

            const pos = lowerBound(uniqueY, py);
            update(pos, sum);
        }

        // Find the first compressed y >= the query's y
        const left = lowerBound(uniqueY, y);

        if (left < m) {
            answer[index] = query(left);
        }
    }

    return answer;
};

function lowerBound(arr, target) {
    let left = 0;
    let right = arr.length;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

