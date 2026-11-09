
var isSubPath = function(head, root) {

    // Check whether the linked list matches
    // a downward path starting at this tree node
    function dfs(head, root) {
        if (!head) return true;

        if (!root) return false;

        if (head.val !== root.val) {
            return false;
        }

        return (
            dfs(head.next, root.left) ||
            dfs(head.next, root.right)
        );
    }

    // Try starting the linked list from every tree node
    function search(root) {
        if (!root) return false;

        return (
            dfs(head, root) ||
            search(root.left) ||
            search(root.right)
        );
    }

    return search(root);
};

