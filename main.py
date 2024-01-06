# main python file

# Level 0
print("----------------------------------------")
print("Level 0")
print("----------------------------------------")
n2 = [[0, 3366, 2290, 3118, 1345, 854, 1176, 1291, 1707, 2160, 1606, 702, 1820, 1985, 1838, 1515, 3370, 1643, 2874, 1418, 2495],
[3366, 0, 1076, 512, 2021, 2512, 2190, 2075, 1923, 1206, 1760, 2664, 1546, 1645, 1528, 1851, 376, 1723, 492, 1948, 1135],
[2290, 1076, 0, 1494, 945, 1436, 1114, 999, 2905, 536, 684, 1588, 876, 2627, 452, 775, 1358, 647, 716, 872, 2117],
[3118, 512, 1494, 0, 1773, 2264, 1942, 1827, 1411, 958, 1512, 2416, 1298, 1133, 1280, 1603, 252, 1475, 778, 1700, 623],
[1345, 2021, 945, 1773, 0, 491, 403, 650, 2348, 815, 261, 787, 475, 2070, 493, 170, 2025, 298, 1529, 763, 1560],
[854, 2512, 1436, 2264, 491, 0, 322, 569, 2429, 1306, 752, 868, 966, 2151, 984, 661, 2516, 789, 2020, 682, 1641],
[1176, 2190, 1114, 1942, 403, 322, 0, 247, 2751, 984, 430, 1190, 722, 2473, 662, 521, 2194, 467, 1698, 360, 1963],
[1291, 2075, 999, 1827, 650, 569, 247, 0, 2998, 869, 677, 1437, 969, 2720, 547, 768, 2079, 352, 1583, 127, 2210],
[1707, 1923, 2905, 1411, 2348, 2429, 2751, 2998, 0, 2369, 2321, 1561, 2029, 278, 2553, 2230, 1663, 2646, 2189, 3111, 788],
[2160, 1206, 536, 958, 815, 1306, 984, 869, 2369, 0, 554, 1458, 340, 2091, 322, 645, 1210, 517, 714, 742, 1581],
[1606, 1760, 684, 1512, 261, 752, 430, 677, 2321, 554, 0, 904, 292, 2043, 232, 91, 1764, 325, 1268, 790, 1533],
[702, 2664, 1588, 2416, 787, 868, 1190, 1437, 1561, 1458, 904, 0, 1118, 1283, 1136, 813, 2668, 1085, 2172, 1550, 1793],
[1820, 1546, 876, 1298, 475, 966, 722, 969, 2029, 340, 292, 1118, 0, 1751, 524, 305, 1550, 617, 1054, 1082, 1241],
[1985, 1645, 2627, 1133, 2070, 2151, 2473, 2720, 278, 2091, 2043, 1283, 1751, 0, 2275, 1952, 1385, 2368, 1911, 2833, 510],
[1838, 1528, 452, 1280, 493, 984, 662, 547, 2553, 322, 232, 1136, 524, 2275, 0, 323, 1532, 195, 1036, 558, 1765],
[1515, 1851, 775, 1603, 170, 661, 521, 768, 2230, 645, 91, 813, 305, 1952, 323, 0, 1855, 416, 1359, 881, 1442],
[3370, 376, 1358, 252, 2025, 2516, 2194, 2079, 1663, 1210, 1764, 2668, 1550, 1385, 1532, 1855, 0, 1727, 642, 1952, 875],
[1643, 1723, 647, 1475, 298, 789, 467, 352, 2646, 517, 325, 1085, 617, 2368, 195, 416, 1727, 0, 1231, 465, 1858],
[2874, 492, 716, 778, 1529, 2020, 1698, 1583, 2189, 714, 1268, 2172, 1054, 1911, 1036, 1359, 642, 1231, 0, 1456, 1401],
[1418, 1948, 872, 1700, 763, 682, 360, 127, 3111, 742, 790, 1550, 1082, 2833, 558, 881, 1952, 465, 1456, 0, 2323],
[2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323, 0]]

import sys

def nearest_neighbor_algorithm(cost_matrix, start_node):
    n = len(cost_matrix)
    visited = [False] * n
    path = [start_node]
    total_distance = 0

    for _ in range(n - 1):
        current_node = path[-1]
        min_distance = sys.maxsize
        next_node = -1

        for neighbor in range(n):
            if not visited[neighbor] and cost_matrix[current_node][neighbor] < min_distance:
                min_distance = cost_matrix[current_node][neighbor]
                next_node = neighbor

        path.append(next_node)
        total_distance += min_distance
        visited[next_node] = True

    total_distance += cost_matrix[path[-1]][start_node]
    path.append(start_node)

    path.remove(start_node)
    return path, total_distance

start_node = 20
optimal_path, optimal_distance = nearest_neighbor_algorithm(n2, start_node)

print(f"The optimal path is {optimal_path}.")
print(f"The optimal distance is {optimal_distance}.")


# Level 1A
print("----------------------------------------")
print("Level 1A")
print("----------------------------------------")
def tsp_knapsack(adj_matrix, source, destination, weights, total_capacity):
    n = len(adj_matrix)
    visited = 1 << source
    memo = {}
    def tsp_masked(mask, pos):
        if (mask, pos) in memo:
            return memo[(mask, pos)]
        
        if mask == (1 << len(destination)) - 1:
            return adj_matrix[pos][source], [pos, source]
        
        min_distance = sys.maxsize
        optimal_path = []
        
        for i in range(len(destination)):
            if not (mask & (1 << i)):
                new_mask = mask | (1 << i)
                new_pos = destination[i]
                if weights[i] <= total_capacity:
                    new_capacity = total_capacity - weights[i]
                    distance, path = tsp_masked(new_mask, new_pos)
                    distance += adj_matrix[pos][new_pos]
                    if distance < min_distance:
                        min_distance = distance
                        optimal_path = [pos] + path
                        memo[(mask, pos)] = (min_distance, optimal_path)
        
        return min_distance, optimal_path
    
    min_distance, optimal_path = tsp_masked(visited, source)
    
    return min_distance, optimal_path

source_point = 0
destination_points = [5,8,12,10,5,7,5]
weights = [12,13,5,10,3,2,14]
total_capacity = 35

shortest_distance, optimal_path = tsp_knapsack(n2, source_point, destination_points, weights, total_capacity)

print(f"Shortest Distance: {shortest_distance}")
print("Optimal Path:", optimal_path)

# Level 1B




