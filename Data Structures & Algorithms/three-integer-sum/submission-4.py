class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans=[]

        for i in range (len(nums)-2):
            target = -nums[i]
            left , right = i+1, len(nums)-1

            while left < right :
                pair = [nums[i],nums[left],nums[right]]
                if pair not in ans and nums[left]+ nums[right] == target :
                    ans.append(pair) 
                    right -=1
                    left +=1
                elif nums[left]+ nums[right] > target : 
                    right -=1
                else:
                    left +=1
        return ans
        