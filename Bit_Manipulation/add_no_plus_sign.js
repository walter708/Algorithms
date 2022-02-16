/*
 *
Given two integers a and b, return the sum of the two integers without using the operators + and -.
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {


    while (b != 0) {
        let borrow = a & b;

        a = a ^ b;

        b = borrow << 1;

    }
    return a;
};