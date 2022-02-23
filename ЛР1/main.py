# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:33:17 2022

@author: stife
"""

from cache import LRUCache
from time import sleep

#%% Пример 1

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse'))  # вернёт 'James'
cache.rem('Walter')
print(cache.get('Walter')) # вернёт ''

print("capacity = %d" % cache.capacity)
print(["%s : %s" % (key, str(val)) for key, val in cache.data.items()])

#%% Пример 2

cache = LRUCache(3)

cache.set('A', 'B')
cache.set('C', 'D')
cache.set('E', 'F')

sleep(0.5)

cache.get('A')
cache.get('E')
cache.set('G', 'H') # ('C', 'D') удалится, т.к. у неё самое старое время запроса

print("capacity = %d" % cache.capacity)
print(["%s : %s" % (key, str(val)) for key, val in cache.data.items()])
