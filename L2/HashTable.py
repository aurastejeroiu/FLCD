# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 08:35:36 2022

@author: Stejeroiu Aura
"""
class Position:
    def __init__(self, position_in_table=None, position_in_list=None):
        self.position_in_table = position_in_table
        self.position_in_list = position_in_list

    def __str__(self):
        return " position in table: " + str(self.position_in_table) +\
               " position in list: " + str(self.position_in_list)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return 0

        current_node = self.head
        position = 1
        while current_node.next is not None:
            current_node = current_node.next
            position += 1
        current_node.next = node

        return position

    def get_position(self, value):
        position = 0
        current = self.head
        while current is not None:
            if current.data == value:
                return position
            position += 1
            current = current.next
        return -1


class HashTable:
    def __init__(self):
        self.size = 4
        self.alpha = 0
        self.table = [LinkedList() for _ in range(self.size)]

    def hash(self, value):
        if type(value) == int:
            return value % self.size
        return self.hash_string(value)

    def hash_string(self, value):
        hash_value = 0
        index = 1
        for i in value:
            hash_value += index * ord(i)
            index += 1
        return hash_value % self.size

    def add(self, value):
        position_in_table = self.hash(value)
        print(position_in_table)
        position_in_list = self.table[position_in_table].add(value)
        return Position(position_in_table, position_in_list)

    def get_position(self, value):
        position_in_table = self.hash(value)
        position_in_list = self.table[position_in_table].get_position(value)
        if position_in_list != -1:
            return Position(position_in_table, position_in_list)
        return None
