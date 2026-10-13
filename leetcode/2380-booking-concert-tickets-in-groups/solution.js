
var BookMyShow = function(n, m) {
    this.n = n;
    this.m = m;
    this.remaining = new Array(n).fill(m);

    this.sumTree = new Array(4 * n).fill(0);
    this.maxTree = new Array(4 * n).fill(0);

    const build = (node, start, end) => {
        if (start === end) {
            this.sumTree[node] = m;
            this.maxTree[node] = m;
            return;
        }

        const mid = Math.floor((start + end) / 2);
        build(node * 2, start, mid);
        build(node * 2 + 1, mid + 1, end);
        this.pull(node);
    };

    this.pull = (node) => {
        this.sumTree[node] =
            this.sumTree[node * 2] + this.sumTree[node * 2 + 1];

        this.maxTree[node] = Math.max(
            this.maxTree[node * 2],
            this.maxTree[node * 2 + 1]
        );
    };

    this.update = (node, start, end, index, value) => {
        if (start === end) {
            this.sumTree[node] = value;
            this.maxTree[node] = value;
            return;
        }

        const mid = Math.floor((start + end) / 2);

        if (index <= mid) {
            this.update(node * 2, start, mid, index, value);
        } else {
            this.update(node * 2 + 1, mid + 1, end, index, value);
        }

        this.pull(node);
    };

    this.querySum = (node, start, end, left, right) => {
        if (right < start || end < left) return 0;

        if (left <= start && end <= right) {
            return this.sumTree[node];
        }

        const mid = Math.floor((start + end) / 2);

        return (
            this.querySum(node * 2, start, mid, left, right) +
            this.querySum(node * 2 + 1, mid + 1, end, left, right)
        );
    };

    this.findRow = (node, start, end, maxRow, k) => {
        if (start > maxRow || this.maxTree[node] < k) {
            return -1;
        }

        if (start === end) return start;

        const mid = Math.floor((start + end) / 2);

        let row = this.findRow(
            node * 2, start, mid, maxRow, k
        );

        if (row !== -1) return row;

        return this.findRow(
            node * 2 + 1, mid + 1, end, maxRow, k
        );
    };

    this.consume = (node, start, end, k) => {
        if (start === end) {
            const taken = Math.min(k, this.remaining[start]);
            this.remaining[start] -= taken;
            this.update(1, 0, this.n - 1, start, this.remaining[start]);
            return k - taken;
        }

        const mid = Math.floor((start + end) / 2);
        let leftOver = k;

        const leftSum = this.sumTree[node * 2];

        if (leftSum > 0) {
            leftOver = this.consume(
                node * 2, start, mid, leftOver
            );
        }

        if (leftOver > 0) {
            leftOver = this.consume(
                node * 2 + 1, mid + 1, end, leftOver
            );
        }

        this.pull(node);
        return leftOver;
    };

    build(1, 0, n - 1);
};

BookMyShow.prototype.gather = function(k, maxRow) {
    const row = this.findRow(1, 0, this.n - 1, maxRow, k);

    if (row === -1) return [];

    const seat = this.m - this.remaining[row];

    this.remaining[row] -= k;
    this.update(1, 0, this.n - 1, row, this.remaining[row]);

    return [row, seat];
};

BookMyShow.prototype.scatter = function(k, maxRow) {
    const available = this.querySum(
        1, 0, this.n - 1, 0, maxRow
    );

    if (available < k) return false;

    this.consume(1, 0, maxRow, k);

    return true;
};

