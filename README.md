# 2d Maze Solver 

## Algorithms :
- **BFS**
- **A***
- **Dijkstra**

##Usage : 
### Parameters :
- **Image :** (str) Path of maze image.
- **Algorithm :** (str) Algorithm to use (Default BFS).
- **Tolernace :** (int) Adjust tolernace from walls in pixels. (Currently coners are edge cases)
- ** Interploation :** (int) no of sparse points in path. Return path with less points than original path.

###Note : On running code the grid will open where you have to select start and end points using mouse. This is done for general support of 2d grids and maze.

```python

    from Solver import MazeSolver
    maze_solver = MazeSolver('maze.png',algo='bfrs',wall_tolerance=5)
    maze_solver.run()

```



