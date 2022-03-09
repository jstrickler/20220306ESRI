import fileinput
import arg


target = "lizard"

for raw_line in fileinput.input():
    if target in raw_line:
        print(fileinput.filename(), raw_line.rstrip())
