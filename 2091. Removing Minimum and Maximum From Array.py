def minimumDeletions(nums):
    minVal=[10**5,0]
    maxVal=[-10**5,0]
    n = len(nums)
    for i in range(n):
        if nums[i] <= minVal[0]:
            minVal[0] = nums[i]
            minVal[1] = i+1
        if nums[i] >= maxVal[0]:
            maxVal[0] = nums[i]
            maxVal[1] = i+1
    print(n)
    print(maxVal)
    print(minVal)
    return min(max(minVal[1],maxVal[1]),minVal[1]+n-maxVal[1]+1,maxVal[1]+n-minVal[1]+1,max(n-maxVal[1]+1,n-minVal[1]+1))

if __name__ == '__main__':
    print(minimumDeletions([52724,12510,62112]))
    print(minimumDeletions([0,-4,19,1,8,-2,-3,5]))
    print(minimumDeletions([-14,61,29,-18,59,13,-67,-16,55,-57,7,74])) 