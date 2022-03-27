# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:39:31 2022

@author: stife
"""

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
        self.data = {}  # словарь: key = запрос, value - значение
    
    def get(self, key: str) -> str:
        if key in self.data:
            val = self.data[key][:]
            del self.data[key]
            self.data[key] = val
            return val
        else:
            return ""

    def set(self, key: str, value: str) -> None:
        if key in self.data: # уже есть
            del self.data[key]
            self.data[key] = value
        else:
            if len(self.data) + 1 > self.capacity: # проверка на переполнение
                # удаляем последнее значение (в порядке добавление)
                del self.data[next(iter(self.data.keys()))]
            self.data[key] = value
            
    def rem(self, key: str) -> None:
        if key in self.data:
            del self.data[key]
            
    def __str__(self):
        return "capacity = %d, data = %s" % (self.capacity, self.data)
        
