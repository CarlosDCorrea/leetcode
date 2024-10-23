import re


def main(strParam):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{2,23}[^_]$"
    matches = re.match(pattern, strParam)
    return "true" if matches else "false"


test1 = "aa_"
test2 = "u__hello_world123_"

print(main(test2))