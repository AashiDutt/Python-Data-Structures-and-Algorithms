# quicksort method
#low = first index    : high= last index

def quick_sort(nums, low, high):

# for base case like array with one or two elements only

    if low>= high:
        return

#pivot index is the centered index below which lies all small elements and above lies all large value elements

    pivot_index = partition(nums, low , high)

#calling quicksort recursively on left and right subarray

    quick_sort(nums , low, pivot_index-1)
    quick_sort(nums , pivot_index+1, high)

# finding pivot_index   ; // --> integer division
def partition(nums , low ,high):

    pivot_index = (low+high)//2

# swaping pivot value with last index(high)
    swap(nums, pivot_index, high)

    i= low

    for j in range (low, high,1):
        if nums[j]<= nums[high]:
            swap(nums, i, j)
            i=i+1

    swap(nums, i, high)
    return i

def swap(nums,i ,j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

if __name__=="__main__":

    nums = [-2,-1,0,1,0,-1,-2]
    quick_sort(nums,0,len(nums)-1)
    print(nums)
