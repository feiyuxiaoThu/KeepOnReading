import random
from stastar.planner import Planner

grid_size, cell_size, domain_size = 20, 1, 1

static_obstacles = [(0, 0), (10, 8), (10, 10), (10, 12), (12, 12), (grid_size-1, grid_size-1)]

dynamic_obstacles = {}    
for seed in (8, 10, 16, 18):  # create dynamic obstacles
    random.seed(seed)    
    x0, y0, x1, y1 = [random.randint(2, grid_size-3) for _ in (0, 1, 2, 3)]
    start, goal = (x0, y0), (x1, y1)
    planner = Planner(cell_size, domain_size, static_obstacles)
    path = planner.plan(start, goal, dynamic_obstacles)
    for step, coord in enumerate(path):
        if step not in dynamic_obstacles:
            dynamic_obstacles[step] = []
        dynamic_obstacles[step].append(coord)

start, goal = (3, 3), (17, 17)
planner = Planner(cell_size, domain_size, static_obstacles)
path = planner.plan(start, goal, dynamic_obstacles, debug=True)

print(path)
