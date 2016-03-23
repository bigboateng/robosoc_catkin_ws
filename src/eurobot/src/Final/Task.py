#!usr/bin/env python
class Task:
    def __init__(self, coordinates, actions):
        """
        coordinates = [(),(),(),()]
        actions = ['pickUp', 'closeDoors', 'doNothing']
        """
        self.actions = actions
        self.coordinates = coordinates
        self.fakePaths = [('t', 0.0), ('d', 0.0), ('t', 1.89), ('d', 36.4),
                          ('t', 0.79), ('d', 7.07), ('t', 0.0)]

  
    def generatePath(self, currentPosition):
        """
        param currentPosition: tuple of currentPosition (x,y)
        returns: generate all the paths, actions and put them in one list
        """
        # loop through all actions and generate path
        paths = []
        for action in self.actions:
            """Tipically it would be """
            paths.extend(self.fakePaths)
            paths.append(('action', action))
        return paths
