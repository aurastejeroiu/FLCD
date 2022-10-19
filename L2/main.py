# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 08:39:07 2022

@author: Stejeroiu Aura
"""

from HashTable import HashTable


def main():
    symbol_table = HashTable()
    print(symbol_table.add(1))
    print(symbol_table.add(2))
    print(symbol_table.add(3))
    print(symbol_table.add(2))
    print(symbol_table.add(3))
    print(symbol_table.add(1))
    print(symbol_table.add(3))
    print(symbol_table.add(1))
    print(symbol_table.add(2))


main()