from levels_manager.star import Star

def read_melody(file):
    file = open(file, "r")
    output = {}
    for line in file:
        content = line.split(":")
        output[float(content[0])] = content[1][:-1]
    file.close()
    return output


def read_level(file):
    file = open(file, "r")
    output = []
    for line in file:
        content = line[:-1].split(",")
        print(content)
        output.append(Star(content[0],(int(content[1]),int(content[2]))))
    file.close()
    return output