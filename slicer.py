from pydub import AudioSegment
from pydub.utils import make_chunks

def sliceSound(path: Path, lengthInSeconds: int, filename: str,
               inputformat = "mp3", outputformat = "wav")
    myaudio = AudioSegment.from_file(path , inputformat)
    chunk_length_s = lengthInSeconds
    chunk_length_ms = 1000 * chunk_length_s # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms)
    sample = chunks[0]
    #Export all of the individual chunks as wav files
    sample.export(filename, format=outputformat)