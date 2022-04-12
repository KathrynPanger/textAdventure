from item import Item
#room_data = read_rooms("data/rooms.txt")

class Room:
    def __init__(self, name: str,
                 description: str,
                 exits: list[str],
                 contents: list[Item]):
        self.name = name
        self.is_visted = False
        self.has_properties = False
        self.description = description
        self.exits = exits
        self.contents = contents

    def __repr__(self):
        return f"Room Object: {self.name}"

    def __hash__(self):
        return hash((self.name))

    def visit(self):
        self.is_visted = True




