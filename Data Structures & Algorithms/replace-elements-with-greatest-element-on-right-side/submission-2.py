class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max=-1
        final=[0]*(len(arr))
        j=len(arr)-1
        while j>=0:
            final[j]=max
            if arr[j]>max:
                max=arr[j]
            j=j-1
        return final