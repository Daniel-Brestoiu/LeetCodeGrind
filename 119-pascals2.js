/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    list = [];
    for (let i = 0; i < rowIndex + 1; i++) {
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
    console.log(list);
    return list[list.length - 1];
};
