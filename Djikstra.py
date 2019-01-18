import numpy as np


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(vector1, vector2):
    v1_u = unit_vector(vector1)
    v2_u = unit_vector(vector2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def find_way(initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node is not end:
        if current_node is not initial:
            vec_before = current_node.get_vector(one_back_node)
        else:
            angle_hardness = 0
        visited.add(current_node)
        destinations = current_node.neighbours
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            if current_node is not initial:
                vec_after = next_node[0].get_vector(current_node)
                angle = angle_between(vec_before, vec_after)
                angle_hardness = np.power(angle, angle)
                #print(current_node.tell_position(), one_back_node.tell_position())
                #print(vec_before, unit_vector(vec_before))
                #print(next_node[0].tell_position(), current_node.tell_position())
                #print(vec_after, unit_vector(vec_after))
                #print(angle, angle_hardness)
            weight = next_node[1] + weight_to_current_node + angle_hardness
            if next_node[0] not in shortest_paths:
                shortest_paths[next_node[0]] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node[0]][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node[0]] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        one_back_node = next_destinations[current_node][0]

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

