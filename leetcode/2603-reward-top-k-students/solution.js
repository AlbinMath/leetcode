
var topStudents = function(positive_feedback, negative_feedback, report, student_id, k) {
    const positive = new Set(positive_feedback);
    const negative = new Set(negative_feedback);

    const students = [];

    for (let i = 0; i < report.length; i++) {
        const words = report[i].split(" ");

        let score = 0;

        for (const word of words) {
            if (positive.has(word)) {
                score += 3;
            } else if (negative.has(word)) {
                score -= 1;
            }
        }

        students.push({
            id: student_id[i],
            score: score
        });
    }

    students.sort((a, b) => {
        if (a.score !== b.score) {
            return b.score - a.score;
        }

        return a.id - b.id;
    });

    return students.slice(0, k).map(student => student.id);
};

