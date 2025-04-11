#!/bin/bash

if
  [ -f "/tmp/file" ]
  echo "File exists"
then
  echo "Doing something"
  for i in {1..5}; do
    echo "Iteration $i"
  done
else
  echo "File does not exist"
fi
