#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Day Mon dd HH:MM:SS YYYY

@author: xxxxx
"""

class SinglyLinkedQueue(object):
    """queue (FIFO) using a singly linked list with a header sentinel
    """
    class _Node(object):
        """an internal node class
        """
        __slot__ = "_element", "_next"

        def __init__(self, element):
            self._element = element
            self._next = None

    def __init__(self):
        """create singly linked queue object
        """
        self._header = self._Node(None)
        self._size = 0
        self._nodes = []

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
        node = self._header
        for i in range(self._size):
            node = node._next
            print (node)
            items.append(node._element)
        return str(items)

    def push(self, element):
        """push an element
        """
        # complete this method
        pass

    def pop(self):
        """pop an element
        """
        # complete this method
        pass

if __name__ == "__main__":
    my_queue = SinglyLinkedQueue()
    print("len(my_queue) = ", len(my_queue))
    print("my_queue = ", repr(my_queue))
    print("my_queue.is_empty() ? = ", my_queue.is_empty())