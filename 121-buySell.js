/**
 * @param {number[]} prices
 * @return {number}
*/

let maxProfit = function(prices) {
    let buy = prices[0];
    let sell = prices[0];
    let delta = sell - buy;
    
    for (let i = 0; i < prices.length;i++) {
        if (prices[i] > sell) {
            sell = prices[i];
        }
        if (prices[i] < buy) {
            delta = sell - buy;
            let j = i + 1;
            while (j < prices.length) {
                if (prices[j] - prices[i] > delta) {
                    buy = prices[i];
                    sell = prices[j];
                    i = j;
                    break;
                }
                if (prices[j] < prices[i]) {
                    i = j - 1;
                    break;
                }
                j++;
            }
            if (j == prices.length) {
                i = j;
            }
        }
    }
    delta = sell - buy;
    return delta > 0 ? delta : 0;
};