import cv2
import numpy as np
from collections import deque
import heapq

class PathPlanningAlgorithm:
    def find_path(self, maze, start, end):
        raise NotImplementedError("Subclasses should implement this method.")

class BFS(PathPlanningAlgorithm):
    def find_path(self, maze, start, end):
        rows, cols = maze.shape
        queue = deque([start])
        visited = set()
        visited.add(start)
        parent = {start: None}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            current = queue.popleft()
            if current == end:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 1 and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    parent[(nr, nc)] = current

        return None

class Dijkstra(PathPlanningAlgorithm):
    def find_path(self, maze, start, end):
        rows, cols = maze.shape
        pq = [(0, start)]
        distances = {start: 0}
        parent = {start: None}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            current_distance, current = heapq.heappop(pq)
            if current == end:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 1:
                    new_distance = current_distance + 1
                    if (nr, nc) not in distances or new_distance < distances[(nr, nc)]:
                        distances[(nr, nc)] = new_distance
                        heapq.heappush(pq, (new_distance, (nr, nc)))
                        parent[(nr, nc)] = current

        return None

class AStar(PathPlanningAlgorithm):
    def find_path(self, maze, start, end):
        rows, cols = maze.shape
        pq = [(0, start)]
        g_costs = {start: 0}
        parent = {start: None}

        def heuristic(point):
            return abs(point[0] - end[0]) + abs(point[1] - end[1])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            _, current = heapq.heappop(pq)
            if current == end:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 1:
                    new_g = g_costs[current] + 1
                    if (nr, nc) not in g_costs or new_g < g_costs[(nr, nc)]:
                        g_costs[(nr, nc)] = new_g
                        f_cost = new_g + heuristic((nr, nc))
                        heapq.heappush(pq, (f_cost, (nr, nc)))
                        parent[(nr, nc)] = current

        return None
