import math


def greates_common_divisor_of_strings(s1: str, s2: str) -> str:
    gcd = math.gcd(len(str1), len(str2))

    repeat_str1 = len(str1) // gcd
    repeat_str2 = len(str2) // gcd

    gcds = str1[:gcd]

    if str1 == gcds * repeat_str1 and str2 == gcds * repeat_str2:
        return gcds

    return ''


str1 = 'ABCDEF'
str2 = 'ABC'

# ABCDEFABC

print(greates_common_divisor_of_strings(str1, str2))

""" result = greates_common_divisor_of_strings(a, b)
print(result) """

# RESEARCH Why does this works? what is the scope of a and b?
"""
def greates_common_divisor_of_strings(s1: str, s2: str) -> str:
    gcd = math.gcd(a, b)

    if s1[:gcd] == s2[:gcd]:
        return s1[:gcd]

    return ''


a = 6
b = 4

print(greates_common_divisor_of_strings(a, b))"""
