from getkey import getkey, keys
from time import sleep
from sys import stdout


def print_buf(buffer):
    "Prints the selection buffer and returns the cursor to the start"
    print(" ".join(buffer), end="\r")


ERASE_LINE = '\x1b[2K'
CURSOR_UP_ONE = '\x1b[1A'


# Read in the tweets for manual annotation
with open("manual_annotation.txt", "r") as f:
    # Read the tweet index and content
    lines = [tuple(el.split("@@@ ")) for el in f.read().split("\n")]
    lines.remove(("",))
    # Replace each element in the lines list with a tuple of the tweet's index and content
    for i, line in enumerate(lines):
        lines[i] = (int(line[0]), line[1])

output = ["idx, irony"]
buffer = [">", "Not irony", "|", " ", "Irony"]

for idx, tweet in lines:
    # Print the tweet and selection buffer
    print(tweet)
    print("Make a selection")
    print_buf(buffer)
    # Get keyboard input
    # Break on ENTER pressed, if < or > is pressed, move cursor accordingly
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
    # Get the position of the cursor and save the choice
    index = buffer.index(">")
    choice = 1 if buffer[3] == ">" else 0
    output.append(f"{idx}, {choice}")
    # Move up cursor once to replace tweet text
    for i in range(3):
        stdout.write(CURSOR_UP_ONE)
        stdout.write(ERASE_LINE)

# Save the results to a csv
name = input("Type your name: ")
with open(f"annotation_result_{name}.csv", "w") as f:
    f.write("\n".join(output))