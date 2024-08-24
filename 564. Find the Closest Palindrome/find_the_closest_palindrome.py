class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == "1":
            return "0"

        m = len(n)
        front = n[:(m+1)//2]
        palindromes = set()

        for i in range(-1, 2):
            front2 = str(int(front) + i)
            if m % 2 == 0:
                palindrome = front2 + front2[::-1]
            else:
                palindrome = front2 + front2[:-1][::-1]
            if palindrome != n:
                palindromes.add(palindrome)

        palindromes.add(str(10**m + 1))
        palindromes.add(str(10**(m-1) - 1))

        closest_palindrome = min(palindromes, key=lambda p: (abs(int(p) - int(n)), int(p)))

        return closest_palindrome