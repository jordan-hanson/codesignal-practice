// Given the string, check if it is a palindrome.

// Example

// For inputString = "aabaa", the output should be
// checkPalindrome(inputString) = true;
// For inputString = "abac", the output should be
// checkPalindrome(inputString) = false;
// For inputString = "a", the output should be
// checkPalindrome(inputString) = true.

function checkPalindrome(inputString) {
    const split = inputString.split("")
    const reversed = split.reverse()
    const joined = reversed.join("")
    if (inputString === joined) {
        return true
    } else { return false }
}

checkPalindrome("aabaa")