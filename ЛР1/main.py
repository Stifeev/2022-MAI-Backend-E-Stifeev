# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:33:17 2022

@author: stife
"""

from cache import LRUCache

#%% Пример 1

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse'))  # вернёт 'James'
cache.rem('Walter')
print(cache.get('Walter')) # вернёт ''

print(cache)

#%% Пример 2

cache = LRUCache(3)

cache.set('A', 'B')
cache.set('C', 'D')
cache.set('E', 'F')

cache.get('A')
cache.get('E')
cache.set('G', 'H') # ('C', 'D') удалится, т.к. у неё самое старое время запроса

print(cache) # capacity = 3, data = {'A': 'B', 'E': 'F', 'G': 'H'}

