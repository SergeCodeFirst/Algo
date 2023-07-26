// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
// typically using all the original letters exactly once.


// Example
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Input: strs = [""]
// Output: [[""]]

// Input: strs = ["a"]
// Output: [["a"]]



const isAnagram = (str1, str2) =>{
    newMap = new Map();
    secondMap = new Map();
    
    if(str1.length != str2.length){
        return false;
    }

    for(let char of str1){
        newMap.set(char, (newMap.get(char) || 0) + 1)
    }

    for(let char of str2){
        secondMap.set(char, (secondMap.get(char) || 0) + 1)
    }

    for(let char of str2){
        if(newMap.get(char) !== secondMap.get(char)){
            return false
        } 
    }

    return true
}


const groupAnagrams = (arrStr) => {
    // write a function that return true when it's an anagram
    // create a nested for loop that will use the function and add the same anagram into a temp array 
    mainArr = []

    for (let i=0; i<arrStr.length; i++){
        tempArr = []

        if (tempArr.length == 0){
            tempArr.push(arrStr[i]);
        }
        
        if (i + 1){
            for(let j=i+1; j<arrStr.length; j++){
                if(isAnagram(arrStr[i], arrStr[j])){
                    tempArr.push(arrStr[j]);
                    arrStr.splice(j, 1);
                }
            }
        }
        mainArr.push(tempArr);
    }

    return mainArr
}


// console.log(isAnagram("", ""));
// console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"])); // [["bat"],["nat","tan"],["ate","eat","tea"]]
console.log(groupAnagrams(["","",""]));
