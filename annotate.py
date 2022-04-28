from getkey import getkey, keys


def print_buf(buffer):
    print(" ".join(buffer), end="\r")


with open("manual_annotation.txt", "r") as f:
    lines = [tuple(el.split("@@@ ")) for el in f.read().split("\n")]
    lines.remove(("",))
    # lines = [map(lambda x: (int(x[0]), x[1]), line) for line in lines]
    for i, line in enumerate(lines):
        lines[i] = (int(line[0]), line[1])

output = ["idx, irony"]

for idx, tweet in lines:
    print("\n\n")
    print(tweet)
    print()
    print("Make a selection")
    buffer = [">", "Not irony", "|", "Irony"]
    print_buf(buffer)
    key = getkey()
    while key != keys.ENTER:
        if key == keys.LEFT:
            buffer.remove(">")
            buffer.insert(0, ">")
            print_buf(buffer)
        elif key == keys.RIGHT:
            buffer.remove(">")
            buffer.insert(2, ">")
            print_buf(buffer)
        key = getkey()
    print(" ".join(buffer))
    index = buffer.index(">")
    choice = 1 if index == 2 else 0
    output.append(f"{idx}, {choice}")


name = input("Type your name: ")
with open(f"annotation_result_{name}.txt", "w") as f:
    f.write("\n".join(output))
