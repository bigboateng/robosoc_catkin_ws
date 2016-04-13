from astar import PathPlanner

planner = PathPlanner()
start, end = (0,0), (0,3)
instructs = planner.getPath(start, end, 0, 0);
    
for i in instructs:
    print(i)
