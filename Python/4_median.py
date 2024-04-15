# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the arrays into a single sorted array.
        merged = nums1 + nums2

        # Sort the merged array.
        merged.sort()

        # Calculate the total number of elements in the merged array.
        total = len(merged)

        if total % 2 == 1:
            # If the total number of elements is odd, return the middle element as the median.
            return float(merged[total // 2])
        else:
            # If the total number of elements is even, calculate the average of the two middle elements as the median.
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0
        
        
# Approach 1: Merge and Sort
# Create a new array with a size equal to the total number of elements in both input arrays.
# Insert elements from both input arrays into the new array.
# Sort the new array.
# Find and return the median of the sorted array.
# Time Complexity

# In the worst case TC is O((n + m) * log(n + m)).
# Space Complexity

# O(n + m), where ‘n’ and ‘m’ are the sizes of the arrays.