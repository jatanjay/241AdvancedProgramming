"""
BFS helper :
"""


class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node == None:  # Removed last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None:  # Removed tail
                self.tail = current_node


#
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# def shortest_path(self, artist_name):
#     path = {}
#     level = 0
#     vertQueue = Queue()
#     vertQueue.enqueue(self.g.getVertex(artist_name))
#     last = vertQueue.items[0]  # keeping track of the last element
#     while (vertQueue.size() > 0):
#         currentVert = vertQueue.dequeue()
#         path[currentVert.id] = level  # adding the element getting dequeued and it's level into path dictionary
#         if last == currentVert:  # checking if last one that got enqueued is the one that got dequeued
#             level += 1  # and if yes, then incrementing the level
#
#         for nbr in self.g.vertList[currentVert.id].coArtists:
#             if nbr.artist not in path.keys() and nbr not in vertQueue.items:
#                 vertQueue.enqueue(
#                     nbr)  # adding vertexes of the co artists to the queue if already is not added previously
#         if vertQueue.items and currentVert == last:
#             last = vertQueue.items[0]  # defining the last element which got enqueued
#
#     return path

# def breadth_first_search(graph, start_vertex, distances=dict()):
#     discovered_set = set()
#     frontier_queue = Queue()
#     visited_list = []
#
#     # start_vertex has a distance of 0 from itself
#     distances[start_vertex] = 0
#
#     frontier_queue.enqueue(start_vertex)  # Enqueue start_vertex in frontier_queue
#     discovered_set.add(start_vertex)  # Add start_vertex to discovered_set
#
#     while (frontier_queue.list.head != None):
#         current_vertex = frontier_queue.dequeue()
#         visited_list.append(current_vertex)
#         if current_vertex in graph:
#             for adjacent_vertex in graph[current_vertex].coArtists.keys():
#                 if adjacent_vertex not in discovered_set:
#                     frontier_queue.enqueue(adjacent_vertex)
#                     discovered_set.add(adjacent_vertex)
#
#                     # Distance of adjacent_vertex is 1 more than current_vertex
#                     distances[adjacent_vertex] = distances[current_vertex] + 1

# res = {'0': int(), '1': int(), '2': int(), '3': int(), '4': int(), '5': int(), '6': int(), '7': int()}
# for i in distances.values():
#     if i == 0: res['0'] += i
#     if i == 1: res['1'] += i
#     if i == 2: res['2'] += i
#     if i == 3: res['3'] += i
#     if i == 4: res['4'] += i
#     if i == 5: res['5'] += i
#     if i == 6: res['6'] += i
#     if i == 7: res['7'] += i

# # k = [i for i in res.values()]
# j = [i for i in distances.values()]
# # distances.values()
# return distances

# def breadth_first_search(graph, start_vertex, distances=None):
#     frontierQueue = Queue()
#     discoveredSet = set()
#     visited = []
#     if distances is None:
#         distances = {}
#
#     distances[start_vertex] = 0
#     frontierQueue.enqueue(start_vertex)
#     discoveredSet.add(start_vertex)
#     while frontierQueue:
#         currV = frontierQueue.dequeue()
#         visited.append(currV)
#         for ver in graph[start_vertex].coArtists:
#             if ver not in discoveredSet:
#                 frontierQueue.enqueue(ver)
#                 discoveredSet.add(ver)
#                 distances[ver] = distances[currV] + 1
#     return visisted
