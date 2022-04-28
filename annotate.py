from getkey import getkey, keys
from time import sleep
from sys import stdout


def print_buf(buffer):
    print(" ".join(buffer), end="\r")


ERASE_LINE = '\x1b[2K'
CURSOR_UP_ONE = '\x1b[1A'

with open("manual_annotation.txt", "r") as f:
    lines = [tuple(el.split("@@@ ")) for el in f.read().split("\n")]
    lines.remove(("",))
    # lines = [map(lambda x: (int(x[0]), x[1]), line) for line in lines]
    for i, line in enumerate(lines):
        lines[i] = (int(line[0]), line[1])

output = ["idx, irony"]
buffer = [">", "Not irony", "|", " ", "Irony"]

for idx, tweet in lines:
    print(tweet)
    print("Make a selection")
    print_buf(buffer)
    key = getkey()
    while key != keys.ENTER:
        if key == keys.LEFT:
            buffer[0] = ">"
            buffer[3] = " "
            print_buf(buffer)
        elif key == keys.RIGHT:
            buffer[3] = ">"
            buffer[0] = " "
            print_buf(buffer)
        key = getkey()
    print(" ".join(buffer))
    index = buffer.index(">")
    choice = 1 if buffer[3] == ">" else 0
    output.append(f"{idx}, {choice}")
    # sleep(0.3)
    for i in range(3):
        stdout.write(CURSOR_UP_ONE)
        stdout.write(ERASE_LINE)


name = input("Type your name: ")
with open(f"annotation_result_{name}.csv", "w") as f:
    f.write("\n".join(output))
