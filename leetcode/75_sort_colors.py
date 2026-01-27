from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ## Better
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] > nums[j] and i < j:
                nums[i], nums[j] = nums[j], nums[i]  
    print(nums)   
    
    ## Optimal
    low, mid, high = 0,0,len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low, mid = low+1, mid+1
        elif nums[mid] == 1:
            mid = mid + 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high = high-1   
    print(nums)
                
                
sortColors([2,0,2,1,1,0])