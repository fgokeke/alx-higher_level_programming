#!/usr/bin/python3
"""Creation of a Singly Linked List."""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """To initialize a node of a singly linked list

        Args:
            data (int): data for the new node.
            next_node (Node): next node to the new node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """to retrieve the data part of a node."""
        return (self.__data)
    @data.setter
    def data(self, value):
        """to set the value of the data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """to retrieve the next_node"""
        return (self.__next_node)
    @next_node.setter
    def next_node(self, value):
        """to set the value of the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """To initialize a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """To insert a new Node in the SinglyLinkedList
        in an increasing order.
        
        Args:
            value(Node): node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while(tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """the print() representation of a SinglyLinkedList"""
        list_values = []
        tmp = self.__head
        while tmp is not None:
            list_values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(list_values))
