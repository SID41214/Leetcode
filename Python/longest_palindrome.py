#Longest Palindromic Substring
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) <= 1:
#             return s
        
#         Max_Len=1
#         Max_Str=s[0]
#         dp = [[False for _ in range(len(s))] for _ in range(len(s))]
#         for i in range(len(s)):
#             dp[i][i] = True
#             for j in range(i):
#                 if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
#                     dp[j][i] = True
#                     if i-j+1 > Max_Len:
#                         Max_Len = i-j+1
#                         Max_Str = s[j:i+1]
#         return Max_Str

def longest_palindromic_substring(s):
    if len(s) <= 1:
        return s
    
    start, max_length = 0, 1
    dp = [[False] * len(s) for _ in range(len(s))]
    
    # All substrings of length 1 are palindromes
    for i in range(len(s)):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for substrings of length 3 or more
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

# Example usage
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # Output: "bb"
