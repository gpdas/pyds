#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Day Mon dd HH:MM:SS YYYY

@author: xxxxx
"""

class DoublyLinked(object):
    """doubly linked list class definition with sentinel end nodes
    """
    class _Node(object):
        """an internal node class
        """
        __slots__ = "_element", "_next", "_prev"

        def __init__(self, element):
            """create a node with the given element
            """
            self._element = element
            self._prev = None
            self._next = None

    def __init__(self):
        """create a linked list object
        """
        self._nodes = []
        self._header = self._Node(None)
        self._trailer = self._Node(None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
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
        node = self._header._next
        for i in range(self._size):
            items.append(node._element)
            node = node._next
        return str(items)

    def __getitem__(self, index):
        """get the element at a given index. raises error if index
        is more than len(object) - 1
        """
        if index < 0 or index >= self._size:
            raise Exception("Index out of range")

        if index < self._size / 2:
            # access frontend elements
            node = self._header
            for i in range(index+1):
                node = node._next
        else:
            # access backend elements
            node = self._trailer
            for i in range(index+1):
                node = node._prev
        return node._element

if __name__ == "__main__":
    my_linked_list = DoublyLinked()
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_emty() ? = ", my_linked_list.is_empty())