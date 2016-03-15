class Machine:
    astar = AStar()
    
    #returns true if the there is a connection between the pi and arduino
    # and there is time left for it to finish
    ###TODO
    def isRunning:
        return True

    #returns true if the tast that the machine was performing has completed
    ###TODO
    def isDone:
        return True

    #returns true if the exception flag is up
    ###TODO
    def isFlagUp:
        return True

    #returns the current position of the robot given in squares
    ###TODO
    def getPos:
        ##gets the value from the arduino itself or some other code on the pi
        return x, y

    #this method takes a list of instructions and sends it to the arduino
    #this could either be a list or a single instruction
    def publish(inst):
        #TODO by Tony

    #returns instructions based on what the astar calculated
    #appends avoid or notavoid to the instruction
    def getPath(endX, endY, avoid):
        insts = astar.getPath(startX, startY, startDirection, endX, endY)
        

    # interprets the instruction sent by the boss
    # and sends specific instructions to the arduino
    ###TOFINISH
    def performTask(task):
        name = task.split(',')[0] #name of the task
        if name=="drive":
            endX = task.split(',')[1]
            endY = task.split(',')[2]
            avoid = task.split(',')[3]
            startX, startY = getPos()
            #aster calculates the new path and based on current x and y and direction
            insts = getPath(endX, endY, avoid)
            publish(insts)
            
        else if name == "reverse":
            endX = task.split(',')[1]
            endY = task.split(',')[2]
            startX, startY = getPos()
            #aster calculates the new path and based on current x and y and direction
            insts = getPath(endX, endY, avoid)
            publish(insts)

        else if name == "pickupTower":
            publish("pickupTower")

        #etc....

            
