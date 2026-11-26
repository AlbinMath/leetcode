from collections import defaultdict
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = defaultdict(list)
        result = []
        
        for person_id, size in enumerate(groupSizes):
            buckets[size].append(person_id)
            if len(buckets[size]) == size:
                result.append(buckets[size])
                buckets[size] = []
                
        return result
