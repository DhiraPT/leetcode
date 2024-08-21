class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        num_dict = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
            80: "Eighty", 90: "Ninety"
        }

        def below_thousand(num: int) -> str:
            res = ""
            if num >= 100:
                res += num_dict[num//100] + " Hundred"
                num %= 100
                if num > 0:
                    res += " "
            if num >= 20:
                res += num_dict[num//10*10]
                num %= 10
                if num > 0:
                    res += " " + num_dict[num]
            elif num > 0:
                res += num_dict[num]
            return res

        res = ""
        if num >= 1_000_000_000:
            res += below_thousand(num//1_000_000_000) + " Billion "
            num %= 1_000_000_000
        if num >= 1_000_000:
            res += below_thousand(num//1_000_000) + " Million "
            num %= 1_000_000
        if num >= 1000:
            res += below_thousand(num//1000) + " Thousand "
            num %= 1000
        res += below_thousand(num)

        return res.strip()