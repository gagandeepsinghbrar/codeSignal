function minesweeper(matrix) {
    var ans = []
    for (let i = 0; i < matrix.length; i ++) {
        var arr = []
        for (let j = 0; j < matrix[i].length; j ++) {
            var num = 0
            for (let k = i - 1; k <= i + 1; k ++) {
                for (let m = j - 1; m <= j + 1; m ++) {
                    if (matrix[k] !== undefined && matrix[k][m]) num ++
                }
            }
            if (matrix[i][j]) num --
            arr.push(num)
        }
        ans.push(arr)
    }
    return ans
}
