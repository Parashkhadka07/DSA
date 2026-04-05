

class Solution:
    def twoSum(self,nums,target):
        hash_table={}
        for i in range(len(nums)):
            first=nums[i]
            second=target-nums[i]
            if second in hash_table:
                return(i,hash_table[second])
            hash_table[nums[i]]=i 
        

solution=Solution()
nums=[3,0,4]
target=6
aoln=solution.twoSum(nums,target)
print(aoln)
