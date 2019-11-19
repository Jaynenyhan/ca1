#!/usr/bin/env python

with open("irish-dobs.txt") as f_input:
   lines = f_input.readlines()

i = 0
while i < len(lines):
   tokens = lines[i].split()
   date = tokens[0].split("/")
   tmp = date[0]
   date[0] = date[1]
   date[1] = tmp
   tokens[0] = "/".join(date)
   lines[i] = " ".join(tokens)
   i = i + 1

with open("american-dobs.txt", "w") as f_output:
   output = "\n".join(lines) + "\n"
   f_output.write(output)
