import csv
from graph import Graph, Point
import numpy as np
import datetime


size = 1000
array = np.ones((size, size))
array[500:700, 0:300] += 1
array[298:303, 0:300] += 1
array[590:610, 330:410] += 1
array[600:700, 430:440] += 1

with open('wyniki.csv', 'a', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['liczba nodow', 'nody ogolem', 'czas tworzenia grafu', 'czas szukania sciezki'])

amounts = (2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200)
for i in amounts:
    graph = Graph()
    start1 = datetime.datetime.now()
    graph.generate_from_map(array, i)
    duration1 = datetime.datetime.now() - start1
    print('-------------------------------------')
    print(i)
    print(duration1)
    start2 = datetime.datetime.now()
    x = graph.get_path(Point(10, 10), Point(650, 350))
    duration2 = datetime.datetime.now() - start2
    print(duration2)
    print('-------------------------------------')

    with open('wyniki.csv', 'a', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([i, i*i, duration1, duration2])
