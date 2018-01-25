def selection_sort(nums):
    for i in range(len(nums)-1):

        index = i
    # make a linear search for smallest number
        for j in range(i+1 , len(nums),1):
            print(i)
            print(j)
            if nums[j] < nums[index]:
                print(j)
                index = j
        if index !=i:
            swap(nums,index,i)

    return nums

#swap function
def swap(nums , i,j):
    temp = nums[i]
    nums[i]=nums[j]
    nums[j] = temp

#input function
if __name__=="__main__":
    nums = [5,6,2,4,8,7,8]

    print(selection_sort(nums))
