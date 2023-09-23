class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if not self.empty():
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data

    def peek(self):
        if not self.empty():
            node = self.top
            return node.data

    def size(self):
        return self._size

    def empty(self):
        return self.size() == 0

    def plot(self):
        if self.empty():
            return
        node = self.top
        print("topo ->", end=' ')
        while node:
            print(f"{node.data} ->", end=' ') if node.next else print(
                f"{node.data}", end='')
            node = node.next if node.next else None
        print("\n")


def read_input():
    matrix = []
    try:
        while True:
            line = input().strip()
            if not line:
                break
            matrix.append(list(line))
    except EOFError:
        pass
    return matrix


matrix = read_input()


def find_bigest_island(matrix):
    stack = Stack()

    bigest_island = 0
    island_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1':
                matrix[i][j] = "0"
                stack.push((i, j))
                island_count = 0

                while not stack.empty():
                    i_stack, j_stack = stack.pop()
                    island_count += 1

                    is_left_available = j_stack - 1 >= 0

                    is_right_available = j_stack + 1 < len(matrix[i_stack])

                    is_up_available = i_stack - 1 >= 0

                    is_down_available = i_stack + 1 < len(matrix)

                    if is_up_available and matrix[i_stack-1][j_stack] == '1':  # up
                        stack.push((i_stack-1, j_stack))
                        matrix[i_stack-1][j_stack] = "0"

                    # down
                    if is_down_available and matrix[i_stack+1][j_stack] == '1':
                        stack.push((i_stack+1, j_stack))
                        matrix[i_stack+1][j_stack] = "0"

                    # right
                    if is_right_available and matrix[i_stack][j_stack+1] == '1':
                        stack.push((i_stack, j_stack+1))
                        matrix[i_stack][j_stack+1] = "0"

                    # left
                    if is_left_available and matrix[i_stack][j_stack-1] == '1':
                        stack.push((i_stack, j_stack-1))
                        matrix[i_stack][j_stack-1] = "0"

                if island_count > bigest_island:
                    bigest_island = island_count

    return bigest_island


bigest_island = find_bigest_island(matrix)

print(bigest_island)
