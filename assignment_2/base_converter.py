import string
from math import floor

class base_converter:
    def toBase62(num, b=62):
        if b <= 0 or b > 62:
            return 0
        base = string.digits + string.ascii_letters
        r = num % b
        res = base[r]
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    def toBase10(string, alphabet=(string.digits + string.ascii_letters)):
        base = len(alphabet)
        strlen = len(string)
        num = 0
        idx = 0
        for char in string:
            if char not in alphabet:
                return None
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1
        return num