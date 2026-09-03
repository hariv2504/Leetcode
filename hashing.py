# Hashing — Solutions

## 1. Two Sum — LeetCode #1

def twoSum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


## 2. Contains Duplicate — LeetCode #217

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


## 3. Valid Anagram — LeetCode #242

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    return True


## 4. Group Anagrams — LeetCode #49

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


## 5. Longest Consecutive Sequence — LeetCode #128

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:  # only start counting from sequence starts
            length = 1
            while (num + length) in num_set:
                length += 1
            longest = max(longest, length)
    return longest


## 6. Intersection of Two Arrays — LeetCode #349

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)


## 7. Isomorphic Strings — LeetCode #205
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    map_s_to_t = {}
    map_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t
        
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s
    
    return True


## 8. Contains Duplicate II — LeetCode #219

def containsNearbyDuplicate(nums, k):
    last_seen = {}
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False


## 9. Single Number — LeetCode #136

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
