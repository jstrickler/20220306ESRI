
file_path = "DATA/mary.txt"

with open(file_path) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)

