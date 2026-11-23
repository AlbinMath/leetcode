
var findOrder = function(numCourses, prerequisites) {
    const graph = Array.from(
        { length: numCourses },
        () => []
    );

    const indegree = new Array(numCourses).fill(0);

    // Build the graph
    for (const [course, prerequisite] of prerequisites) {
        graph[prerequisite].push(course);
        indegree[course]++;
    }

    // Find courses with no prerequisites
    const queue = [];

    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) {
            queue.push(i);
        }
    }

    const order = [];
    let front = 0;

    // Process courses in topological order
    while (front < queue.length) {
        const course = queue[front++];
        order.push(course);

        for (const nextCourse of graph[course]) {
            indegree[nextCourse]--;

            if (indegree[nextCourse] === 0) {
                queue.push(nextCourse);
            }
        }
    }

    // If a cycle exists, not all courses can be completed
    return order.length === numCourses ? order : [];
};

