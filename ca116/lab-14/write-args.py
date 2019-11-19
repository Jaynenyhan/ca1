#!/usr/bin/env python

import sys
args = sys.argv[2:]

message = "\n".join(args)
file_name = sys.argv[1]

with open(file_name, "w") as fd:
   fd.write(message + "\n")
