import cv2
import numpy as np
from collections import deque
from algorithms import *


class MazeSolver:
    def __init__(self, image_path,algo='bfs',wall_tolerance = 5):
        self.image_path = image_path
        self.start_point = None
        self.end_point = None
        self.maze_grid = None
        self.image_with_path = None
        self.algo = algo
        self.planner = None
        self.wall_tolerance = wall_tolerance

        
        if algo == 'bfs':

            self.planner = BFS()

        elif algo == 'A*':
            self.planner = AStar()

        elif algo == 'Dijkstra':
            self.planner = Dijkstra()
        else :

            print(f"No implementation found for {algo} , availble implementations are BFS , A*  and Dijkstra . Switching to BFS")
            self.planner = BFS()







    def load_maze(self):
        image = cv2.imread(self.image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        _, binary_maze = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        self.maze_grid = (binary_maze // 255).astype(np.uint8)
        self.image_with_path = image.copy()

    def interpolate_path(self,path,points):
        off_set= len(path)/points
        new_length = int(off_set*points)
        new_path = []
        for i in range(0,new_length,int(off_set)):
            new_path.append(path[i])
        return new_path
    

    def adjust_tolerance(self,path):

        new_path=[]
        for nr, nc in path:
            r=nr
            c= nc
            if self.maze_grid[r+1,c] ==0:
                r = r-5
            if self.maze_grid[r-1,c] ==0:
                r = r+5
            if self.maze_grid[r,c+1] ==0:
                c = c-5
            if self.maze_grid[r,c - 1] ==0:
                c = c+5

            if nc == c and nr == r:
                r = r+5
                c= c+5

        

            new_path.append((r,c))

        return new_path
        

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
            if self.start_point is None:
                self.start_point = (y, x)  # Set start point
                print(f"Start point set at: {self.start_point}")
            elif self.end_point is None:
                self.end_point = (y, x)  # Set end point
                print(f"End point set at: {self.end_point}")
                self.solve_maze()


    
    def solve_maze(self):
       

        path = self.planner.find_path(self.maze_grid,self.start_point,self.end_point)#self.bfs(self.maze_grid, self.start_point, self.end_point)

        if path:
            print(f"Path found: {len(path)} steps.")
            path = self.adjust_tolerance(path)
            path = self.interpolate_path(path,points=200)
            
            for i in range(len(path) - 1):
                cv2.line(self.image_with_path, (path[i][1], path[i][0]), (path[i + 1][1], path[i + 1][0]), (0, 0, 255), 1)
            cv2.imshow('Solved Maze', cv2.resize(self.image_with_path, (512, 512)))
        else:
            print("No path found.")

    def run(self):
        self.load_maze()
        print("Click to set the start point, then click to set the end point.")
        cv2.imshow('Maze', self.image_with_path)
        cv2.setMouseCallback('Maze', self.mouse_callback)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


