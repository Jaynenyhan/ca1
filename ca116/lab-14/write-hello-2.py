#!/usr/bin/env python

import sys

message = "Hello world."
file_name = sys.argv[1]

with open(file_name, "w") as fd:
   fd.write(message + "\n")
