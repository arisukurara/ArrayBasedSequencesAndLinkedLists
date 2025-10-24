from singly_linked_list import *

class SplitEvensOdds(SinglyLinkedList):
    def split_evens_odds(self):
        if self._SinglyLinkedList__head is None:
            raise SinglyLinkedList.EmptyListException()

        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()

        current = self._SinglyLinkedList__head

        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0

        while current:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                if even_list._SinglyLinkedList__tail is None:
                    even_list._SinglyLinkedList__head = current
                    even_list._SinglyLinkedList__tail = current
                else:
                    even_list._SinglyLinkedList__tail.next = current
                    even_list._SinglyLinkedList__tail = current
                even_list._SinglyLinkedList__count += 1
            else:
                if odd_list._SinglyLinkedList__tail is None:
                    odd_list._SinglyLinkedList__head = current
                    odd_list._SinglyLinkedList__tail = current
                else:
                    odd_list._SinglyLinkedList__tail.next = current
                    odd_list._SinglyLinkedList__tail = current
                odd_list._SinglyLinkedList__count += 1

            current = next_node

        return even_list, odd_list