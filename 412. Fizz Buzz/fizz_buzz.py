class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            match i % 15:
                case 0:
                    ans.append("FizzBuzz")
                case 3:
                    ans.append("Fizz")
                case 5:
                    ans.append("Buzz")
                case 6:
                    ans.append("Fizz")
                case 9:
                    ans.append("Fizz")
                case 10:
                    ans.append("Buzz")
                case 12:
                    ans.append("Fizz")
                case _:
                    ans.append(str(i))
        return ans