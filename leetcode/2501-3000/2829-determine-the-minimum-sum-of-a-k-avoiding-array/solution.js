var minimumSum = function(n, k) {
    let sum = 0;
    let count = 0;
    let num = 1;
    let selected = new Set();

    while (count < n) {
        if (!selected.has(k - num)) {
            selected.add(num);
            sum += num;
            count++;
        }
        num++;
    }

    return sum;
};
