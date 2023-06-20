// Given an array of integers nums and an integer target, return indices of the two numbers such that they 
// add up to target.You may assume that each input would have exactly one solution, and you may not use the 
// same element twice. You can return the answer in any order.

// EXAMPLE

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


// const twoSum = (num, target) => {
//     // itterate 
//     for(let i=0; i< num.length; i++){
//         if (i != num.length - 1){
//             for(let j=i+1; j<num.length; j++){
//                 if (num[i] + num[j] == target){
//                     return [i,j]
//                 }
//             }
//         }
//     }
// }

// const twoSum = (nums, target, map = new Map()) => {
//     for (let index = 0; index < nums.length; index++) {/* Time O(N) */
//         const num = nums[index];
//         const complement = (target - num);
//         const sumIndex = map.get(complement);

//         const isTarget = map.has(complement)
//         if (isTarget) return [ sumIndex, index ];

//         map.set(num, index);                                /* Space O(N) */
//     }

//     return [ -1, -1 ];
// }


const twoSum = (arr, target) => {
    var newMap = new Map(); //  number : index

    for (let i=0; i<arr.length; i++){
        const difference = target - arr[i];
        
        if (newMap.has(difference)){
            return [newMap.get(difference), i]
        }
        newMap.set(arr[i], i)
    }
    console.log(newMap);
}

console.log(twoSum([2,7,11,15], 9)); // [0,1]
console.log(twoSum([3,2,4], 6)); // [1,2]
console.log(twoSum([3,3], 6)); // [0,1]