class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression_list = [int(x) for x in re.findall('[+-]?\d+', expression)]

        denominator = math.lcm(*expression_list[1::2])
        numerator = sum([denominator // expression_list[i+1] * expression_list[i] for i in range(0, len(expression_list), 2)])

        gcd = math.gcd(numerator, denominator)
        if gcd != 1:
            numerator //= gcd
            denominator //= gcd

        return f'{numerator}/{denominator}'