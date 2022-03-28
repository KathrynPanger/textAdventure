from readData import read_rooms
room_data = read_rooms("data/rooms.txt")

class Room:
    def __init__(self, name: str):
        self.name = name
        self.is_visted = False
        self.has_properties = False
        self.description: str
        self.exits: list
        self.contents: list[Item]
        self.player: Optional[Player] = None

    def __repr__(self):
        return f"{self.name}"

    def __hash__(self):
        return hash((self.name))

    def visit(self):
        self.is_visted = True

    def set_properties(self):
        if self.name in room_data:
            self.description = room_data[f"{self.name}"]["description"]
            self.exits = room_data[f"{self.name}"]["exits"].split(",")
            self.items = room_data[f"{self.name}"]["items"].split(",")
            self.has_properties = True
            print(f"{self.name} created")
        elif self.name:
            print(f"No room data found for {self.name}")
        else:
            pass




