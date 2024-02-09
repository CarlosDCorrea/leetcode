from typing import List


word1 = 'abc'
word2 = 'pqrsss'


def merge_alternately(word1: str, word2: str) -> List[str]:
    output: List[str] = []

    i = 0

    while i < len(word1) and i < len(word2):
        output.append(word1[i])
        output.append(word2[i])

        i += 1

    output.append(word1[i:])
    output.append(word2[i:])
    return "".join(output)


print(merge_alternately(word1, word2))
