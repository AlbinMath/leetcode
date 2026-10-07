class Solution {
    function deleteDuplicates($head) {
        $current = $head;

        while ($current !== null && $current->next !== null) {

            if ($current->val == $current->next->val) {
                // Skip duplicate node
                $current->next = $current->next->next;
            } else {
                // Move to next node
                $current = $current->next;
            }
        }

        return $head;
    }
}
