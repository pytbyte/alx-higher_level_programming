#!/usr/bin/python3

"""
Defines two classes:
1. Node
2. SinglyLinkedList
"""


class Node:
    """
    Class Node: Represents a node in a singly-linked list.
    It has the following attributes and methods:
    """

    def __init__(self, data, next_node=None):
        """
        Class Node: Represents a node in a singly-linked list.
        It has the following attributes and methods:

        Attributes:
        data: Holds the data value of the node.
        next_node: Points to the next node in the list.

        Methods:
        __init__(self, data, next_node=None):
        Initializes a new node with the given data and next_node.

        @property data: Getter method for the data attribute.
        @data.setter: Setter method for the data attribute.
        @property next_node: Getter method for the next_node attribute.
        @next_node.setter: Setter method for the next_node attribute.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Access the Node data private instance attribute.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Sets the value of the accessed private instance attribute.

        Args:
        value - must be of type int.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Access and return the private instance attribute: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the value of next_node if value is of type Node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly-linked list.

    Attributes:
    __head: Points to the head (first node) of the linked list.

    Methods:
    __init__(self):
    Initializes a new singly-linked list with an empty head.

    sorted_insert(self, value):
    Inserts a new node with the given value into the list
    at the correct ordered numerical position.

    __str__(self):
    Returns a string representation of the linked list.
    """

    def __init__(self):
        """
        Initializes a new Singly Linked List and creates attribute head.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into
        the list at the correct ordered numerical position.

        Args:
        value: The new node to be inserted.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp_header = self.__head
            while tmp_header.next_node is not None and tmp_header.next_node.data < value:
                tmp_header = tmp_header.next_node
            new_node.next_node = tmp_header.next_node
            tmp_header.next_node = new_node

    def __str__(self):
        """
        Define the print() representation of a SinglyLinkedList.
        """
        current = self.__head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
