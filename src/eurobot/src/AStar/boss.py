def secondaryTasks:
    # setup
    # a list of all the inistial values needs to be added at some point
    setup = []
    setup.append("position,3,16") # is the initial position
    setup.append("direction,45") # initial bearing of 045deg y-axis being north line
    tasks = [] # instructions
    tasks.append("drive,24,20,notavoid") # go to point (12, 17) without trying to avaid obstacles
    tasks.append("pickUpTopBlock")
    tasks.append("drive,28,16,notavaid")
    tasks.append("dropTopBlock")
    tasks.append("drive,6,2,avoid") # align with the first door
    tasks.append("drive,6,0,notavoid") # slam the door shut
    tasks.append("reverse,6,2")
    tasks.append("drive,12,2,avoid") # align with the next door
    tasks.append("drive,12,0,notavoid") # slam into the next door
    #....
    #instructions to be added
    tasks.append("END") # halt at the end

    return setup,tasks

def primaryTasks:
    # setup
    # a list of all the inistial values needs to be added at some point
    setup = []
    setup.append("position,3,14") # is the initial position
    setup.append("direction,45") # initial bearing of 045deg y-axis being north line
    tasks = [] # instructions
    tasks.append("drive,28,14,avoid")
    tasks.append("pickupTower")
    #....
    #instructions to be added
    tasks.append("raiseParasol")
    tasks.append("END") # halt at the end
    return setup,tasks


setup, tasks = secondaryTasks()#change this according to the robot in use

machine = Machine()
machine.setup(setup)#set the setup

count = 0;
while machine.isRunning:
    machine.performTask(tasks[count]))
    while not (machine.isDone and machine.isFlagUp): #flag is an exception flag
        #wait;
        delay(10)

    if machine.flagIsUp:
        # shout that the machine is broken

    if machine.isDone:
        count+=1
