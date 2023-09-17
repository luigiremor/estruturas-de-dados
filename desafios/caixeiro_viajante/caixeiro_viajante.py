import math


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x, y):
        if not self.head:
            self.head = Node(x, y)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(x, y)

    def distance(self, node1, node2):
        return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

    def total_distance(self):
        current = self.head
        distance = 0
        while current.next:
            distance += self.distance(current, current.next)
            current = current.next

        distance += self.distance(current, self.head)
        return distance

    def swap_adjacent_nodes(self, prev):

        first = prev.next if prev else self.head

        if not first:
            return

        second = first.next if first else None

        if not second:
            # Swap last with first condition
            second = self.head
            prev.next = second
            first.next = second.next
            second.next = None
            self.head = first
            return

        # Regular swap
        first.next = second.next
        second.next = first
        if prev:
            prev.next = second
        else:
            self.head = second

    def improve(self):
        improvement_made = True
        while improvement_made:
            improvement_made = False
            prev = None
            current = self.head
            while current:
                # defines distances
                original_distance = self.total_distance()
                self.swap_adjacent_nodes(prev)
                new_distance = self.total_distance()

                # compares distances
                if new_distance < original_distance:
                    improvement_made = True
                else:
                    self.swap_adjacent_nodes(prev)

                current = current.next

                # Defines prev
                if prev:
                    prev = prev.next
                else:
                    # first with second
                    prev = self.head


def main(input_data):
    cities = LinkedList()

    for line in input_data:
        x, y = map(int, line.split())
        if x == -1 and y == -1:
            break
        cities.append(x, y)

    original_cost = cities.total_distance()
    cities.improve()
    improved_cost = cities.total_distance()

    return "{:.2f}".format(original_cost), "{:.2f}".format(improved_cost)
