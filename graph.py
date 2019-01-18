import numpy as np
import matplotlib.pyplot as plt
import Djikstra
import datetime


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, point):
        return np.sqrt(((self.x-point.x)*(self.x-point.x)) + ((self.y-point.y)*(self.y-point.y)))


class Node:
    def __init__(self, x, y):
        self.position = Point(x,y)
        self.neighbours = list()

    def get_distance(self, point):
        return self.position.get_distance(point)

    def add_neighbour(self, new_neighbour, weight):
        on_list = False
        if new_neighbour is not self:
            for n in self.neighbours:
                if n[0] is new_neighbour:
                    on_list = True
            if not on_list:
                self.neighbours.append((new_neighbour, weight))
                new_neighbour.add_neighbour(self, weight)

    def tell_position(self):
        return self.position.x, self.position.y

    def get_vector(self, n):
        x = self.position.x - n.position.x
        y = self.position.y - n.position.y
        return (x, y)


class Graph:
    def __init__(self):
        self.nodes = list()
        self.weights = {}
        self.distance_between = 0

    def find_closest(self, point):
        closest = None
        i = 0.5
        while closest is None:
            for node in self.nodes:
                x, y = node.tell_position()
                if point.x-self.distance_between*i <= x <= point.x+self.distance_between*i and \
                        point.y-self.distance_between*i <= y <= point.y+self.distance_between*i:

                    distance = node.get_distance(point)
                    if closest is None:
                        closest = (node, distance)
                    elif distance < closest[1]:
                        closest = (node, distance)
            i += 0.5
        return closest[0]

    def generate_from_map(self, map, density):
        self.distance_between = int(map.shape[0]/density)
        #print(distance_between)
        size = (int(map.shape[0]/self.distance_between), int(map.shape[1]/self.distance_between))
        for y in range(1, size[0]+1):
            for x in range(1, size[1]+1):
                new = Node(int((x-0.5)*self.distance_between), int((y-0.5)*self.distance_between))
                self.nodes.append(new)
        self.nodes = tuple(self.nodes)
        for node in self.nodes:
            sumx, sumy, sumxy, sumyx= 0, 0, 0, 0
            for i in range(1, self.distance_between+1):
                if node.position.x < map.shape[0]-self.distance_between:
                    sumx += map[node.position.x+i, node.position.y]
                if node.position.y < map.shape[1]-self.distance_between:
                    sumy += map[node.position.x, node.position.y+i]
                if node.position.x < map.shape[0]-self.distance_between and node.position.y < map.shape[1]-self.distance_between:
                    sumxy += map[node.position.x+i, node.position.y+i]
                if node.position.x > self.distance_between and node.position.y < map.shape[1]-self.distance_between:
                    sumyx += map[node.position.x - i, node.position.y + i]
            if 0 < sumx < self.distance_between+1:
                node.add_neighbour(self.find_closest(Point(node.position.x+self.distance_between, node.position.y)), 1.)
            if 0 < sumy < self.distance_between+1:
                node.add_neighbour(self.find_closest(Point(node.position.x, node.position.y+self.distance_between)), 1.)
            if 0 < sumxy < self.distance_between+1:
                node.add_neighbour(self.find_closest(Point(node.position.x+self.distance_between, node.position.y+self.distance_between)), 1.4)
            if 0 < sumyx < self.distance_between+1:
                node.add_neighbour(self.find_closest(Point(node.position.x-self.distance_between, node.position.y+self.distance_between)), 1.4)

    def get_path(self, start, end):
        start_node = self.find_closest(start)
        end_node = self.find_closest(end)
        x = Djikstra.find_way(start_node, end_node)
        return x





