from graph import Graph, Point
import numpy as np
import matplotlib.pyplot as plt
import datetime

size = 1000
array = np.ones((size, size))
array[500:700, 0:300] += 1
array[298:303, 0:300] += 1
array[590:610, 330:410] += 1
array[600:700, 430:440] += 1

start = datetime.datetime.now()
graph = Graph()
graph.generate_from_map(array, 100)
duration = datetime.datetime.now() - start
print('-------------------------------------')
print(duration)
#print('grafik ok')


start = datetime.datetime.now()
x = graph.get_path(Point(50, 50), Point(650, 350))
duration = datetime.datetime.now() - start
print(duration)

# x1 = list()
# y1 = list()
# xs = list()
# ys = list()
#
# for node in graph.nodes:
#     xs.append(node.position.x)
#     ys.append(node.position.y)
#     for n in node.neighbours:
#         plt.plot((node.position.x, n[0].position.x), (node.position.y, n[0].position.y), 'k-', lw=2)
#
# for node in x:
#     x1.append(node.position.x)
#     y1.append(node.position.y)
# plt.plot(xs, ys, 'ro')
# plt.plot(x1, y1, 'g', lw=5)
# plt.axis([0, size, size, 0])
# plt.show()
