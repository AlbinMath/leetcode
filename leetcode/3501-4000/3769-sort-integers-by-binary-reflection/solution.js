
var sortByReflection = function(nums) {
    function getReflection(num) {
        let reflected = 0;

        while (num > 0) {
            let bit = num & 1;
            reflected = (reflected << 1) | bit;
            num >>>= 1;
        }

        return reflected;
    }

    return nums.sort((a, b) => {
        const reflectionA = getReflection(a);
        const reflectionB = getReflection(b);

        if (reflectionA !== reflectionB) {
            return reflectionA - reflectionB;
        }

        return a - b;
    });
};

