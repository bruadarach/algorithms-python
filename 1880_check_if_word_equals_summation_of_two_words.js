/*

The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.
For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

 
Example 1:

Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.


Example 2:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.


Example 3:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
 

Constraints:

1 <= firstWord.length, secondWord.length, targetWord.length <= 8
firstWord, secondWord, and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.

*/


/**
 * @param {string} firstWord
 * @param {string} secondWord
 * @param {string} targetWord
 * @return {boolean}
 */
var isSumEqual = function(firstWord, secondWord, targetWord) {
    let obj = {
        'a': '0',
        "b": '1',
        "c": '2',
        "d": '3',
        "e": '4',
        'f': '5',
        'g': '6',
        'h': '7',
        'i': '8',
        "j": '9'
    };

    let words = [firstWord, secondWord, targetWord];
    let newWord = '';
    let result = [];

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words[i].length; j++) {
            let char = words[i][j];
            if (char in obj) {
                newWord = newWord.concat(obj[char]);
            }
        }
        result.push(newWord);
        newWord = '';
    }
    return Number(result[0]) + Number(result[1]) === Number(result[2]);
}

// (runtime / memory)
//  68 ms / 38.5 MB



/**
 * @param {string} firstWord
 * @param {string} secondWord
 * @param {string} targetWord
 * @return {boolean}
 */
var isSumEqual = function(firstWord, secondWord, targetWord) {
    let obj = {
        'a': '0',
        "b": '1',
        "c": '2',
        "d": '3',
        "e": '4',
        'f': '5',
        'g': '6',
        'h': '7',
        'i': '8',
        "j": '9'
    };

    let words = [firstWord, secondWord, targetWord];
    let newWord = '';
    let result = [];

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words[i].length; j++) {
            let char = words[i][j];
            if (char in obj) {
                newWord = newWord.concat(obj[char]);
            }
        }
        result.push(newWord)
        newWord = '';
    }
    console.log(result)
    return parseInt(result[0]) + parseInt(result[1]) === parseInt(result[2]);
}

// (runtime / memory)
//  80 ms / 39.1 MB