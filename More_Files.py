from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could to these on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"{from_file}'s content:\n{len(indata)} bytes\n\n{indata}")

print(f"Output file exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()