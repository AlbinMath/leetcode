class Solution {
    function deleteDuplicates($head) {
        // Dummy node handles duplicates at the beginning
        $dummy = new ListNode(0);
        $dummy->next = $head;

        $prev = $dummy;
        $current = $head;

        while ($current !== null) {

            // Check if current node has duplicates
            if ($current->next !== null &&
                $current->val == $current->next->val) {

                $duplicateValue = $current->val;

                // Skip all nodes with this value
                while ($current !== null &&
                       $current->val == $duplicateValue) {
                    $current = $current->next;
                }

                // Connect previous distinct node
                $prev->next = $current;

            } else {
                // Current node is unique
                $prev = $current;
                $current = $current->next;
            }
        }

        return $dummy->next;
    }
}
