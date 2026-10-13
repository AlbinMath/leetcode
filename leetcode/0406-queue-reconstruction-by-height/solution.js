
var reconstructQueue = function(people) {
    // Sort by height descending.
    // For equal heights, sort by k ascending.
    people.sort((a, b) => {
        if (b[0] !== a[0]) {
            return b[0] - a[0];
        }
        return a[1] - b[1];
    });

    const queue = [];

    // Insert each person at their required index
    for (const person of people) {
        queue.splice(person[1], 0, person);
    }

    return queue;
};

