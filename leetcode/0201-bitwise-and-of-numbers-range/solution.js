
var rangeBitwiseAnd = function(left, right) {
    let shifts = 0;

    while (left < right) {
        left >>>= 1;
        right >>>= 1;
        shifts++;
    }

    return left << shifts;
};

