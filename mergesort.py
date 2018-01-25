def merge_sort(nums):

    if len(nums) == 1:
# if array has single  (base case)
        return

#divide part

    middle_index = len(nums)//2
# integer division
#create subarrays
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

#calling merge sort recursively untill a single element is left i.e len(nums)=1
    merge_sort(left_half)
    merge_sort(right_half)


#conquer part
    i=0 # index of left subarray
    j=0 # index of right sub array
    k=0 # index of new array

#consider all elements in both subarrays
    while i<len(left_half) and j<len(right_half):

#if element in leftsubarray is smaller than element in right subarray
        if left_half[i] < right_half[j]:

# put the no. in the new array having indices "k"
            nums[k] = left_half[i]
            i=i+1
        else:
            nums[k] = right_half[j]
            j=j+1
        k = k+1
# in case all elements of either subarray are already copied to new array(copy leftovers)
#and no no. is left to compare then copy the opposite array as it is to the new array
    while i<len(left_half):
        nums[k] =left_half[i]
        k=k+1
        i = i+1

    while j<len(right_half):
        nums[k] = right_half[j]
        k= k+1
        j = j+1

if __name__=="__main__":
    nums=[32, -12, 0 , 3, 1,12 ,20]
    merge_sort(nums)
    print(nums)


