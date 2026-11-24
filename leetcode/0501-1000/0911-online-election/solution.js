var TopVotedCandidate = function(persons, times) {
    this.times = times;
    this.leaders = new Array(persons.length);
    const counts = new Map();
    let leader = -1;
    let maxVotes = 0;
    
    for (let i = 0; i < persons.length; i++) {
        const person = persons[i];
        const votes = (counts.get(person) || 0) + 1;
        counts.set(person, votes);
    
        if (votes >= maxVotes) {
            maxVotes = votes;
            leader = person;
        }
        this.leaders[i] = leader;
    }
};

TopVotedCandidate.prototype.q = function(t) {
    let left = 0;
    let right = this.times.length - 1;
    
    while (left <= right) {
        const mid = (left + right) >> 1;
        if (this.times[mid] <= t) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return this.leaders[right];
};
