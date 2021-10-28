/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let nums2Counter = 0;
    for (let i = 0; i < m + n; i++) {
        let pastM = (i >= m + nums2Counter);
        if (nums2[nums2Counter] < nums1[i] || pastM) {
            nums1.splice(i,pastM,nums2[nums2Counter]);    
            nums2Counter++;
        }
    }
    
    //Get rid of extraneous 0's.
    while (nums1.length > n + m) {
        nums1.pop();
    }
};