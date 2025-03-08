def read_melody(file):
    file = open(file, "r")
    output = {}
    for line in file:
        content = line.split(":")
        output[content[0]] = content[1][:-1]
    file.close()
    return output

print(read_melody("resources/tutorial.txt"))