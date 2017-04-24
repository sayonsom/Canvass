"""Usage: operate.py <filename>

Options:
    -o  open this file
"""


from shutil import copyfile
import docopt




with open('ieee14bus.txt', 'r') as input_file, open('ieee14bus2.txt', 'w') as output_file:
    for line in input_file:
        if 'sw1' in line:
            line2 = line.replace("True","False")
            output_file.write(line2)
        else:
            output_file.write(line)
