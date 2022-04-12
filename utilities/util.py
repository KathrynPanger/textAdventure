# from pydub import AudioSegment
# from pydub.utils import make_chunks

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


# def sliceSound(path: Path, lengthInSeconds: int, filename: str,
#                inputformat = "mp3", outputformat = "wav")
#     myaudio = AudioSegment.from_file(path , inputformat)
#     chunk_length_s = lengthInSeconds
#     chunk_length_ms = 1000 * chunk_length_s # pydub calculates in millisec
#     chunks = make_chunks(myaudio, chunk_length_ms)
#     sample = chunks[0]
#     #Export all of the individual chunks as wav files
#     sample.export(filename, format=outputformat)