#3. Longest Substring Without Repeating Characters

# A brute force solution would first require finding every possible substring, which would run in O(n2) time. 
# We're not done yet though, because we now have to check every substring for duplicate characters by iterating through every substring.
# Each check for duplicate characters runs in O(n) time, and we need to do that for every substring generated (which ran in O(n2) time), so the brute force approach ends up running in O(n3) time.


# Instead, we can reduce this to O(n) time by using a sliding window approach and eliminating unnecessary computations. We use two pointers, l and r, to denote where the substring starts and ends, and a dictionary called seen to keep track of the index of each character encountered. Then, we move the right pointer one character at a time to the right to expand our substring.

# At each iteration, we check for two things.

# Have we seen the newly added character (at index r) before? If we haven't, then this is a brand new character and we can just add it to the substring and extend the length
# If we have seen it before, is its last known position greater than or equal to the left index? If it is, then that means it's repeated somewhere in the substring. If not, then that means it's outside of the substring, so we can just add it to the substring and extend the length
# So if both conditions are true, the new character is repeated and we have a problem. We can get rid of the repeated character by moving up the left pointer to be one index past the last recorded index in seen. Then, we just keep moving up the right pointer until it reaches the end of the string. Since we only have to loop through the string once, and since hash table lookups run in constant time, this algorithm ends up running in O(n) time.

# For an intuitive proof of why this works and why we don't need to check all the other substrings while moving up the left pointer, please see the video - it's a bit difficult to explain without a visualization and a concrete example. But basically, all the other substrings will either still contain a repeated character or will be shorter than the last valid substring encountered, so they can be safely ignored.



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length