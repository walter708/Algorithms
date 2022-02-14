/*
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
*/

var maxProfit = function(prices) {
    let diff = 0;
    let sm = prices[0];

    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < sm) {
            sm = prices[i]
        } else {
            if ((prices[i] - sm) > diff) {
                diff = (prices[i] - sm);
            }
        }
    }
    if (diff <= 0) {
        return 0;
    } else {
        return diff
    }
};