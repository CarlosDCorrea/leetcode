from typing import List


word1 = 'abc'
word2 = 'pqrsss'


def merge_alternately(word1: str, word2: str) -> List[str]:
    output: List[str] = []
    offset: int = 0
    exced: List[str] = []

    if len(word1) > len(word2):
        offset = len(word2)
        exced = [l for l in word1[offset:]]
    elif len(word1) < len(word2):
        offset = len(word1)
        exced = [l for l in word2[offset:]]

    for l1, l2 in zip(word1, word2):
        output.extend([l1, l2])

    if exced:
        output.extend(exced)

    return "".join(output)


merge_alternately(word1, word2)
