class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        curr_char = ''
        count = 0
        j = 0

        for c in chars:
            if c != curr_char:
                curr_char = c
                if count > 1:
                    count_str = str(count)
                    chars[j:j+len(count_str)] = list(count_str)
                    j += len(count_str)
                chars[j] = curr_char
                j += 1
                count = 1
            else:
                count += 1

        if count > 1:
            count_str = str(count)
            chars[j:j+len(count_str)] = list(count_str)
            j += len(count_str)

        return j