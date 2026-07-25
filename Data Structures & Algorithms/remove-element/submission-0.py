class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expectedNum=[]
        k=0
        for i in range (len(nums)):
            if nums[i]!=val:
                expectedNum.append(nums[i])
            else:
                k=k+1
        for j in range(len(nums)-k):
            nums[j]=expectedNum[j]
        return len(nums)-k
