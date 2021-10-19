#include <stdio.h>
#include <stdlib.h>

//Recursive Solution:
//Faster than 100% of C solutions.
int searchInsertHelper(int * nums, int numsSize, int target, int indexesSpent) {
    int middle = numsSize / 2;
    
    if (nums[middle] == target) {
        //Found item.
        return middle + indexesSpent;
    }  else if (nums[middle] < target) {
        //Binary search right half.
        if (middle == numsSize - 1) {
            //Not found item, and index is last item in Arr.
            return numsSize + indexesSpent;        
        } 
        return searchInsertHelper(nums + middle, numsSize - middle, target, middle + indexesSpent);
    } else if (nums[middle] > target) {
        //Binary search left half.
        if (middle == 0) {
            //Not found item, and index is 0. 
            return middle + indexesSpent;
        }
        return searchInsertHelper(nums, middle, target, indexesSpent );
    }
    
    return -1;
}

int searchInsert(int* nums, int numsSize, int target){
    return searchInsertHelper(nums, numsSize, target, 0);
}

int main(void) {
    int arrLen = 4;
    int arr[4] = {1, 3, 5, 6};

    int value = searchInsert(arr, arrLen, 1);
    printf("%d", value);

    return 0;
}