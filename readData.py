def read_rooms(room_file):
    with open(room_file) as f:
        corpus = f.read()
        text = corpus.split("\n")
        all_rooms = {}
        one_room= {}
        for info_string in text:
            if info_string:
                property = info_string.split(": ")
                one_room[property[0]] = property[1]

            else:
                all_rooms[one_room["name"]] = one_room
                one_room = {}
        return (all_rooms)
