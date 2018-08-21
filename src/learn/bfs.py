#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/21/2018 4:53 PM
"""

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}


def bfs_connected_component(graph, start):
    explored = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return explored


def bfs_short_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return "OK"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            explored.append(node)
    return 'Sorry'


# ref https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/

if __name__ == "__main__":
    print(bfs_connected_component(graph, 'A'))
    print(bfs_short_path(graph, 'D', 'A'))
    print("hello imp")
