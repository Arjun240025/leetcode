class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            total=0
            while n>0:
                digit=n%10
                total+=digit*digit
                n=n//10
            n=total
        return True

# 1. seen = set() – Creates an empty set to store numbers that we have already visited.

# 2. while n != 1 – Keeps repeating the calculation until the number becomes 1.

# 3. if n in seen – Checks whether the current number has already appeared. If it has, the process is repeating in a cycle.

# 4. return False – Stops the function and returns False because the number will never reach 1.

# 5. seen.add(n) – Stores the current number in the set so we can detect it if it appears again.

# 6. total = 0 – Initializes a variable to store the sum of the squares of all digits.

# 7. while n > 0 – Runs until all the digits of the number have been extracted.

# 8. digit = n % 10 – Extracts the last digit from the number.

# 9. total += digit * digit – Squares the extracted digit and adds it to the total.

# 10. n = n // 10 – Removes the last digit from the number so we can process the next digit.

# 11. n = total – Replaces the original number with the calculated sum and starts the process again.

# 12. return True – If the number becomes 1, it is a happy number.