from action import Action

#Action lists
takeList={"take","grab", "pick"}
dropList = {"put", "drop"}
useList={"combine","use", "put"}
openList={"open"}
closeList={"close", "shut"}
lookList={"look","examine"}
readList = {"read"}
pushList = {"push"}
pullList = {"pull"}
switchList = {"switch", "turn", "press", "flip"}
inventoryList = {"i", "inventory"}
goList = {"go", "move"}
droplist={"drop"}
castList = {"cast"}
directionList = {"n","s","e","w", "north","south","east","west","up","u","down","d"}
spellList={"rezrov", "kendall", "spakemoon", "throck", "frotz", "gnusto"}

#Command restructuring vars
twoWordsList={"pick up","check inventory", "look at"}
removeList={"up", "check", "switch", "with", "on", "in", "at", "the", "and"}


actionLists=(takeList | dropList | useList | openList | closeList | lookList |
    pushList | pullList | switchList | inventoryList | goList | directionList | droplist | castList | readList)


def validateCommand(command, Action):

    is_valid = True
    theAction = Action.fail
    theNoun = None
    theSecondNoun = None
    theCommand=command.lower().split()
    if theCommand[1] == "on":
        theCommand[1] = "onn"
        print(theCommand)
    firstWord=theCommand[0]
    secondWord= theCommand[1]
    lastWord= theCommand[-1]


    theCommand=[item for item in theCommand if item not in removeList]
    if firstWord not in actionLists or len(theCommand)>3:
        is_valid=False
    elif firstWord in goList or firstWord in directionList:
        theCommand = [item for item in theCommand if item not in goList]
        if len(theCommand) == 1 and theCommand[0] in directionList:
            theAction = Action.go
            theNoun = theCommand[0][0]
        else:
            is_valid=False
    elif firstWord in takeList:
        theAction= Action.take
        theNoun = secondWord
    elif firstWord in droplist:
        theAction=Action.drop
        theNoun = secondWord
    elif firstWord in useList and len(theCommand)==3:
        theAction= Action.use
        theNoun = secondWord
        theSecondNoun = lastWord
    elif firstWord in openList:
        theAction= Action.openIt
    elif firstWord in closeList:
        theAction= Action.closeIt
    elif firstWord in lookList and len(theCommand<=2):
        theAction=Action.look
        if len(theCommand)==2:
            theNoun = secondWord
        else:
            theNoun = secondWord
    elif firstWord in switchList:
        theNoun = secondWord
        if secondWord == "onn":
            theAction = Action.switchOn
        elif secondWord == "off":
            theAction = Action.switchOff
    elif firstWord in readList:
        theAction=Action.read
        theNoun = secondWord
    elif firstWord in pushList:
        theAction = Action.push
        theNoun = secondWord
    elif firstWord in pullList:
        theAction=Action.pull
        theNoun = secondWord
    elif firstWord in castList and secondWord in spellList:
        theAction = Action.cast
        theNoun=secondWord
        theSecondNoun=lastWord
    elif firstWord in inventoryList and len(theCommand == 1):
        theAction = Action.inventory
        theNoun="i"
    else:
        is_valid = False

    return(is_valid,theAction,theNoun, theSecondNoun)
