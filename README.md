# Hard-LoveLocal-
Q 3.Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Explaination:
countDigitOne Function:

This function takes an integer n as input and calculates the total number of occurrences of the digit 1 in all non-negative integers less than or equal to n.
It uses a loop to iterate through each digit place (ones, tens, hundreds, etc.) of the numbers.
Initialization:

count is initialized to 0 to keep track of the total count of digit 1 occurrences.
factor is initialized to 1, representing the current digit place.
While Loop:

The while loop continues until the factor exceeds the value of n.
Inside the loop, the code calculates the quotient and remainder when dividing n by (factor * 10) to determine the contributions of the current digit place to the total count.
The count is updated based on the quotient and remainder calculations.
Factor Update:

factor is multiplied by 10 to move to the next digit place.
User Input:

The code takes user input for the integer n.
Function Call and Print:

The countDigitOne function is called with the user-input value, and the result is printed.
The overall idea is to iterate through each digit place, calculate its contribution to the total count of digit 1 occurrences, and accumulate these contributions to get the final result.
