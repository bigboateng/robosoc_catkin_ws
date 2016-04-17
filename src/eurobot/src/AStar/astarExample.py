from astar import PathPlanner

planner = PathPlanner()

instructs = planner.getPath((0,0), (0,10), 180, 180);

for i in instructs:
    print(i)

obstPos = (0,5)
planner.add_obsticle(obstPos,0)

instructs = planner.getPath((0,10), (0,0), 180, 0);
print("\n On the way back \n")    
for i in instructs:
    print(i)

instructs = planner.getPath((0,0), (0,10), 0, 180);
print("\n And going back down again \n")    
for i in instructs:
    print(i)

planner.delete_obsticle()

instructs = planner.getPath((0,10), (0,0), 180, 0);
print("\n On the way back to the top again\n")    
for i in instructs:
    print(i)
