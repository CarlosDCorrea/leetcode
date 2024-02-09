from collections import defaultdict


def min_deletion(s: str) -> int:
    ocurrences = defaultdict(int)

    for letter in s:
        ocurrences[letter] += 1

    deletions: int = 0
    is_good_word: bool = False

    ocurrences_values = list(ocurrences.values())
    ocurrences_values.sort(reverse=True)

    print(f'ocurrences_values {ocurrences_values}')

    i = 0
    while not is_good_word and i < len(ocurrences_values) - 1:
        pivot = ocurrences_values[i]
        j = i + 1

        while ocurrences_values[j] == pivot and ocurrences_values[j] != 0:
            ocurrences_values[j] -= 1
            deletions += 1

            if j < len(ocurrences_values) - 1:
                j += 1
            else:
                break

        if i == len(ocurrences_values) - 1:
            is_good_word = True
            break
        i += 1

    return deletions


deletions = min_deletion('bbcebab')
print(deletions)
