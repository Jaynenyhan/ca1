#!/usr/bin/env python

message = "Hello world."
file_name = "hello.txt"

with open(file_name, "w") as fd:
   fd.write(message + "\n")
