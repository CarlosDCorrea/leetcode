class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def presedence(op):
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            num = ""

            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            
            output.append(num)
            continue
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and presedence(stack[-1]) >= presedence(char):
                output.append(stack.pop())
            stack.append(char)
        
        i += 1

    while stack:
        output.append(stack.pop())

    return output


def build_expression_tree(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            node = Node(int(char))
            stack.append(node)
        else:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack[-1]


def inorder(node):
    stack = []
    root = node

    while True:
        while root:
            if root.left:
                stack.append(root)
                root = root.left
                continue
            
            print(root.value)

            if stack:
                root = stack.pop()
                print(root.value)

                if root.right:
                    root = root.right
            else:
                root = None
        if not stack:
            break


def evaluate_unrecursive(node):
    if not node:
        return 0

    stack = []
    root = node
    value = 0

    values = []

    while True:
        while root:
            if root.right:
                stack.append(root.right)

            stack.append(root)
            root = root.left
        
        root = stack.pop()

        if stack and root.right and stack[-1] == root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            if isinstance(root.value, int):
                values.append(root.value)
            else:
                right_value = values.pop()
                left_value = values.pop()

                if root.value == "+":
                    values.append(left_value + right_value)
                elif root.value == "-":
                    values.append(left_value - right_value)
                elif root.value == "*":
                    values.append(left_value * right_value)
                elif root.value == "/":
                    values.append(left_value // right_value)

            root = None
        
        if not stack:
            break

    return values[-1]


def evaluate(node):
    if node.left is None and node.right is None:
        return node.value
    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    if node.value == "+":
        return left_value + right_value
    if node.value == "-":
        return left_value - right_value
    if node.value == "*":
        return left_value * right_value
    if node.value == "/":
        return left_value // right_value
# test cases

test1 = "3+5*2"
test2 = "6*(4/2)+3*1"
test3 = "10-2/2"
test4 = "2*5+6/3"



def calculator(expression):
    postfix = infix_to_postfix(expression)
    root = build_expression_tree(postfix)

    print(postfix)

    #evaluate(root)
    #print(f"postfix", postfix)
    #inorder(root)
    #print("=============================")
    return evaluate_unrecursive(root)


print(calculator(test2))
