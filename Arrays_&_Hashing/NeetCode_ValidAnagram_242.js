// =========== HASHMAP ==============
// const sMap = new Map();
// const tMap = new Map();

// console.log(sMap);
// console.log(tMap);

// s = 'cool'

// for (let char of s) {
//     sMap.set(char, (sMap.get(char) || 0) + 1);
//     tMap.set(char, (tMap.get(char) || 0) + 1);
// }
// console.log(sMap);
// console.log(tMap);



// ==================
// FIRST SOLUTION
// ==================

const isAnagram = (s, t) => {
    if (t.length != s.length){
        return false
    }

    let sMap = new Map();
    let tMap = new Map();

    for (let char of s) {
        sMap.set(char, (sMap.get(char) || 0) + 1);
    }

    for (let char of t) {
        tMap.set(char, (tMap.get(char) || 0) + 1);
    }

    console.log(sMap);
    console.log(tMap);

    // console.log(sMap.has("c"));
    // console.log(tMap.has("a"));

    for (let char of s){
        if (sMap.has(char) && tMap.has(char)){
            if (sMap.get(char) != tMap.get(char)){
                return false;
            }
        } else{
            return false;
        }
    }
    return true
}

// console.log(isAnagram("cool", "loco"));
// console.log(isAnagram("cool", "aaaa"));



// ==================
// SECOND SOLUTION 
// ==================

// const isAnagram = (s, t) => {
//     let sortedS = s.split('').sort().join('');
//     let sortedT = t.split('').sort().join('');

//     return sortedS == sortedT
// }

// console.log(isAnagram("cool", "loco"));
// console.log(isAnagram("cool", "local"));
