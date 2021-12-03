/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    list = [];
    for (let i = 0; i < numRows; i++) {
        tempList = [];
        for (let ii = 0; ii <= i; ii++) {
            if (ii == 0 || ii == i) {
                tempList[ii] = 1;
            } else {
                sum = list[i - 1][ii - 1] + list[i - 1][ii];
                tempList.splice(ii,0,sum);
            }
        }    
        list[i] = tempList;
    }
    
    return list;
};

console.log(generate(4))