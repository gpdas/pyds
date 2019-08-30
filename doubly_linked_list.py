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
            for i in range(self._size - index):
                node = node._prev
        return node._element

    def insert(self, element, index):
        """insert and element at a given index
        """
        if index < 0 or index > self._size:
            raise Exception("index out of range")

        if index <= self._size / 2:
            # first half
            prev_node = self._header
            for i in range(index):
                prev_node = prev_node._next
        else:
            # second half
            prev_node = self._trailer
            for i in range(self._size - index + 1):
                prev_node = prev_node._prev

        next_node = prev_node._next
        new_node = self._Node(element)
        new_node._next = next_node
        next_node._prev = new_node
        new_node._prev = prev_node
        prev_node._next = new_node

        self._nodes.append(new_node)
        self._size += 1

    def remove(self, element):
        """remove a given element from the linked list"""
        if self._size == 0:
            raise Exception("No elements in the linked list")

        element_found = False
        curr_node = self._header
        for i in range(self._size-1):
            curr_node = curr_node._next
            if curr_node._element == element:
                element_found = True
                break

        if element_found:
            prev_node = curr_node._prev
            next_node = curr_node._next
            prev_node._next = next_node
            next_node._prev = prev_node
            # unlinked node is still in the list of nodes, remove it
            self._nodes.remove(curr_node)
            self._size -= 1
            return True
        else:
            print ("Element not found in the linked list")
            return False

if __name__ == "__main__":
    my_linked_list = DoublyLinked()
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 1 at index 0")
    my_linked_list.insert(1, 0)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 2 at index 0")
    my_linked_list.insert(2, 0)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 3 at index 0")
    my_linked_list.insert(3, 0)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 4 at index 0")
    my_linked_list.insert(4, 0)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 5 at index 2")
    my_linked_list.insert(5, 2)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 6 at index 4")
    my_linked_list.insert(6, 4)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\nremoving val: 6")
    my_linked_list.remove(6)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\nremoving val: 4")
    my_linked_list.remove(4)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())
