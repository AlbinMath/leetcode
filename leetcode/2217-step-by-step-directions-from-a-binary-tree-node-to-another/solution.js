
var getDirections = function(root, startValue, destValue) {
    function findPath(node, target, path) {
        if (node === null) return false;

        if (node.val === target) return true;

        path.push("L");
        if (findPath(node.left, target, path)) return true;
        path.pop();

        path.push("R");
        if (findPath(node.right, target, path)) return true;
        path.pop();

        return false;
    }

    const startPath = [];
    const destPath = [];

    findPath(root, startValue, startPath);
    findPath(root, destValue, destPath);

    let i = 0;

    while (
        i < startPath.length &&
        i < destPath.length &&
        startPath[i] === destPath[i]
    ) {
        i++;
    }

    return "U".repeat(startPath.length - i) +
           destPath.slice(i).join("");
};

