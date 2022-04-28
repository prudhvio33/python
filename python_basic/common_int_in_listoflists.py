from typing import List


class Solution:
    def intersection(nums: List[List[int]]) -> List[int]:
        result = []
        concat = []
        n = len(nums)

        for i in range(n):
            concat += nums[i]

        for i in set(concat):
            print(set(concat), concat, len(nums))
            if concat.count(i) == len(nums):
                result.append(i)
        return sorted(result)

obj = Solution
res = Solution.intersection(nums = [[1,2,3,4],[3,4,5], [2,4,5]])
print(res)


