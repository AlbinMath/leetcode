var calculateTax = function(brackets, income) {
    let totalTax = 0;
    let prevUpper = 0;

    for (const [upper, percent] of brackets) {
        if (income <= prevUpper) {
            break;
        }

        const taxable = Math.min(income, upper) - prevUpper;
        totalTax += taxable * (percent / 100);
        prevUpper = upper;
    }

    return totalTax;
};
