var countStudents = function(students, sandwiches) {
    let count0 = 0;
    let count1 = 0;

    // Count students who prefer each sandwich type
    for (let student of students) {
        if (student === 0) {
            count0++;
        } else {
            count1++;
        }
    }

    // Process sandwiches from the top of the stack
    for (let sandwich of sandwiches) {
        if (sandwich === 0) {
            if (count0 === 0) return count1;
            count0--;
        } else {
            if (count1 === 0) return count0;
            count1--;
        }
    }

    return 0;
};
