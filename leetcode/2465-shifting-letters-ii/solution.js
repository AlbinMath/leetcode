
var shiftingLetters = function(s, shifts) {
    const n = s.length;
    let diff = new Array(n + 1).fill(0);
    for (let [start, end, direction] of shifts) {
        let shift = direction === 1 ? 1 : -1;
        diff[start] += shift;
        diff[end + 1] -= shift;
    }
    let result = [];
    let currentShift = 0;
    for (let i = 0; i < n; i++) {
        currentShift += diff[i];
        let shift = ((currentShift % 26) + 26) % 26;
        let charCode = s.charCodeAt(i) - 97;
        let newChar = (charCode + shift) % 26;
        result.push(String.fromCharCode(newChar + 97));
    }
    return result.join('');
};

