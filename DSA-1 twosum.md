#Two Sum – Hash Map Approach
Approach

This solution uses a hash map (Python dictionary) to store previously visited elements and their indices while iterating through the array.

For each element, we compute its complement (target - current value) and check whether it already exists in the hash map.

If the complement exists, we immediately return the indices of both elements.
Otherwise, we store the current element and continue.
Algorithm
Initialize an empty dictionary hash_table.
Iterate through the list using index i.
For each element:
Compute second = target - nums[i]
If second exists in hash_table:
Return [hash_table[second], i]
Otherwise, store nums[i] with index i in the hash map
Continue until the solution is found.
Code
class Solution:
def twoSum(self, nums, target):
hash_table = {}

        for i in range(len(nums)):
            second = target - nums[i]

            if second in hash_table:
                return [hash_table[second], i]

            hash_table[nums[i]] = i

Complexity Analysis
Metric Value
Time Complexity O(n)
Space Complexity O(n)
Each lookup and insertion in the hash map takes O(1) on average.
Only one pass through the array is required. 5. Final critique

You’re close, but still coding like:

“trial and adjust”

Instead, aim for:

“clear invariant → predictable behavior → minimal code”
