var finalString = function(s) {
    // Pre-allocate buffer of size 2 * n for O(1) push/unshift
    const n = s.length;
    const buffer = new Array(2 * n);
    let head = n;
    let tail = n;
    let reversedMode = false;

    for (const ch of s) {
        if (ch === 'i') {
            reversedMode = !reversedMode;
        } else if (reversedMode) {
            buffer[--head] = ch;
        } else {
            buffer[tail++] = ch;
        }
    }

    const result = buffer.slice(head, tail);
    if (reversedMode) result.reverse();
    return result.join('');
};
