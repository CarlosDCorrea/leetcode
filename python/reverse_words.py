def reverse_words(s: str) -> str:
    only_reversed_words = [word for word in s.split()[::-1]]
    return " ".join(only_reversed_words)


def reverse_words_better(s: str) -> str:
    words = [bytes(word, "utf-8") for word in s.split()]

    l, r = 0, len(words) - 1

    while l < r:
        words[l] = words[l] ^ words[r]
        words[r] = words[r] ^ words[l]
        words[l] = words[l] ^ words[r]

        l += 1
        r -= 1
    
    return words

test1 = "the sky is blue"
test2 = "  hello world  "
test3 = "a good   example"

print(reverse_words(test2))
print(reverse_words_better(test2))