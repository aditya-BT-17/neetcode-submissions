class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currsum=0

        for n in nums:
            if currsum<=0:
                currsum=0
            currsum=currsum+n
            maxsum=max(currsum,maxsum)
        return maxsum