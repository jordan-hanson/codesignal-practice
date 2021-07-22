// Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

// Example

// For year = 1905, the output should be
// centuryFromYear(year) = 20;
// For year = 1700, the output should be
// centuryFromYear(year) = 17.

function centuryFromYear(year) {
    // year one: 1-100
    // year two: 101-200 etc...
    //  if year = 1905 result = 20
    // if year = 1700 result = 17.
    // return the century

    // The last two digits control the change 00->01. 
    // first two digits are what century based upon the change.

    test = (year).toString(10).split("").map(number => parseInt(number, 10))
    console.log("whole number split", test)

    const firstNumbers = parseInt(test.slice(0, test.length - 2).join(""), 10)
    console.log("sliced numbers before the last two digits", firstNumbers)

    const secondDigit = test.slice(-2)
    console.log("secondDigit", secondDigit)

    if (test.length < 3) {
        return 1
    }
    if (secondDigit[1] == 0 && secondDigit[0] == 0) {
        return firstNumbers
    }
    if (secondDigit[0] == 0 && secondDigit[1] > 0) {
        return firstNumbers + 1
    }
    if (secondDigit[0] > 0 && secondDigit[1] > 0) {
        return firstNumbers + 1
    }
}
centuryFromYear(1905)