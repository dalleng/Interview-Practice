class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        int_extracted = ""
        state = "start"

        for char in s:
            if state == "start":
                if char.isdigit():
                    int_extracted += char
                    state = "digit"
                elif char in "+-":
                    int_extracted += char
                    state = "digit_or_sign"
                else:
                    break
            elif state == "digit":
                if char.isdigit():
                    int_extracted += char
                else:
                    break
            elif state == "digit_or_sign":
                if char in "+-":
                    int_extracted += char
                elif char.isdigit():
                    state = "digit"
                    int_extracted += char
                else:
                    break

        try:
            ret_value = int(int_extracted)
        except ValueError:
            ret_value = 0

        if ret_value > 0:
            ret_value = min(ret_value, 2**31 - 1)

        if ret_value < 0:
            ret_value = max(ret_value, -(2**31))

        return ret_value


if __name__ == "__main__":
    s = Solution()
    # print(s.myAtoi("456"))
    # print(s.myAtoi("-456"))
    print(s.myAtoi("-+456"))
