from typing import Optional, DefaultDict, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_tree(node: Optional[TreeNode], values_maped: DefaultDict[int, int]) -> None:
    if not node:
        return values_maped

    traverse_tree(node.left, values_maped)
    values_maped[node.val] += 1
    traverse_tree(node.right, values_maped)


def findMode(root: Optional[TreeNode]) -> List[int]:
    maped_values = defaultdict(int)
    traverse_tree(root, maped_values)

    key_values: List[int] = maped_values.keys()
    values: List[int] = maped_values.values()

    result = [mode for mode in key_values if maped_values[mode] == max(values)]
    return result


root = TreeNode(1)

node_2 = TreeNode(2)
node_3 = TreeNode(2)

root.right = node_2
node_2.left = node_3

findMode(root)
