from collections.abc import Iterable, Iterator


class InputReader:
    def __init__(self, stream: Iterable[str]):
        self.stream = ''.join(stream)

    def peek(self, n: int = 1) -> str:
        if n > len(self.stream):
            raise IndexError("Out of bounds")
        return self.stream[:n]

    def consume(self, n: int = 1) -> str:
        ret = self.peek(n)
        self.stream = self.stream[n:]
        return ret

    def is_EOF(self) -> bool:
        return len(self.stream) == 0

    def __iter__(self) -> Iterator[str]:
        while not self.is_EOF():
            yield self.consume()

IR = InputReader("this is the song that never ends")

while not IR.is_EOF():
    n = 1
    try:
        while not IR.peek(n).endswith(" "):
            n += 1
    except IndexError:
        pass
    token = IR.consume(n-1)
    try:
        IR.consume(1)
    except IndexError:
        pass
    print(token)