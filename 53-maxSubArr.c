#include <stdio.h>
#include <stdlib.h>

int maxSubArray(int* nums, int numsSize){
    int maxSum = nums[0];
    int sum = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (sum >= 0) {
            sum += nums[i];
        } else {
            sum = nums[i];
        }
        
        if (sum >= maxSum) {
            maxSum = sum;
        }
    }
    return maxSum;
}

int main(void) {
    int testArr[9] = {-2,1,-3,4,-1,2,1,-5,4};
    int size = 9;

    int maxSum = maxSubArray(testArr, size);
    printf("%d", maxSum);

    return 0;
}