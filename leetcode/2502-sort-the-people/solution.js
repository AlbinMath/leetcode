
var sortPeople = function(names, heights) {
    const people = [];

    for (let i = 0; i < names.length; i++) {
        people.push([heights[i], names[i]]);
    }

    people.sort((a, b) => b[0] - a[0]);
    return people.map(person => person[1]);
};

