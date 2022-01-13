from dataclasses import dataclass

import validateCommand as vc
check = vc.validate("take book")
print(check)
