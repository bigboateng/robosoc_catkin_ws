from astar import PathPlanner

planner = PathPlanner()
start, end = (15,20), (45,20)
instructs = planner.getPath(start, end, 10, 12);
    
for i in instructs:
    print(i)
