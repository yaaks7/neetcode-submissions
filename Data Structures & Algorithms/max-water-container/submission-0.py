class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        
        left,right = 0, len(heights)-1

        while left < right :
            currarea = 0
            if heights[left] <= heights[right]:
                currarea = heights[left]*(right - left)
                maxarea = max(maxarea, currarea)
                left +=1
            else :
                currarea = heights[right]*(right - left)
                maxarea = max(maxarea, currarea)
                right -=1
        return maxarea



        