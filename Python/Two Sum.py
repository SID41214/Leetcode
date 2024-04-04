# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numin={}

#         for i,num in enumerate(nums):
#             complement = target - num

#             if complement in numin:
#                 return [numin[complement],i]

#             numin[num]=i


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numin = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numin:
                return [numin[complement], i]

            numin[num] = i

# Example usage
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [2, 7, 11, 15]
#     target = 9
#     result = solution.twoSum(nums, target)
#     print(result)
