class Node:

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right: Node = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left: Node = node

    def children(self):
        left_node = self._left if self._left else None
        right_node = self._right if self._right else None
        return left_node, right_node


class BinaryExpressionTree:

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root: Node):
        self._root = root

    def add_left(self, parent: Node, left_node: Node):
        parent.left = left_node

    def add_right(self, parent: Node, right_node: Node):
        parent.right = right_node


# pós-ordem (left, right, root)
# pré-ordem (root, left, right)
# ordem (left, root, right)

expression = "A*B+C*D-E"

"""
Percorre a lista de trás para frente

Fica com o primeiro valor de menor prioridade

Chama a função para os dois lados de forma recursiva
    Se o tamanho for 1, retorna ela
    Se o tamanho for maior que 2, chama a função para a expressão
"""

expression_tree = BinaryExpressionTree()

priority_table = {
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
}


def priority(key):
    return priority_table[key] if key in priority_table.keys() else 3


"""
min_priority_index = 0
for i in range(len(expression)-2, -1, -1):
    if priority(expression[i]) < priority(expression[min_priority_index]):
        min_priority_index = i


root = Node(expression[min_priority_index])
expression_tree.root = root

left_array = expression[:min_priority_index]  # left side
right_array = expression[min_priority_index+1:]  # right side
"""


def percurse(exp):
    if len(exp) == 1:
        return exp

    min_priority_index = 0
    for i in range(len(exp)-2, -1, -1):
        if priority(exp[i]) < priority(exp[min_priority_index]):
            min_priority_index = i

    print(exp[min_priority_index])
    percurse(exp[:min_priority_index])
    percurse(exp[min_priority_index+1:])


print(percurse(expression))
