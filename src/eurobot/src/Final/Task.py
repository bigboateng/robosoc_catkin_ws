#!usr/bin/env python
class Task:
    def __init__(self,name, coordinates, actions):
        """
        coordinates = [(),(),(),()]
        actions = ['pickUp', 'closeDoors', 'doNothing']
        """
        self.name = name
        self.actions = actions
        self.coordinates = coordinates

  
    def generatePath(self, planner, currentPos):
        """
        param currentPosition: tuple of currentPosition (x,y)
        returns: generate all the paths, actions and put them in one list
        """
        # loop through all actions and generate path
        paths = []
        actions = self.actions
        coordinates = self.coordinates
        lastPosition = (None, None)
        for i in range(len(self.actions)):
            """Tipically it would be """
##            planner = PathPlanner()
##            path = planer.getPath(currentPos,coordinates[i],10,12)
            if i == 0:
##                print("Starting at {}".format(currentPos))
                paths.extend(planner.getPath(currentPos, coordinates[i],0,0))
                paths.append(('action',actions[i]))
                lastPosition = coordinates[0]
            else:
##                print("Starting at {}".format(lastPosition))
                paths.extend(planner.getPath(lastPosition, coordinates[i],0,0))
                paths.append(('action',actions[i]))
                lastPosition = coordinates[i]
            
        return paths

    def get_name(self):
        return self.name
