#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Day Mon dd HH:MM:SS YYYY

@author: xxxxx
"""

class SinglyLinked(object):
    """singly linked list class definition
    """
    class _Node(object):
        """an internal node class
        """
        __slots__ = "_element", "_next"

        def __init__(self, element):
            """create a node with the given element
            """
            self._element = element
            self._next = None

    def __init__(self):
        """create a linked list object
        """
        self._nodes = []
        self._head = None
        self._size = 0

    def __len__(self):
        """return length of the linked list object
        """
        return self._size

    def is_empty(self):
        """return True if the linked list object is empty
        """
        return self._size == 0

    def __repr__(self):
        """return the string representation of the linked list object
        """
        items = []
        for i in range(self._size):
            if i == 0:
                node = self._head
            items.append(node._element)
            node = node._next
        return str(items)

    def __getitem__(self, index):
        """get the element at a given index. raises error if index
        is more than len(object) - 1
        """
        if index < 0 or index >= self._size:
            raise Exception("Index out of range")
        node = self._head
        for i in range(index):
            node = node._next
        return node._element

if __name__ == "__main__":
    my_linked_list = SinglyLinked()
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_emty() ? = ", my_linked_list.is_empty())