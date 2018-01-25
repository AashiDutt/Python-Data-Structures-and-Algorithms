def insertion_sort(nums):
    for i in range(len(nums)):
        print('initial value of i is =',i)
        j=i
        while j>0 and nums[j-1] > nums[j]:
            print("value of i is = ",i)
            swap(nums, j, j-1)                                # disadvantage of insertion sort is too many swap operations
            print('value of j is =',j)
            j=j-1
    return nums

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] =temp

if __name__ =="__main__":

    nums =[1, 3,5,100,4,7]
    print( insertion_sort(nums))
