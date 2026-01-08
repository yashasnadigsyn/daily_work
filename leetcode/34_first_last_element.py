from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    low, high = 0, len(nums)-1
    leftmost = len(nums)
    
    while low<=high:
        mid = (low+high)//2
        if target == nums[mid]:
            leftmost = mid
            high = mid-1
        if len(nums[low:high]) == 0:
            if leftmost < len(nums):
                return leftmost
            else:
                return [-1,-1]
        if target <= nums[mid]:
            high = mid-1
        else:
            low = mid+1
            
print(searchRange([1,3,4,5,6,5,3,1,4], 2))
        
    