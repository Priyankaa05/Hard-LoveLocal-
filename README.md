# Hard-LoveLocal-
Q 3.Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Explaination:

Logic:
Function Definition:

The function count_digit_one(n) takes an integer n as input.
Initialization:

The variable count is initialized to 0. This variable will be used to keep track of the total count of digit '1'.
Loop through Numbers:

The for loop iterates through numbers from 1 to n (inclusive).
Counting '1's in Each Number:

For each number i, its decimal representation is converted to a string (str(i)) and then the count() method is used to count the occurrences of the digit '1'.
Accumulate Counts:

The count of '1's for each number is added to the overall count.
Return Result:

The total count of digit '1' in the decimal representation of numbers from 1 to n is returned.
User Input and Output:

The user is prompted to enter a number (n), and the result of count_digit_one(n) is printed.
Example:
Let's say the user enters n = 12.

For numbers from 1 to 12, the counts of '1's are as follows:

1: 1 time
2: 1 time
3: 1 time
4: 1 time
5: 1 time
6: 1 time
7: 1 time
8: 1 time
9: 1 time
10: 1 time
11: 2 times
12: 2 times
The total count is 14, so the code would output 14.

Time Complexity:
The time complexity of this code is O(n log n), where n is the input number. This is because, in the worst case, the decimal representation of each number from 1 to n has about log10(n) digits, and for each digit, we perform constant time operations. The loop runs n times.







