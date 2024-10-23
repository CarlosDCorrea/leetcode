from collections import defaultdict


def main(arr):
    # get the list with less elements in it
    shorter = min(arr, key=len)
    larger = max(arr, key=len)
    results = []

    numbers = defaultdict(int)
    shorter_list = shorter.split(", ")
    larger_list = larger.split(", ")

    for number in larger_list:
        if number in shorter_list:
            results.append(number)

    return ",".join(results)

test1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
test2 = ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]

print(main(test2))