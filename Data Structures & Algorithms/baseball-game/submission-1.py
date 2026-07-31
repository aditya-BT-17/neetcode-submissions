class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum=0
        arr=[]
        for val in operations:
            if val=="+":
                arr.append((arr[-1])+(arr[-2]))
                sum=sum+arr[-1]
            elif val=="C":
                sum=sum-arr[-1]
                arr.pop()
            elif val=="D":
                arr.append(2*(arr[-1]))
                sum=sum+arr[-1]
            else:
                arr.append(int(val))
                sum=sum+arr[-1]
        return sum

                