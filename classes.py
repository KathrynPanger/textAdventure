import enum

class Action(enum.Enum):

    #base action
    take = enum.auto()
    drop = enum.auto()
    use = enum.auto()
    openIt = enum.auto()
    closeIt = enum.auto()
    look = enum.auto()
    read = enum.auto()
    push = enum.auto()
    pull = enum.auto()
    switchOn = enum.auto()
    switchOff = enum.auto()
    toggle = enum.auto()
    inventory = enum.auto()
    go = enum.auto()
    fail = enum.auto()
    cast = enum.auto()

    #spells
    rezrov = enum.auto()
    kendall = enum.auto()
    spakemoon = enum.auto()
    frotz = enum.auto()
    gnustu = enum.auto
