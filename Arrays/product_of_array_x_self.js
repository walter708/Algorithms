/*
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
*/
var productExceptSelf = function(nums) {

    let res = Array(nums.lenght).fill(1)

    let prefill = 1;
    let postfill = 1;

    for (let i = 0; i < nums.length; i++) {
        res[i] = prefill;

        prefill *= nums[i];
    }


    for (let j = (nums.length - 1); j >= 0; j--) {
        res[j] *= postfill;
        postfill *= nums[j];
    }
    return res;
};

console.log(productExceptSelf([2, 4, 6, 8, 10]))