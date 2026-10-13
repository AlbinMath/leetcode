
var canFinish = function(numCourses, prerequisites) {
    const graph = Array.from(
        { length: numCourses },
        () => []
    );

    const indegree = new Array(numCourses).fill(0);

    // Build the graph and count prerequisites
    for (const [course, prerequisite] of prerequisites) {
        graph[prerequisite].push(course);
        indegree[course]++;
    }

    // Start with courses that have no prerequisites
    const queue = [];

    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) {
            queue.push(i);
        }
    }

    let completed = 0;
    let front = 0;

    while (front < queue.length) {
        const course = queue[front++];
        completed++;

        // Remove this course as a prerequisite
        for (const nextCourse of graph[course]) {
            indegree[nextCourse]--;

            if (indegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }

    // All courses must be completed
    return completed === numCourses;
};

