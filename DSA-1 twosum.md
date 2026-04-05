# Two Sum Problem (Optimized Approach)

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

### Constraints
- Each input has exactly one solution  
- You may not use the same element twice  
- Return the answer in any order  

---

## Brute Force Approach

### Idea
Check every possible pair using two nested loops.

### Complexity
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1)  

### Drawback
Inefficient for large inputs due to quadratic time complexity.

---

## Optimized Approach: Hash Map

### Core Idea
Store previously seen elements in a hash map and check if the complement exists in constant time.

---

## Algorithm

1. Initialize an empty dictionary `hash_table`
2. Iterate through the array
3. For each element:
   - Compute:
     ```
     second = target - nums[i]
     ```
   - If `second` exists in `hash_table`:
     - Return `[hash_table[second], i]`
   - Otherwise:
     - Store current element:
     ```
     hash_table[nums[i]] = i
     ```

---

## Implementation

```python
class Solution:
    def twoSum(self, nums, target):
        hash_table = {}

        for i in range(len(nums)):
            second = target - nums[i]

            if second in hash_table:
                return [hash_table[second], i]

            hash_table[nums[i]] = i