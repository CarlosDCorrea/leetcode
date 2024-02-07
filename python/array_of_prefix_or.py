def find_array(pref: list[int]) -> list[int]:
    n = len(pref)
    prev = pref[0]

    for i in range(1, n):
        pref[i] ^= prev
        prev ^= pref[i]

    return pref


if __name__ == "__main__":
    pref = find_array([5, 2, 0, 3, 1])
    print(pref)
