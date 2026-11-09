
var lengthLongestPath = function(input) {
    const paths = input.split('\n');

    // Store path lengths at each depth
    const stack = [0];

    let maxLength = 0;

    for (let path of paths) {
        // Count directory depth
        const depth = path.lastIndexOf('\t') + 1;

        // Remove tab characters
        const name = path.slice(depth);

        // Calculate current absolute path length
        const currentLength = stack[depth] + name.length;

        if (name.includes('.')) {
            // It is a file
            maxLength = Math.max(maxLength, currentLength);
        } else {
            // It is a directory
            stack[depth + 1] = currentLength + 1;
        }
    }

    return maxLength;
};

