class Solution:
    def canReach(self, arr, start) -> bool:
        if 0<=start<len(arr) and arr[start]>=0:
            arr[start] = -arr[start]
            return arr[start]==0 or self.canReach(arr, start-arr[start]) or self.canReach(arr, start+arr[start])
        return False




if __name__ == '__main__':
    arr=[4,2,3,0,3,1,2]
    start=5
    solution=Solution()
    print(solution.canReach(arr,start))