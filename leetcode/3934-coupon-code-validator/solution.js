var validateCoupons = function(code, businessLine, isActive) {
    const priority = {
        electronics: 0,
        grocery: 1,
        pharmacy: 2,
        restaurant: 3
    };
    const validCoupons = [];
    for (let i = 0; i < code.length; i++) {
        if (
            code[i].length > 0 &&
            /^[a-zA-Z0-9_]+$/.test(code[i]) &&
            priority[businessLine[i]] !== undefined &&
            isActive[i] === true
        ) {
            validCoupons.push([
                businessLine[i],
                code[i]
            ]);
        }
    }
    validCoupons.sort((a, b) => {
        if (priority[a[0]] !== priority[b[0]]) {
            return priority[a[0]] - priority[b[0]];
        }
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;

        return 0;
    });
    return validCoupons.map(coupon => coupon[1]);
};

