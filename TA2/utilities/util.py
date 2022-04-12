def read_rooms(room_file):
    with open(room_file) as f:
        corpus = f.read()
        text = corpus.split("\n")
        all_rooms = {}
        one_room= {}
        for info_string in text:
            if info_string:
                properties = info_string.split(": ")
                property_type = properties[0]
                property_content = properties[1]
                room_listables = ["exits", "contents"]
                if property_type in room_listables:
                    property_content = property_content.split(",")
                one_room[property_type] = property_content

            else:
                all_rooms[one_room["name"]] = one_room
                one_room = {}
        return (all_rooms)
