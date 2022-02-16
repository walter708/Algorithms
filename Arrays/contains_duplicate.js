/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
*/


var containsDuplicate = function(nums) {

    //     let obj = {};

    //     for(let i = 0; i < nums.length; i++)
    //         {
    //             obj[nums[i] ] = 0;
    //         }


    //         for(let j = 0; j < nums.length; j++)
    //         {
    //             obj[nums[j] ] +=1
    //         }

    //         for(const prop in  obj)
    //             {
    //                 if(obj[prop] > 1)
    //                     {
    //                         return true
    //                     }

    //             }
    //        return false;




    const hashSet = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (hashSet.has(nums[i])) {
            return true;
        }
        hashSet.add(nums[i])
    }
    return false;
};