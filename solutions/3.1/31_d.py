while (line := input()) != "":
    if line.endswith("@@@"):
        pass
    elif line.startswith("##"):
        print(line[2:])
    else:
        print(line)
