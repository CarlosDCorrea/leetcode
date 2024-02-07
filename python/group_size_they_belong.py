from typing import List
# from collections import defaultdict


def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    """ groups: DefaultDict[int, List[int]] = defaultdict(list)
    output: List[List[int]] = []

    for i, group_size in enumerate(groupSizes):
        groups[group_size].append(i)

        if len(groups[group_size]) == group_size:
            output.append(groups[group_size])
            groups[group_size] = []

    return output """

    groupSizes = [x for x in enumerate(groupSizes)]
    groupSizes.sort(key=lambda x: x[1])

    output = []

    while len(groupSizes) > 0:
        output.append([x[0] for x in groupSizes[0: groupSizes[0][1]]])
        del groupSizes[0: groupSizes[0][1]]

    return output


input_data: List[int] = [3, 3, 3, 3, 3, 1, 3]

output = groupThePeople(input_data)
print(output)
