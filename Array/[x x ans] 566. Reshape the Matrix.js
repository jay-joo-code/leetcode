// x x ans

/**
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
const matrixReshapeAttemptOne = (nums, r, c) => {
    let elts = [];
    // error: Array.fill fills array with the exact same object
    // reshaped is filled with the exact same array
    // hence mutating one row will mutate all rows
    let reshaped = Array(r).fill(Array(c).fill(null));
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums[i].length; j++) {
            elts.push(nums[i][j]);
        }
    }
    if (elts.length !== r * c) return nums;
    for (let i = 0; i < r; i++) {
        for (let j = 0; j < c; j++) {
            const newElt = elts.shift();
            reshaped[i][j] = newElt;
        }
    }
    return reshaped;
};

// console.log('matrixReshapeAttemptOne([[1,2],[3,4]], 4, 1) :>> ', matrixReshapeAttemptOne([[1,2],[3,4]], 4, 1));

const ans = (nums, r, c) => {
    if ((currentRows * currentCols) !== (r * c)) {
        return nums; // not possible to reshape
    }
	
	// index of next position to place elt in reshaped matrix
    let rIdx = 0;
    let cIdx = 0;
	
	let matrix = [];
    
    for (let row = 0; row < nums.length; row++) {
        for (let col = 0; col < nums[row].length; col++) {
            if (!matrix[rIdx]) {
                matrix.push([]);
            }
            
            matrix[rIdx].push(nums[row][col]); 
            cIdx += 1;
			
            if (cIdx === c) {
                cIdx = 0;
                rIdx += 1;
            }
        }
    }
    
    return matrix;
}

console.log('ans([[1,2],[3,4]], 4, 1) :>> ', ans([[1,2],[3,4]], 4, 1));