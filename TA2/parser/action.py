from enum import Enum, auto

class Action(Enum):

    #Default Actions
    TAKE = auto(),
    DROP = auto(),
    OPEN = auto(),
    CLOSE = auto(),
    SWITCH_ON = auto(),
    SWITCH_OFF = auto(),
    PUT_ON = auto(),
    PUSH = auto(),
    PULL = auto(),
    USE_WITH = auto(),
    EXAMINE = auto(),
    LOOK = auto(),
    INVENTORY = auto(),
    GO_TO = auto(),
    TALK_TO = auto(),

    #Special Actions
    READ = auto(),
    SHAKE = auto(),
    EAT = auto(),
    DRINK = auto(),
    CAST = auto()

    #Spells
    REZROV = auto()


