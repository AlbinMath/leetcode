class PairMinHeap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.data[p][0] <= this.data[i][0]) break;
            [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
            i = p;
        }
    }
    pop() {
        const top = this.data[0];
        const last = this.data.pop();
        if (this.data.length > 0) {
            this.data[0] = last;
            let i = 0;
            const n = this.data.length;
            while (true) {
                let smallest = i;
                const l = (i << 1) + 1;
                const r = (i << 1) + 2;
                if (l < n && this.data[l][0] < this.data[smallest][0]) smallest = l;
                if (r < n && this.data[r][0] < this.data[smallest][0]) smallest = r;
                if (smallest === i) break;
                [this.data[i], this.data[smallest]] = [this.data[smallest], this.data[i]];
                i = smallest;
            }
        }
        return top;
    }
}


var kthSmallest = function(mat, k) {
    const kSmallestPairSums = (nums1, nums2) => {
        const heap = new PairMinHeap();
        for (let i = 0; i < nums1.length; i++) {
            heap.push([nums1[i] + nums2[0], i, 0]);
        }

        const merged = [];
        while (heap.size() > 0 && merged.length < k) {
            const [currSum, i, j] = heap.pop();
            merged.push(currSum);
            if (j + 1 < nums2.length) {
                heap.push([nums1[i] + nums2[j + 1], i, j + 1]);
            }
        }
        return merged;
    };

    let currSums = mat[0].slice(0, k);
    for (let r = 1; r < mat.length; r++) {
        currSums = kSmallestPairSums(currSums, mat[r]);
    }

    return currSums[k - 1];
};
