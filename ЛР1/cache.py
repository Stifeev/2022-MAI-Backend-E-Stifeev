# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:39:31 2022

@author: stife
"""

from time import time_ns

class Node:
    def __init__(self, value, time):
        self.value = value # значение
        self.time = time   # время запроса
        
    def __str__(self):
        return "(%s, %d)" % (self.value, self.time)

class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        """
        Parameters
        ----------
        capacity : int, optional
            DESCRIPTION. Максимальный размер кэша в количестве добавленных значений.
            capacity >= 1. Значение по умолчанию 10.
        """
        self.capacity = capacity
        self.data = {}  # словарь: key = запрос, value - (значение, время запроса)
    
    def get(self, key: str) -> str:
        if key in self.data:
            self.data[key].time = time_ns()
            return self.data[key].value
        else:
            return ""

    def set(self, key: str, value: str) -> None:
        if key in self.data:
            self.data[key] = Node(value, time_ns())
        else:
            if len(self.data) + 1 > self.capacity: # проверка на переполнение
                # удаляем последнее значение (в порядке добавление)
                skey = None
                smin = time_ns()
                for _key, val in self.data.items(): # поиск минимума за линию
                    time = val.time
                    if time <= smin:
                        smin = time
                        skey = _key
                del self.data[skey]
                    
            self.data[key] = Node(value, time_ns())
            
    def rem(self, key: str) -> None:
        if key in self.data:
            del self.data[key]
        