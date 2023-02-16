class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        maxRow= len(mat)-1
        minRow= 0
        while minRow < maxRow:
            midRow = (minRow+maxRow)//2
            if max(mat[midRow])>max(mat[midRow+1]):
                maxRow=midRow
            else:
                minRow = midRow+1
        return [minRow,mat[minRow].index(max(mat[minRow]))]
            