var letterCombinations = function(digits) {
    if (digits.length === 0) return [];

    const phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };

    let result = [''];

    for (const digit of digits) {
        const letters = phone[digit];
        const combinations = [];

        for (const combination of result) {
            for (const letter of letters) {
                combinations.push(combination + letter);
            }
        }

        result = combinations;
    }

    return result;
};
