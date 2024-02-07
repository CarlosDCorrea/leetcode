from typing import Optional, List, DefaultDict
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    curr: TreeNode = root
    maped_values: DefaultDict[int, int] = defaultdict(int)
    stack: List[TreeNode] = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        maped_values[curr.val] += 1
        curr = curr.right

    return maped_values


root = TreeNode(1)
node_1 = TreeNode(2)
node_2 = TreeNode(2)

root.right = node_1
node_1.left = node_2

print(findMode(root))
