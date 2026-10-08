class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {}

        for i in range(len(list1)):
            index_map[list1[i]] = i

        result = []
        min_sum = float('inf')

        for j in range(len(list2)):
            if list2[j] in index_map:
                current_sum = index_map[list2[j]] + j

                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [list2[j]]

                elif current_sum == min_sum:
                    result.append(list2[j])

        return result
