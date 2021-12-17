#!/usr/bin/python

# Given a string s, find the length of the longest substring without repeating characters.
# 
#  
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



def lengthOfLongestSubstring(self, s: str) -> int:
    last_pos = defaultdict(int) # key = char, value = last position index; gets updated as we move forward
    latest = 0 # variable to store the latest duplicate
    curr_size = 0
    max_size = 0
    for i in range(len(s)):
        if s[i] in last_pos.keys():
            latest = max(latest, last_pos[s[i]]) # cause the latest could already be ahead of last_pos[s[i]]
            curr_size = i - latest
        else:
            curr_size += 1
        max_size = max(max_size, curr_size)
        last_pos[s[i]] = i
    return max_size



# condensed version


def lengthOfLongestSubstring(self, s: str) -> int:
    dict1=defaultdict(int)
    i=0
    ans=0
    for j in range(len(s)):
        if s[j] in dict1:
            i=max(i,dict1[s[j]])
        ans=max(ans,j-i+1)
        dict1[s[j]]=j+1
    return ans
