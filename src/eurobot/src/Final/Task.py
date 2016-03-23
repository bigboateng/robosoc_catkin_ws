#!usr/bin/env python
##from astar import *
class Task:
    def __init__(self, coordinates, actions):
        """
        coordinates = [(),(),(),()]
        actions = ['pickUp', 'closeDoors', 'doNothing']
        """
        self.actions = actions
        self.coordinates = coordinates
        self.fakePaths = [('t', 1.89), ('d', 36.4),
                          ('t', 0.79), ('d', 7.07), ('t', 0.0)]

  
    def generatePath(self, currentPos):
        """
        param currentPosition: tuple of currentPosition (x,y)
        returns: generate all the paths, actions and put them in one list
        """
        # loop through all actions and generate path
        paths = []
        actions = self.actions
        coordinates = self.coordinates  
        for i in range(len(self.actions)):
            """Tipically it would be """
##            planner = PathPlanner()
##            path = planer.getPath(currentPos,coordinates[i],10,12)
            paths.extend(self.fakePaths)
            paths.append(('action',actions[i]))
        return paths
