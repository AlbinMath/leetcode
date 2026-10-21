
var isSymmetric = function(root) {
    function isMirror(left, right) {
        if (left === null && right === null) {
            return true;
        }

        if (left === null || right === null) {
            return false;
        }

        if (left.val !== right.val) {
            return false;
        }

        return isMirror(left.left, right.right) &&
               isMirror(left.right, right.left);
    }

    return isMirror(root.left, root.right);
};

