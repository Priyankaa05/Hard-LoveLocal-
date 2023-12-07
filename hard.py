def countDigitOne(n):
    count = 0
    factor = 1

    while factor <= n:
        quotient = n // (factor * 10)
        remainder = n % (factor * 10)
        count += quotient * factor + min(max(remainder - factor + 1, 0), factor)

        factor *= 10

    return count

user_input = int(input("Enter an integer (n): "))


result = countDigitOne(user_input)
print("Total number of digit 1 appearing in all numbers up to", user_input, "is:", result)
