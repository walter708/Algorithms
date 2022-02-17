/*

Given a string s, find the length of the longest substring without repeating characters.

*
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let hashSet = new Set();

    let slow = 0;
    let fast = 0;
    let maxi = 0

    while (fast < s.length) {
        if (!hashSet.has(s[fast])) {
            hashSet.add(s[fast])
            fast += 1;
            maxi = Math.max(hashSet.size, maxi)
        } else {
            hashSet.delete(s[slow])
            slow += 1;
        }
    }
    return maxi;
};