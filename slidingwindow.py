# Sliding Window — Solutions

## 1. Longest Substring Without Repeating Characters — LeetCode #3

def lengthOfLongestSubstring(s):
    seen = {}  # character -> most recent index seen at
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        ch = s[right]
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len


## 2. Longest Repeating Character Replacement — LeetCode #424

def characterReplacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_len = 0
    
    for right in range(len(s)):
        ch = s[right]
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])
        
        window_len = right - left + 1
        if window_len - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len


## 3. Minimum Size Subarray Sum — LeetCode #209

def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0
