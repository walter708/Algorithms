/* 
   You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

*/
var characterReplacement = function(s, k) {

    let hashMap = {};

    let l = 0;

    let res = 0;
    let maxf = 0

    for (let r = 0; r < s.length; r++) {
        hashMap[s[r]] = hashMap[s[r]] != undefined ? 1 + hashMap[s[r]] : 1 + 0
        maxf = Math.max(maxf, hashMap[s[r]])

        if ((r - l + 1) - maxf > k) {
            hashMap[s[l]] -= 1;
            l += 1;
        }
        res = Math.max(res, ((r - l) + 1));
    }
    return res;
};