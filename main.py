from dataclasses import dataclass

import command as c
import action
check = c.validateCommand("take book", action.Action)
print(c.spellList)
