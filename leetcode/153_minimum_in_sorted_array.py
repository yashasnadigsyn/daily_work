from typing import List

def findMin(nums: List[int]) -> int:
    low, high = 0, len(nums)-1
    while low<=high:
        mid = (low+high)//2
        print(low, mid, high)
        if nums[mid] > nums[high]:
            low=mid+1
        else:
            high=mid-1
    return nums[low]
            
# print(findMin([4,5,6,7,0,1,2]))
print(findMin([3,4,5,1,2]))
# print(findMin([11,13,15,17]))
print(findMin([2,1]))
print(findMin([1,2]))