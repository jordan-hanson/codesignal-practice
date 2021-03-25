# For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

# Example

# For n = 1, the output should be
# fibonacciSimpleSum2(n) = true.

# Explanation: 1 = 0 + 1 = F0 + F1.

# For n = 11, the output should be
# fibonacciSimpleSum2(n) = true.

# Explanation: 11 = 3 + 8 = F4 + F6.

# For n = 60, the output should be
# fibonacciSimpleSum2(n) = true.

# Explanation: 60 = 5 + 55 = F5 + F10.

# For n = 66, the output should be
# fibonacciSimpleSum2(n) = false.
def fibonacciSimpleSum2(n):
    numbers = []
    boolean = False
    if n <= 1:
        return True
    else:
        p, c = 0, 1
        sumOf = 0
        for number in range(0, n + 1):
            if sumOf > n:
                break
            sumOf = p + c
            p, c = c, p + c
            numbers.append(sumOf)
        if sumOf > n:
            for x in range(len(numbers)):
                for y in range(x+1, len(numbers), 1):
                    theSum = numbers[x] + numbers[y]
                    if numbers[x] + numbers[y] == n:
                        theSum = numbers[x] + numbers[y]
                        boolean = True
        return boolean