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

    def insert(self, element, index):
        """insert element at a given index
        """
        if index < 0 or index > self._size:
            raise Exception("Index out of range")

        if index == 0:
            # as first node
            new_node = self._Node(element)
            new_node._next = self._head
            self._nodes.append(new_node)
            self._head = new_node
            self._size += 1
        else:
            # in between two nodes
            node = self._head
            for i in range(index-1):
                node = node._next
            next_node = node._next
            new_node = self._Node(element)
            node._next = new_node
            new_node._next = next_node
            self._nodes.append(new_node)
            self._size += 1

    def remove(self, element):
        """remove a given element from the linked list"""
        if self._size == 0:
            raise Exception("No elements in the linked list")

        node = self._head
        element_found = False
        if node._element == element:
            temp_node = node
            self._head = self._head._next
            element_found = True
        else:
            for i in range(self._size-1):
                prev_node = node
                node = node._next
                if node._element == element:
                    temp_node = node
                    prev_node._next = node._next
                    element_found = True
                    break
        if element_found:
            # removed node is still in the list of nodes, remove it
            self._nodes.remove(temp_node)
            self._size -= 1
            return True
        else:
            print ("Element not found in the linked list")
            return False

if __name__ == "__main__":
    my_linked_list = SinglyLinked()
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 1 at index: 0")
    my_linked_list.insert(1,0)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 2 at index: 0")
    my_linked_list.insert(2,0)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 3 at index: 0")
    my_linked_list.insert(3,0)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 4 at index: 3")
    my_linked_list.insert(4,3)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 5 at index: 3")
    my_linked_list.insert(5,3)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\nremoving val: 5")
    my_linked_list.remove(5)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

    print ("\ninserting val: 5 at index: 2")
    my_linked_list.insert(5,2)
    print("len(my_linked_list) = ", len(my_linked_list))
    print("my_linked_list = ", repr(my_linked_list))
    print("my_linked_list.is_empty() ? = ", my_linked_list.is_empty())

