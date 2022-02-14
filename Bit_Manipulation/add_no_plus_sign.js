/*
 *
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