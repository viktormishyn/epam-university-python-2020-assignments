#!/bin/bash

# this script automates creating a number of folders for the course assignments repository
# each folder is called <Task{n}> and contains empty readme.md file

for n in {1..15}; do
  mkdir "Task$n"
done;

for d in */; do
  touch "${d}readme.md"
done;
