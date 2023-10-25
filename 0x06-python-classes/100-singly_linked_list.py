#!/usr/bin/python3

"""A module defining Classes for a singly linked list"""


class Node:
    """ A class that defines a Node"""

    def __init__(self, data, next_node=None):
        """Initialize a new node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieve the data of the node"""

        return self.__data

    @data.setter
    def data(self, value):
        """ Change the data of the node"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieve the next node of the linked list"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node to the current node"""

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""

    def __init__(self):
        """" Initialize the singly linked list with a head node"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node in the list"""

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """ A method to define a printaple representation of the list"""

        values = []
        tmp = self.__head

        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
