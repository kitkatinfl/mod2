# kathleen Module 3 binary search assignment
# 9/4/24

#define function
def binary_search(arr,k,low,high):

    if high>=low:

        median=(high+low)//2

        if arr[median]==k:
            return median
        elif arr[median]<k:
            return binary_search(arr,k,median+1,high)
        else:
            return binary_search(arr,k,low,median-1)
    else:
        return -1

#static variables
arr=[5,20,62,77,91,100]
k=90

# function call
ans=binary_search(arr,k,0,len(arr)-1)
if ans != -1:
    print('Value',k,'found in index pos',ans)
else:
    print('Value',k,'not found')
    