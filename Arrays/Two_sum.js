/* @return {number[]}
 */
var twoSum = function(nums, target) {
    if (nums == []) {
        return
    }

    let hashMap = {};
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        // Here I checked if the different has a key in the hashMap
        let val = (target - nums[left])
        if (val in hashMap) {
            return [left, hashMap[val]]
        } else {
            hashMap[nums[left]] = left;
            left += 1
        }
    }


}

console.log(twoSum([2, 7, 11, 15], target = 9))